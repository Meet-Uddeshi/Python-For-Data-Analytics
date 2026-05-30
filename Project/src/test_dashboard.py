import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.widgets import CheckButtons, Slider, TextBox
from matplotlib.gridspec import GridSpec
from matplotlib.dates import date2num
import datetime

# --- Theme Constants ---
COLORS = {
    'bg': '#0A0E1A',
    'card': '#141B2D',
    'accent': '#B5924C',
    'bullish': '#26A69A',
    'bearish': '#EF5350',
    'font': '#FFFFFF',
    'font_secondary': '#A0AEC0',
    'grid': '#2A3550',
    'ma20': '#B5924C',
    'ma50': '#4A90D9',
    'ma200': '#FFFFFF',
}

# Apply base styles
plt.rcParams.update({
    'figure.facecolor': COLORS['bg'],
    'axes.facecolor': COLORS['bg'],
    'axes.edgecolor': COLORS['grid'],
    'axes.labelcolor': COLORS['font_secondary'],
    'text.color': COLORS['font'],
    'xtick.color': COLORS['font_secondary'],
    'ytick.color': COLORS['font_secondary'],
    'grid.color': COLORS['grid'],
    'grid.alpha': 0.3,
    'axes.titlecolor': COLORS['font'],
})

# --- Data Loading ---
def load_data():
    base_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    files = [
        'gs_barchart.csv',
        'gs_investing_com.csv',
        'gs_marketwatch.csv',
        'gs_yahoo_finance.csv'
    ]
    
    dfs = []
    for f in files:
        path = os.path.join(base_dir, f)
        if os.path.exists(path):
            df = pd.read_csv(path)
            # Normalize columns
            df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
            dfs.append(df)
            
    if not dfs:
        raise FileNotFoundError("No CSV files found in data directory.")
        
    merged = pd.concat(dfs, ignore_index=True)
    
    # Parse dates
    merged['date'] = pd.to_datetime(merged['date'], utc=True).dt.tz_localize(None)
    
    # Ensure numeric
    numeric_cols = ['open', 'high', 'low', 'close', 'volume']
    for col in numeric_cols:
        merged[col] = pd.to_numeric(merged[col], errors='coerce')
        
    merged = merged.sort_values('date').reset_index(drop=True)
    return merged

# --- Global State ---
df_full = load_data()
sources = sorted(df_full['source'].dropna().unique().tolist())
selected_sources = list(sources)
ma_periods = {'ma1': 20, 'ma2': 50, 'ma3': 200}
volatility_window = 30

fig = plt.figure(figsize=(24, 16))
fig.patch.set_facecolor(COLORS['bg'])

# --- Layout Definition ---
# Using GridSpec to match the requested layout
# 20 columns: 3 for sidebar, 17 for main area
gs = GridSpec(6, 20, figure=fig, wspace=0.4, hspace=1.2)

# Sidebar (Filters)
ax_sidebar = fig.add_subplot(gs[:, 0:3])
ax_sidebar.axis('off')

