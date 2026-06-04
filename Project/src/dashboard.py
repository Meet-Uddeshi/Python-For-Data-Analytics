import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.gridspec import GridSpec
from matplotlib.patches import FancyBboxPatch
from matplotlib.colors import LinearSegmentedColormap
import datetime
import warnings
warnings.filterwarnings('ignore')

# --- Theme Constants ---
COLORS = {
    "bg": "#FFFFFF",
    "card": "#F8F9FA",
    "text": "#212529",
    "secondary_text": "#495057",
    "grid": "#DEE2E6",
    "accent": "#B5924C",
    "positive": "#198754",
    "negative": "#DC3545",
    "neutral": "#6C757D"
}

# Apply base styles
plt.rcParams.update({
    'figure.facecolor': COLORS['bg'],
    'axes.facecolor': COLORS['bg'],
    'axes.edgecolor': COLORS['grid'],
    'axes.labelcolor': COLORS['secondary_text'],
    'text.color': COLORS['text'],
    'xtick.color': COLORS['secondary_text'],
    'ytick.color': COLORS['secondary_text'],
    'grid.color': COLORS['grid'],
    'grid.alpha': 0.5,
    'axes.titlecolor': COLORS['text'],
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

# --- Data Preprocessing ---
def get_daily_data():
    df_full = load_data()
    # Aggregate to daily average across sources
    df = df_full.groupby('date').agg({'open':'mean', 'high':'mean', 'low':'mean', 'close':'mean', 'volume':'mean'}).reset_index()
    df = df.sort_values('date').dropna(subset=['close'])
    return df

# --- Drawing Functions ---
def draw_kpi(ax, title, value_str, color):
    ax.axis('off')
    # Draw rounded background card
    bbox = FancyBboxPatch((0, 0), 1, 1, boxstyle="round,pad=0.03", facecolor=COLORS['card'], edgecolor=COLORS['grid'], transform=ax.transAxes, lw=1)
    ax.add_patch(bbox)
    
    ax.text(0.5, 0.65, title, ha='center', va='center', fontsize=12, color=COLORS['secondary_text'], transform=ax.transAxes)
    ax.text(0.5, 0.35, value_str, ha='center', va='center', fontsize=18, fontweight='bold', color=color, transform=ax.transAxes)

def draw_price_trend(df, ax):
    ax.plot(df['date'], df['close'], color=COLORS['text'], lw=1.5, label='Close Price')
    
    if len(df) >= 50:
        ma50 = df['close'].rolling(50).mean()
        ax.plot(df['date'], ma50, color=COLORS['accent'], lw=1.2, label='50-Day MA')
    if len(df) >= 200:
        ma200 = df['close'].rolling(200).mean()
        ax.plot(df['date'], ma200, color=COLORS['positive'], lw=1.2, label='200-Day MA')
    
    ax.set_title("Price Trend", color=COLORS['text'], fontweight='bold', fontsize=14, loc='left', pad=10)
    ax.grid(color=COLORS['grid'], alpha=0.5, linestyle='--')
    ax.legend(loc='upper left', frameon=True, facecolor=COLORS['card'], edgecolor=COLORS['grid'], labelcolor=COLORS['text'])
    ax.tick_params(axis='x', rotation=0, labelcolor=COLORS['secondary_text'])
    for spine in ax.spines.values():
        spine.set_color(COLORS['grid'])

def draw_distribution(df, ax):
    daily_returns = df['close'].pct_change().dropna() * 100
    sns.histplot(daily_returns, kde=True, ax=ax, color=COLORS['accent'], edgecolor=COLORS['bg'], line_kws={'lw': 2})
    mean_ret = daily_returns.mean()
    ax.axvline(mean_ret, color=COLORS['negative'], linestyle='--', lw=1.5)
    ax.text(mean_ret, ax.get_ylim()[1]*0.9, f" Mean: {mean_ret:.2f}%", color=COLORS['negative'], va='center', fontsize=10, fontweight='bold')
    
    ax.set_title("Daily Return Distribution", color=COLORS['text'], fontweight='bold', fontsize=14, loc='left', pad=10)
    ax.set_xlabel("Daily Return (%)", color=COLORS['secondary_text'])
    ax.set_ylabel("Frequency", color=COLORS['secondary_text'])
    ax.grid(color=COLORS['grid'], alpha=0.5, linestyle='--')
    for spine in ax.spines.values():
        spine.set_color(COLORS['grid'])

def draw_rolling_vol(df, ax):
    daily_returns = df['close'].pct_change()
    rolling_vol = daily_returns.rolling(window=30).std() * np.sqrt(252) * 100
    ax.plot(df['date'], rolling_vol, color=COLORS['text'], lw=1.5)
    
    ax.set_title("30-Day Rolling Volatility", color=COLORS['text'], fontweight='bold', fontsize=14, loc='left', pad=10)
    ax.set_ylabel("Annualized Vol (%)", color=COLORS['secondary_text'])
    ax.set_xlabel("")
    ax.grid(color=COLORS['grid'], alpha=0.5, linestyle='--')
    for spine in ax.spines.values():
        spine.set_color(COLORS['grid'])

def draw_heatmap(df, ax):
    # Calculate monthly returns
    daily = df.set_index('date')['close']
    monthly = daily.resample('ME').last()
    m_returns = monthly.pct_change() * 100
    
    m_returns = m_returns.reset_index()
    m_returns['year'] = m_returns['date'].dt.year
    m_returns['month'] = m_returns['date'].dt.month
    
    # Filter latest 10 years
    latest_year = m_returns['year'].max()
    m_returns = m_returns[m_returns['year'] > latest_year - 10]
    
    pivot = m_returns.pivot(index='year', columns='month', values='close')
    
    # Logic for dynamic annotation
    num_years = len(pivot)
    if num_years <= 10:
        annot = True
        if num_years <= 5:
            annot_size = 9
        else:
            annot_size = 8
    else:
        annot = False
        annot_size = 6
        
    cmap = LinearSegmentedColormap.from_list('custom_cmap', [COLORS['negative'], COLORS['bg'], COLORS['positive']])
    
    if not pivot.empty:
        sns.heatmap(pivot, ax=ax, cmap=cmap, annot=annot, fmt=".1f", center=0, cbar=False,
                    linecolor=COLORS['bg'], linewidths=2, annot_kws={"size": annot_size})
        
    ax.set_title("Monthly Returns %", color=COLORS['text'], fontweight='bold', fontsize=14, loc='left', pad=10)
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.tick_params(axis='y', rotation=0, labelcolor=COLORS['secondary_text'], labelsize=10)
    
    # Replace month numbers with names
    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # Adjust for cases where not all months are present
    valid_months = [month_names[int(m)-1] for m in pivot.columns]
    ax.set_xticklabels(valid_months, rotation=0, color=COLORS['secondary_text'], fontsize=10)
    
    for spine in ax.spines.values():
        spine.set_color(COLORS['grid'])
        spine.set_visible(True)

# --- Main Dashboard Execution ---
def create_dashboard():
    df = get_daily_data()
    if df.empty:
        print("Error: No data available to generate dashboard.")
        return

    # Calculate KPIs
    current_price = df['close'].iloc[-1]
    prev_price = df['close'].iloc[-2] if len(df) > 1 else current_price
    daily_ret = (current_price / prev_price - 1) * 100
    
    latest_date = df['date'].max()
    year_data = df[df['date'].dt.year == latest_date.year]
    ytd_start_price = year_data['close'].iloc[0] if not year_data.empty else current_price
    ytd_ret = (current_price / ytd_start_price - 1) * 100
    
    total_days = (df['date'].max() - df['date'].min()).days
    if total_days > 0:
        total_years = total_days / 365.25
        total_ret = current_price / df['close'].iloc[0]
        ann_ret = (total_ret ** (1 / total_years) - 1) * 100 if total_years > 0 else 0
    else:
        ann_ret = 0.0

    daily_returns = df['close'].pct_change().dropna()
    ann_vol = daily_returns.std() * np.sqrt(252) * 100 if len(daily_returns) > 0 else 0
    
    risk_free_rate = 0.0
    sharpe = ((ann_ret / 100) - risk_free_rate) / (ann_vol / 100) if ann_vol > 0 else 0

    kpi_data = [
        ("Current Price", f"${current_price:,.2f}", COLORS['text']),
        ("Daily Return %", f"{daily_ret:+.2f}%", COLORS['positive'] if daily_ret >= 0 else COLORS['negative']),
        ("YTD Return %", f"{ytd_ret:+.2f}%", COLORS['positive'] if ytd_ret >= 0 else COLORS['negative']),
        ("Annualized Return", f"{ann_ret:+.2f}%", COLORS['positive'] if ann_ret >= 0 else COLORS['negative']),
        ("Annualized Volatility", f"{ann_vol:.2f}%", COLORS['text']),
        ("Sharpe Ratio", f"{sharpe:.2f}", COLORS['positive'] if sharpe >= 1 else (COLORS['negative'] if sharpe < 0 else COLORS['text']))
    ]

    # Setup Layout
    fig = plt.figure(figsize=(18, 14))
    
    # Title and Timestamp
    fig.suptitle('Goldman Sachs Equity Analytics Dashboard', fontsize=22, fontweight='bold', color=COLORS['text'], y=0.97)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    fig.text(0.5, 0.94, f"Last Updated: {timestamp} | Data Analyst Portfolio", ha='center', fontsize=12, color=COLORS['secondary_text'])

    gs = GridSpec(4, 4, figure=fig, height_ratios=[1.0, 1.5, 1.2, 2.0], hspace=0.45, wspace=0.30)
    fig.subplots_adjust(left=0.05, right=0.95, top=0.90, bottom=0.05)
    
    # Row 1: KPIs
    gs_kpi = gs[0, :].subgridspec(1, 6, wspace=0.15)
    kpi_axes = [fig.add_subplot(gs_kpi[0, i]) for i in range(6)]
    for ax, (title, val, color) in zip(kpi_axes, kpi_data):
        draw_kpi(ax, title, val, color)

    # Row 2: Price Trend
    ax_price = fig.add_subplot(gs[1, :])
    draw_price_trend(df, ax_price)
    
    # Row 3: Risk & Return
    ax_hist = fig.add_subplot(gs[2, 0:2])
    ax_vol = fig.add_subplot(gs[2, 2:4])
    draw_distribution(df, ax_hist)
    draw_rolling_vol(df, ax_vol)
    
    # Row 4: Monthly Heatmap
    ax_heatmap = fig.add_subplot(gs[3, :])
    draw_heatmap(df, ax_heatmap)
    
    # Save snapshot
    out_dir = os.path.join(os.path.dirname(__file__), '..', 'output')
    os.makedirs(out_dir, exist_ok=True)
    plt.savefig(os.path.join(out_dir, 'dashboard_portfolio_snapshot.png'), facecolor=fig.get_facecolor(), bbox_inches='tight', dpi=150)
    
    # Display
    plt.show()

if __name__ == "__main__":
    create_dashboard()
