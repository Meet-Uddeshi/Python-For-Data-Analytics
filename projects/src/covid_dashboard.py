import os
import textwrap
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as patches
from matplotlib.gridspec import GridSpec

# --- Aesthetic Settings ---
sns.set_theme(style="whitegrid", rc={"axes.edgecolor": "#CCCCCC", "axes.linewidth": 1})
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['text.color'] = '#333333'
plt.rcParams['axes.labelcolor'] = '#555555'
plt.rcParams['xtick.color'] = '#555555'
plt.rcParams['ytick.color'] = '#555555'

# --- Load Data ---
current_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.join(os.path.dirname(current_dir), "data_covid_analysis")
df_covid   = pd.read_csv(os.path.join(base_dir, "covid.csv"))
df_grouped = pd.read_csv(os.path.join(base_dir, "covid_grouped.csv"))
df_death   = pd.read_csv(os.path.join(base_dir, "coviddeath.csv"))

# --- Clean Data ---
df_grouped["Date"] = pd.to_datetime(df_grouped["Date"])
df_death["Number of COVID-19 Deaths"] = df_death["Number of COVID-19 Deaths"].fillna(0)

# ─────────────────────────────────────────────────────────────
# Layout
# ─────────────────────────────────────────────────────────────
fig = plt.figure(figsize=(28, 20))
fig.canvas.manager.set_window_title('COVID-19 Dashboard')
fig.suptitle("COVID-19 Global & US Analysis Dashboard",
             fontsize=22, fontweight='bold', color='#1A237E', y=0.99)

gs = GridSpec(3, 2, figure=fig,
              height_ratios=[0.9, 4.5, 5.5],
              hspace=0.55, wspace=0.65)
fig.subplots_adjust(top=0.94, bottom=0.10, left=0.10, right=0.97)

# Subtitle
fig.text(0.07, 0.96,
         "Static View  |  All global regions & countries  |  Full date range",
         va='center', ha='left', fontsize=10, color='#777777', style='italic')

# ─────────────────────────────────────────────────────────────
# KPI Row
# ─────────────────────────────────────────────────────────────
ax_kpi = fig.add_subplot(gs[0, :])
ax_kpi.axis('off')

total_cases     = df_covid["TotalCases"].sum()
total_deaths    = df_covid["TotalDeaths"].sum()
total_recovered = df_covid["TotalRecovered"].sum()
us_deaths = df_death[df_death["Age Group"] != "All ages"]["Number of COVID-19 Deaths"].sum()

metrics = [
    {"label": "Global Cases",     "value": f"{total_cases:,.0f}",     "bg": "#E3F2FD", "fg": "#1565C0"},
    {"label": "Global Deaths",    "value": f"{total_deaths:,.0f}",    "bg": "#FFEBEE", "fg": "#C62828"},
    {"label": "Global Recovered", "value": f"{total_recovered:,.0f}", "bg": "#E8F5E9", "fg": "#2E7D32"},
    {"label": "US COVID Deaths",  "value": f"{us_deaths:,.0f}",       "bg": "#FFF3E0", "fg": "#EF6C00"},
]

bw = 0.245
sp = 0.005
sx = (1 - (4 * bw + 3 * sp)) / 2

for i, m in enumerate(metrics):
    x = sx + i * (bw + sp)
    ax_kpi.add_patch(patches.FancyBboxPatch(
        (x, 0.02), bw, 0.96,
        transform=ax_kpi.transAxes,
        boxstyle="round,pad=0.02",
        facecolor=m["bg"], edgecolor='#CCCCCC', linewidth=1.2
    ))
    ax_kpi.text(x + bw/2, 0.75, m["label"],
                ha='center', va='center', fontsize=11,
                color='#555555', transform=ax_kpi.transAxes)
    ax_kpi.text(x + bw/2, 0.25, m["value"],
                ha='center', va='center', fontsize=17,
                fontweight='bold', color=m["fg"],
                transform=ax_kpi.transAxes)

# ─────────────────────────────────────────────────────────────
# Top Charts — Row 1
# ─────────────────────────────────────────────────────────────

# V1: Top 15 Countries by Total Cases
ax1 = fig.add_subplot(gs[1, 0])
top_countries = df_covid.nlargest(15, 'TotalCases')
sns.barplot(data=top_countries, x='TotalCases', y='Country/Region',
            hue='Country/Region', ax=ax1, palette='Blues_r', legend=False)
ax1.set_title("Top 15 Countries by Total Cases", fontsize=14, fontweight='bold', pad=10)
ax1.set_xlabel("Total Cases", fontsize=11)
ax1.set_ylabel("")

# ── FIX 1: wrap long country names so they never overlap ──
wrapped = [textwrap.fill(lbl.get_text(), width=18) for lbl in ax1.get_yticklabels()]
ax1.set_yticks(ax1.get_yticks())
ax1.set_yticklabels(wrapped, fontsize=9.5)
ax1.tick_params(axis='x', labelsize=10)
ax1.yaxis.set_tick_params(pad=4)

# V2: Global Cumulative Trends
ax2 = fig.add_subplot(gs[1, 1])
df_trend = df_grouped.groupby("Date")[["Confirmed","Recovered","Deaths"]].sum().reset_index()
ax2.plot(df_trend["Date"], df_trend["Confirmed"], label="Confirmed", color="#1976D2", linewidth=2.5)
ax2.plot(df_trend["Date"], df_trend["Recovered"], label="Recovered", color="#388E3C", linewidth=2.5)
ax2.plot(df_trend["Date"], df_trend["Deaths"],    label="Deaths",    color="#D32F2F", linewidth=2.5)
ax2.fill_between(df_trend["Date"], df_trend["Confirmed"], color="#1976D2", alpha=0.08)
ax2.set_title("Global Cumulative Trends Over Time", fontsize=14, fontweight='bold', pad=10)
ax2.set_xlabel("Date", fontsize=11)
ax2.set_ylabel("Cumulative Count", fontsize=11)
ax2.tick_params(axis='both', labelsize=9)
ax2.legend(loc='upper left', fontsize=10, frameon=True)