# Main Area Rows
# Row 1: KPIs (6 cards)
# We will create individual axes for these below
kpi_axes = []
for i in range(6):
    col_start = 3 + (i * 17 // 6)
    col_end = 3 + ((i + 1) * 17 // 6)
    kpi_axes.append(fig.add_subplot(gs[0, col_start:col_end]))

# Row 2: Candlestick (60%) + Histogram (40%)
ax_candle = fig.add_subplot(gs[1:3, 3:13]) # Takes 2 rows
ax_hist = fig.add_subplot(gs[1:3, 13:20])

# Row 3: Volume Bar (full width)
ax_vol = fig.add_subplot(gs[3, 3:20])

# Row 4: Daily Returns (50%) + Monthly Volume (50%)
ax_ret_line = fig.add_subplot(gs[4, 3:11])
ax_month_vol = fig.add_subplot(gs[4, 11:20])

# Row 5: Multi-line Close (60%) + Heatmap (40%)
ax_close_comp = fig.add_subplot(gs[5, 3:13])
ax_heatmap = fig.add_subplot(gs[5, 13:20])

chart_axes = [ax_candle, ax_hist, ax_vol, ax_ret_line, ax_month_vol, ax_close_comp, ax_heatmap]

# --- UI Widgets setup ---
# Filter components in sidebar area
ax_chk = fig.add_axes([0.02, 0.7, 0.1, 0.2])
ax_chk.set_facecolor(COLORS['bg'])
chk = CheckButtons(ax_chk, sources, [True]*len(sources))
for t in chk.labels: t.set_color(COLORS['font'])

ax_slider = fig.add_axes([0.02, 0.6, 0.1, 0.02])
slider_vol = Slider(ax_slider, 'Vol Window', 7, 90, valinit=30, valstep=1, color=COLORS['accent'])
slider_vol.label.set_color(COLORS['font_secondary'])
slider_vol.valtext.set_color(COLORS['font'])

ax_ma1 = fig.add_axes([0.06, 0.5, 0.06, 0.03])
ax_ma2 = fig.add_axes([0.06, 0.45, 0.06, 0.03])
ax_ma3 = fig.add_axes([0.06, 0.4, 0.06, 0.03])

for ax in [ax_ma1, ax_ma2, ax_ma3]: ax.set_facecolor(COLORS['card'])
tb_ma1 = TextBox(ax_ma1, 'MA 1 ', initial='20', color=COLORS['card'], textalignment="center")
tb_ma2 = TextBox(ax_ma2, 'MA 2 ', initial='50', color=COLORS['card'], textalignment="center")
tb_ma3 = TextBox(ax_ma3, 'MA 3 ', initial='200', color=COLORS['card'], textalignment="center")

for tb in [tb_ma1, tb_ma2, tb_ma3]:
    tb.label.set_color(COLORS['font_secondary'])
    tb.text_disp.set_color(COLORS['font'])

# Add sidebar title
fig.text(0.02, 0.95, "FILTERS", color=COLORS['font'], fontsize=14, fontweight='bold')


def style_ax(ax):
    ax.set_facecolor(COLORS['bg'])
    ax.tick_params(colors=COLORS['font_secondary'], labelcolor=COLORS['font_secondary'])
    for spine in ax.spines.values():
        spine.set_color(COLORS['grid'])
    ax.grid(color=COLORS['grid'], alpha=0.3)

# --- Drawing Functions ---

def draw_kpis(df):
    for ax in kpi_axes:
        ax.clear()
        ax.axis('off')
        # Draw background card
        rect = plt.Rectangle((0, 0), 1, 1, transform=ax.transAxes, facecolor=COLORS['card'], edgecolor=COLORS['grid'], lw=1)
        ax.add_patch(rect)

    if df.empty: return

    # Calculate KPIs
    # 1. Latest Close
    latest_close = df.groupby('source').last()['close'].mean() # average of latest across sources if multiple
    
    # 2. 52-Week High (last 252 days)
    # Approximation: last 252 rows per source
    high_52w = df.groupby('source').tail(252)['high'].max()
    
    # 3. 52-Week Low
    low_52w = df.groupby('source').tail(252)['low'].min()
    
    # 4. Daily Return %
    # using average close across sources for simplicity
    daily_close = df.groupby('date')['close'].mean()
    if len(daily_close) >= 2:
        c1, c0 = daily_close.iloc[-1], daily_close.iloc[-2]
        daily_ret = (c1 - c0) / c0 * 100
    else:
        daily_ret = 0.0

    # 5. Avg Volume 30D
    vol_30d = df.groupby('source').tail(30)['volume'].mean()
    
    # 6. Ann. Volatility
    pct_changes = daily_close.pct_change().tail(volatility_window)
    ann_vol = pct_changes.std() * np.sqrt(252) * 100

    kpi_data = [
        ("Latest Close", f"${latest_close:,.2f}", COLORS['font']),
        ("52-Week High", f"${high_52w:,.2f}", COLORS['font']),
        ("52-Week Low", f"${low_52w:,.2f}", COLORS['font']),
        ("Daily Return %", f"{daily_ret:+.2f}%", COLORS['bullish'] if daily_ret >= 0 else COLORS['bearish']),
        ("Avg Volume 30D", f"{vol_30d:,.0f}", COLORS['font']),
        ("Ann. Volatility", f"{ann_vol:.2f}%", COLORS['font'])
    ]

    for ax, (title, val, color) in zip(kpi_axes, kpi_data):
        ax.text(0.5, 0.7, title, color=COLORS['font_secondary'], ha='center', va='center', fontsize=10, transform=ax.transAxes)
        ax.text(0.5, 0.3, val, color=color, ha='center', va='center', fontsize=16, fontweight='bold', transform=ax.transAxes)

def draw_candlestick(df, ax):
    ax.clear()
    style_ax(ax)
    if df.empty: return
    
    # Aggregate to daily to draw candlestick if multiple sources are selected
    # For a true candlestick, usually you want 1 symbol, but we average here if needed
    daily = df.groupby('date').agg({'open':'mean', 'high':'max', 'low':'min', 'close':'mean'}).reset_index()
    
    up = daily[daily.close >= daily.open]
    down = daily[daily.close < daily.open]
    
    # We use width=0.6 days
    width = 0.6
    
    # Wicks
    ax.vlines(up.date, up.low, up.high, color=COLORS['bullish'], linewidth=1)
    ax.vlines(down.date, down.low, down.high, color=COLORS['bearish'], linewidth=1)
    
    # Bodies
    # matplotlib dates are numbers, but ax.bar accepts datetime objects
    # To set width correctly with datetimes, we might need timedelta
    width_td = pd.Timedelta(days=width)
    
    if not up.empty:
        ax.bar(up.date, up.close - up.open, width_td, bottom=up.open, color=COLORS['bullish'])
    if not down.empty:
        ax.bar(down.date, down.open - down.close, width_td, bottom=down.close, color=COLORS['bearish'])

    # MAs
    for key, color in [('ma1', COLORS['ma20']), ('ma2', COLORS['ma50']), ('ma3', COLORS['ma200'])]:
        period = ma_periods[key]
        if len(daily) >= period:
            ma = daily['close'].rolling(window=period).mean()
            ax.plot(daily.date, ma, color=color, label=f"MA{period}")
            
    ax.legend(facecolor=COLORS['card'], edgecolor=COLORS['grid'], labelcolor=COLORS['font'], loc='upper left', fontsize=9)
    ax.set_title("Price & Moving Averages", color=COLORS['font'])

def draw_histogram(df, ax):
    ax.clear()
    style_ax(ax)
    if df.empty: return
    
    daily = df.groupby('date')['close'].mean().pct_change() * 100
    daily = daily.dropna()
    
    if not daily.empty:
        ax.hist(daily, bins=50, color=COLORS['accent'], edgecolor=COLORS['bg'])
        mean_val = daily.mean()
        ax.axvline(mean_val, color=COLORS['bearish'], linestyle='--')
        ax.text(mean_val, ax.get_ylim()[1]*0.9, f"Mean: {mean_val:.2f}%", color=COLORS['bearish'])
        
    ax.set_title("Daily Returns Distribution", color=COLORS['font'])
    ax.set_xlabel("Return %")
    ax.set_ylabel("Frequency")

def draw_volume(df, ax):
    ax.clear()
    style_ax(ax)
    if df.empty: return
    
    daily = df.groupby('date').agg({'volume':'sum', 'close':'mean', 'open':'mean'}).reset_index()
    colors = [COLORS['bullish'] if c >= o else COLORS['bearish'] for c, o in zip(daily.close, daily.open)]
    width_td = pd.Timedelta(days=0.6)
    
    ax.bar(daily.date, daily.volume, width=width_td, color=colors)
    ax.set_title("Volume", color=COLORS['font'])
    
    # Share x axis with candlestick if possible, we'll let matplotlib handle it loosely

def draw_returns_line(df, ax):
    ax.clear()
    style_ax(ax)
    if df.empty: return
    
    daily = df.groupby('date')['close'].mean().pct_change() * 100
    ax.plot(daily.index, daily.values, color=COLORS['ma50'], linewidth=1)
    ax.axhline(0, color='grey', linestyle='--')
    ax.set_title("Daily Returns Over Time", color=COLORS['font'])

def draw_monthly_volume(df, ax):
    ax.clear()
    style_ax(ax)
    if df.empty: return
    
    df['month'] = df['date'].dt.month
    monthly = df.groupby(['month', 'source'])['volume'].mean().reset_index()
    
    sns.barplot(data=monthly, x='month', y='volume', hue='source', ax=ax, palette='deep')
    ax.legend(facecolor=COLORS['card'], edgecolor=COLORS['grid'], labelcolor=COLORS['font'], loc='upper right', fontsize=9)
    ax.set_title("Avg Monthly Volume by Source", color=COLORS['font'])

def draw_close_comp(df, ax):
    ax.clear()
    style_ax(ax)
    if df.empty: return
    
    sns.lineplot(data=df, x='date', y='close', hue='source', ax=ax, palette='deep')
    ax.legend(facecolor=COLORS['card'], edgecolor=COLORS['grid'], labelcolor=COLORS['font'], loc='upper left', fontsize=9)
    ax.set_title("Close Price Comparison", color=COLORS['font'])

def draw_heatmap(df, ax):
    ax.clear()
    style_ax(ax)
    if df.empty: return
    
    # Calculate monthly returns (average across sources for simplicity)
    daily = df.groupby('date')['close'].mean()
    monthly = daily.resample('ME').last()
    m_returns = monthly.pct_change() * 100
    
    # Prepare pivot table
    m_returns = m_returns.reset_index()
    m_returns['year'] = m_returns['date'].dt.year
    m_returns['month'] = m_returns['date'].dt.month
    pivot = m_returns.pivot(index='year', columns='month', values='close')
    
    if not pivot.empty:
        sns.heatmap(pivot, ax=ax, cmap='RdYlGn', annot=True, fmt=".1f", center=0, cbar=False,
                    linecolor=COLORS['bg'], linewidths=1)
        
    ax.set_title("Monthly Returns %", color=COLORS['font'])
    # Fix tick labels
    ax.tick_params(colors=COLORS['font_secondary'], labelcolor=COLORS['font_secondary'])
    ax.tick_params(axis='y', rotation=0)
    ax.tick_params(axis='x', rotation=0)

def update_dashboard():
    df_filtered = df_full[df_full['source'].isin(selected_sources)].copy()
    
    draw_kpis(df_filtered)
    draw_candlestick(df_filtered, ax_candle)
    draw_histogram(df_filtered, ax_hist)
    draw_volume(df_filtered, ax_vol)
    draw_returns_line(df_filtered, ax_ret_line)
    draw_monthly_volume(df_filtered, ax_month_vol)
    draw_close_comp(df_filtered, ax_close_comp)
    draw_heatmap(df_filtered, ax_heatmap)
    
    fig.canvas.draw_idle()

# --- Callback Functions ---
def on_chk_clicked(label):
    if label in selected_sources:
        selected_sources.remove(label)
    else:
        selected_sources.append(label)
    update_dashboard()

def on_vol_changed(val):
    global volatility_window
    volatility_window = int(val)
    update_dashboard()

def on_ma1_submit(text):
    try: ma_periods['ma1'] = int(text); update_dashboard()
    except ValueError: pass
def on_ma2_submit(text):
    try: ma_periods['ma2'] = int(text); update_dashboard()
    except ValueError: pass
def on_ma3_submit(text):
    try: ma_periods['ma3'] = int(text); update_dashboard()
    except ValueError: pass

chk.on_clicked(on_chk_clicked)
slider_vol.on_changed(on_vol_changed)
tb_ma1.on_submit(on_ma1_submit)
tb_ma2.on_submit(on_ma2_submit)
tb_ma3.on_submit(on_ma3_submit)

# Initial draw
update_dashboard()

# Save snapshot
out_dir = os.path.join(os.path.dirname(__file__), '..', 'output')
os.makedirs(out_dir, exist_ok=True)
plt.savefig(os.path.join(out_dir, 'dashboard_snapshot.png'), facecolor=fig.get_facecolor(), bbox_inches='tight')

# Display
print('Done')
