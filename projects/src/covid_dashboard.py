import os
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
df_covid = pd.read_csv(os.path.join(base_dir, "covid.csv"))
df_grouped = pd.read_csv(os.path.join(base_dir, "covid_grouped.csv"))
df_death = pd.read_csv(os.path.join(base_dir, "coviddeath.csv"))

# --- Clean Data ---
df_grouped["Date"] = pd.to_datetime(df_grouped["Date"])
df_death["Number of COVID-19 Deaths"] = df_death["Number of COVID-19 Deaths"].fillna(0)

# --- Create Dashboard Layout ---
fig = plt.figure(figsize=(22, 14), constrained_layout=True)
fig.canvas.manager.set_window_title('COVID-19 Native Python Dashboard')
fig.suptitle("COVID-19 Global & US Analysis Dashboard", fontsize=28, fontweight='bold', color='#1A237E')

# GridSpec: 4 rows. Row 0: Filters context, Row 1: KPIs, Row 2: Charts, Row 3: Charts
gs = GridSpec(4, 2, figure=fig, height_ratios=[0.2, 0.6, 4, 4])

# --- Context ---
ax_filter = fig.add_subplot(gs[0, :])
ax_filter.axis('off')
filter_text = "Static Native View | All global regions and countries included | Dates: Max range"
ax_filter.text(0.01, 0.5, filter_text, va='center', ha='left', fontsize=12, color='#666666', style='italic')

# --- KPIs (Second Row) ---
ax_kpi = fig.add_subplot(gs[1, :])
ax_kpi.axis('off')

total_cases = df_covid["TotalCases"].sum()
total_deaths = df_covid["TotalDeaths"].sum()
total_recovered = df_covid["TotalRecovered"].sum()
us_deaths = df_death[df_death["Age Group"] != "All ages"]["Number of COVID-19 Deaths"].sum()

metrics = [
    {"label": "Global Cases", "value": f"{total_cases:,.0f}", "color": "#E3F2FD", "text_color": "#1565C0"},
    {"label": "Global Deaths", "value": f"{total_deaths:,.0f}", "color": "#FFEBEE", "text_color": "#C62828"},
    {"label": "Global Recovered", "value": f"{total_recovered:,.0f}", "color": "#E8F5E9", "text_color": "#2E7D32"},
    {"label": "US COVID Deaths", "value": f"{us_deaths:,.0f}", "color": "#FFF3E0", "text_color": "#EF6C00"}
]

box_width = 0.22
spacing = 0.03
start_x = (1 - (4 * box_width + 3 * spacing)) / 2

for i, metric in enumerate(metrics):
    x = start_x + i * (box_width + spacing)
    rect = patches.FancyBboxPatch((x, 0.1), box_width, 0.8, transform=ax_kpi.transAxes, 
                                  boxstyle="round,pad=0.02", facecolor=metric["color"], 
                                  edgecolor='#DDDDDD', linewidth=1)
    ax_kpi.add_patch(rect)
    
    ax_kpi.text(x + box_width/2, 0.6, metric["label"], ha='center', va='center', 
                fontsize=14, color='#555555', transform=ax_kpi.transAxes)
    ax_kpi.text(x + box_width/2, 0.35, metric["value"], ha='center', va='center', 
                fontsize=22, fontweight='bold', color=metric["text_color"], transform=ax_kpi.transAxes)

# --- V1: Top 15 Countries by Cases ---
ax1 = fig.add_subplot(gs[2, 0])
top_countries = df_covid.nlargest(15, 'TotalCases')
sns.barplot(data=top_countries, x='TotalCases', y='Country/Region', hue='Country/Region', ax=ax1, palette='Blues_r', legend=False)
ax1.set_title("Top 15 Countries by Total Cases", fontsize=16, fontweight='bold', pad=15)
ax1.set_xlabel("Total Cases", fontsize=12)
ax1.set_ylabel("")

# --- V2: Global Cumulative Trends ---
ax2 = fig.add_subplot(gs[2, 1])
df_trend = df_grouped.groupby("Date")[["Confirmed", "Recovered", "Deaths"]].sum().reset_index()
ax2.plot(df_trend["Date"], df_trend["Confirmed"], label="Confirmed Cases", color="#1976D2", linewidth=3)
ax2.plot(df_trend["Date"], df_trend["Recovered"], label="Recovered", color="#388E3C", linewidth=3)
ax2.plot(df_trend["Date"], df_trend["Deaths"], label="Deaths", color="#D32F2F", linewidth=3)
ax2.fill_between(df_trend["Date"], df_trend["Confirmed"], color="#1976D2", alpha=0.1)
ax2.set_title("Global Cumulative Trends Over Time", fontsize=16, fontweight='bold', pad=15)
ax2.set_xlabel("Date", fontsize=12)
ax2.set_ylabel("Cumulative Count", fontsize=12)
ax2.legend(loc='upper left', fontsize=12, frameon=True, shadow=True)

# --- V3: Testing Efficiency (Tests vs Cases per 1M) ---
ax3 = fig.add_subplot(gs[3, 0])
df_test = df_covid[(df_covid['Tests/1M pop'] > 0) & (df_covid['Tot Cases/1M pop'] > 0)].copy()
scatter = sns.scatterplot(data=df_test, x='Tests/1M pop', y='Tot Cases/1M pop', size='TotalDeaths', 
                hue='WHO Region', sizes=(30, 800), alpha=0.7, ax=ax3, palette="deep")
ax3.set_xscale('log')
ax3.set_yscale('log')
ax3.set_title("Testing Efficiency (Tests vs Cases per 1M pop)", fontsize=16, fontweight='bold', pad=15)
ax3.set_xlabel("Tests per 1M population (Log Scale)", fontsize=12)
ax3.set_ylabel("Total Cases per 1M population (Log Scale)", fontsize=12)
handles, labels = ax3.get_legend_handles_labels()
ax3.legend(handles, labels, bbox_to_anchor=(1.02, 1), loc='upper left', fontsize=10, borderaxespad=0., frameon=True)

# --- V4: US Deaths by Condition Group ---
ax4 = fig.add_subplot(gs[3, 1])
df_cond = df_death.groupby("Condition Group")["Number of COVID-19 Deaths"].sum().reset_index()
df_cond = df_cond.sort_values("Number of COVID-19 Deaths", ascending=False).head(10)
df_cond['Condition Group'] = df_cond['Condition Group'].str.wrap(30)
sns.barplot(data=df_cond, x='Number of COVID-19 Deaths', y='Condition Group', hue='Condition Group', ax=ax4, palette='Reds_r', legend=False)
ax4.set_title("Top 10 US Deaths by Condition Group", fontsize=16, fontweight='bold', pad=15)
ax4.set_xlabel("Number of COVID-19 Deaths", fontsize=12)
ax4.set_ylabel("")

# Render natively
plt.show()