# ─────────────────────────────────────────────────────────────
# Bottom Charts — Row 2
# ─────────────────────────────────────────────────────────────

# V3: Testing Efficiency scatter
ax3 = fig.add_subplot(gs[2, 0])
df_test = df_covid[(df_covid['Tests/1M pop'] > 0) & (df_covid['Tot Cases/1M pop'] > 0)].copy()
sns.scatterplot(data=df_test, x='Tests/1M pop', y='Tot Cases/1M pop',
                size='TotalDeaths', hue='WHO Region',
                sizes=(30, 500), alpha=0.75, ax=ax3, palette="deep")
ax3.set_xscale('log')
ax3.set_yscale('log')
ax3.set_title("Testing Efficiency (Tests vs Cases per 1M pop)", fontsize=13, fontweight='bold', pad=10)
ax3.set_xlabel("Tests per 1M population (Log Scale)", fontsize=10)
ax3.set_ylabel("Total Cases per 1M pop (Log Scale)", fontsize=10)
ax3.tick_params(axis='both', labelsize=9)
ax3.tick_params(axis='x', pad=6)        # extra gap between x-ticks and label
ax3.tick_params(axis='y', pad=4)        # ensure y-tick labels aren't clipped
ax3.set_ylabel("Total Cases per 1M pop (Log Scale)", fontsize=10, labelpad=8)

# ── FIX 2: single combined legend placed cleanly outside right of plot ──
handles, labels = ax3.get_legend_handles_labels()
who_regions = list(df_test['WHO Region'].unique())

reg_h = [h for h, l in zip(handles, labels) if l in who_regions]
reg_l = [l for l in labels if l in who_regions]
siz_h = [h for h, l in zip(handles, labels) if l not in who_regions]
siz_l = [l for l in labels if l not in who_regions]

# Uniform small size for all size-legend markers
for h in siz_h:
    if hasattr(h, 'set_sizes'):
        h.set_sizes([40])

# Remove the default auto-generated legend
ax3.legend_.remove()

# Shrink ax3 width so the legend panel on the right never overlaps the plot
ax3_pos = ax3.get_position()
ax3.set_position([ax3_pos.x0 + 0.02,   # shift right → Y-axis labels fully visible
                  ax3_pos.y0 + 0.04,   # shift up → X-axis label fully visible
                  ax3_pos.width * 0.70,
                  ax3_pos.height])

# Build one combined handle/label list:
#   - blank title-style entry for "WHO Region" section
#   - all WHO region handles
#   - blank spacer
#   - blank title-style entry for "Total Deaths" section
#   - all size handles
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

def blank_handle():
    """Invisible handle used as a section header row."""
    return Patch(color='none')

combined_h = (
    [blank_handle()] + reg_h +
    [blank_handle(), blank_handle()] + siz_h
)
combined_l = (
    ['── WHO Region ──'] + reg_l +
    ['', '── Total Deaths (size) ──'] + siz_l
)

leg = ax3.legend(
    combined_h, combined_l,
    bbox_to_anchor=(1.02, 1.0), loc='upper left',
    fontsize=8.5, frameon=True,
    edgecolor='#BBBBBB', fancybox=True,
    handlelength=1.2, handleheight=1.0,
    borderpad=0.8, labelspacing=0.45,
)

# Bold the two section-header rows
for text in leg.get_texts():
    if text.get_text().startswith('──'):
        text.set_fontweight('bold')
        text.set_color('#333333')

# V4: US Deaths by Condition Group
ax4 = fig.add_subplot(gs[2, 1])
df_cond = df_death.groupby("Condition Group")["Number of COVID-19 Deaths"].sum().reset_index()
df_cond = df_cond.sort_values("Number of COVID-19 Deaths", ascending=False).head(10)

# ── FIX 3: wrap condition group labels so they don't overlap ──
df_cond['Condition Group'] = df_cond['Condition Group'].apply(
    lambda x: '\n'.join(textwrap.wrap(str(x), width=22))
)

sns.barplot(data=df_cond, x='Number of COVID-19 Deaths', y='Condition Group',
            hue='Condition Group', ax=ax4, palette='Reds_r', legend=False)
ax4.set_title("Top 10 US Deaths by Condition Group", fontsize=14, fontweight='bold', pad=10)
ax4.set_xlabel("Number of COVID-19 Deaths", fontsize=11)
ax4.set_ylabel("")

# Increase left margin so wrapped labels have room
ax4.tick_params(axis='y', labelsize=8.5, pad=4)
ax4.tick_params(axis='x', labelsize=9)
ax4.yaxis.set_tick_params(length=0)          # hide tick marks — saves space
ax4.set_yticks(ax4.get_yticks())
ax4.set_yticklabels(ax4.get_yticklabels(), linespacing=0.85)

# Extra left margin for ax4 so wrapped text isn't clipped
ax4_pos = ax4.get_position()
ax4.set_position([ax4_pos.x0 + 0.04, ax4_pos.y0,
                  ax4_pos.width - 0.04, ax4_pos.height])

plt.savefig(os.path.join(current_dir, "covid_dashboard_fixed.png"), dpi=150, bbox_inches='tight')
plt.show()