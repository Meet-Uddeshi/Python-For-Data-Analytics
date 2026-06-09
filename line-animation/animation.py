import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.lines import Line2D
import matplotlib.dates as mdates

# ── 1. Load all sources ───────────────────────────────────────────────────────

SOURCES = {
    "Bar Chart":      "gs_barchart.csv",
    "Investing.com":  "gs_investing_com.csv",
    "MarketWatch":    "gs_marketwatch.csv",
    "Master Dataset": "gs_master_dataset.csv",
    "NASDAQ":         "gs_nasdaq.csv",
    "Yahoo Finance":  "gs_yahoo_finance.csv",
}

PALETTE = ["#4C72B0", "#DD8452", "#55A868", "#C44E52", "#8172B3", "#E8C84A"]

frames: dict = {}

for label, path in SOURCES.items():
    try:
        df = pd.read_csv(path)
        # normalise column names to title-case
        df.columns = [c.strip().title() for c in df.columns]

        df["Date"]   = pd.to_datetime(df["Date"], utc=True).dt.tz_localize(None)
        df["Close"]  = pd.to_numeric(df["Close"].astype(str).str.replace(",", ""), errors="coerce")
        df["Volume"] = pd.to_numeric(df["Volume"].astype(str).str.replace(",", ""), errors="coerce")
        df = df.sort_values("Date").dropna(subset=["Close"]).reset_index(drop=True)
        df["DateNum"] = mdates.date2num(df["Date"])
        frames[label] = df[["Date", "DateNum", "Close", "Volume"]]
        print(f"✓ {label}: {len(df)} rows  {df['Date'].min().date()} → {df['Date'].max().date()}")
    except FileNotFoundError:
        print(f"✗ {label}: not found — skipping")

if not frames:
    raise SystemExit("No CSV files loaded.")

# ── 2. Global limits ──────────────────────────────────────────────────────────

all_nums  = pd.concat([df["DateNum"] for df in frames.values()])
all_close = pd.concat([df["Close"]   for df in frames.values()])
all_vol   = pd.concat([df["Volume"]  for df in frames.values()]).dropna()

x_min, x_max = all_nums.min(),  all_nums.max()
cp_min, cp_max = all_close.min(), all_close.max()
vp_min, vp_max = all_vol.min(),   all_vol.max()

cp_pad = (cp_max - cp_min) * 0.06
vp_pad = (vp_max - vp_min) * 0.06

# ── 3. Figure: two stacked panels ────────────────────────────────────────────

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 9), sharex=True,
                                gridspec_kw={"height_ratios": [2.5, 1]})
fig.patch.set_facecolor("#0f1117")
fig.subplots_adjust(hspace=0.08)

for ax in (ax1, ax2):
    ax.set_facecolor("#0f1117")
    for spine in ax.spines.values():
        spine.set_edgecolor("#2a2a3a")
    ax.tick_params(colors="#aaa", labelsize=9)
    ax.yaxis.label.set_color("#aaa")
    ax.grid(color="#1a1d2e", linewidth=0.5)

ax1.set_title("Goldman Sachs (GS) — Close Price & Volume by Source",
              color="white", fontsize=14, fontweight="bold", pad=12)
ax1.set_ylabel("Close Price (USD)", fontsize=10)
ax2.set_ylabel("Volume", fontsize=10)
ax2.set_xlabel("Date", fontsize=10)
ax2.xaxis.label.set_color("#aaa")

ax1.set_xlim(x_min, x_max);  ax1.set_ylim(cp_min - cp_pad, cp_max + cp_pad)
ax2.set_xlim(x_min, x_max);  ax2.set_ylim(0, vp_max + vp_pad)

ax2.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
ax2.xaxis.set_major_locator(mdates.YearLocator(4))
fig.autofmt_xdate(rotation=30)

# ── 4. Artists: line + dot per source for each panel ─────────────────────────

labels = list(frames.keys())
colors = PALETTE[: len(labels)]

close_lines, close_dots = {}, {}
vol_lines,   vol_dots   = {}, {}

for label, color in zip(labels, colors):
    (cl,) = ax1.plot([], [], lw=1.6, color=color, alpha=0.85)
    (cd,) = ax1.plot([], [], "o",  ms=5,  color=color, zorder=5)
    (vl,) = ax2.plot([], [], lw=1.2, color=color, alpha=0.75)
    (vd,) = ax2.plot([], [], "o",  ms=4,  color=color, zorder=5)
    close_lines[label] = cl;  close_dots[label] = cd
    vol_lines[label]   = vl;  vol_dots[label]   = vd

# legend (top panel)
legend_handles = [Line2D([0], [0], color=c, lw=2, label=l)
                  for l, c in zip(labels, colors)]
ax1.legend(handles=legend_handles, loc="upper left",
           framealpha=0.25, labelcolor="white",
           facecolor="#1a1d2e", edgecolor="#333", fontsize=9)

date_text = ax1.text(0.99, 0.05, "", transform=ax1.transAxes,
                     ha="right", va="bottom", fontsize=11,
                     color="#aaa", fontfamily="monospace", fontweight="bold")

# ── 5. Animation ──────────────────────────────────────────────────────────────

N_FRAMES  = 400
num_steps = [x_min + (x_max - x_min) * i / (N_FRAMES - 1) for i in range(N_FRAMES)]

def init():
    for label in labels:
        close_lines[label].set_data([], [])
        close_dots[label].set_data([], [])
        vol_lines[label].set_data([], [])
        vol_dots[label].set_data([], [])
    date_text.set_text("")
    return []

def update(i):
    cutoff = num_steps[i]
    for label, df in frames.items():
        mask = df["DateNum"] <= cutoff
        sub  = df[mask]
        xd   = sub["DateNum"].values

        # close panel
        yd = sub["Close"].values
        close_lines[label].set_data(xd, yd)
        if len(sub):
            close_dots[label].set_data([xd[-1]], [yd[-1]])

        # volume panel
        yv = sub["Volume"].dropna().values
        xv = sub.loc[sub["Volume"].notna(), "DateNum"].values
        vol_lines[label].set_data(xv, yv)
        if len(yv):
            vol_dots[label].set_data([xv[-1]], [yv[-1]])

    date_text.set_text(mdates.num2date(cutoff).strftime("%b %Y"))
    return []

ani = animation.FuncAnimation(
    fig, update, frames=N_FRAMES,
    init_func=init, interval=25,
    blit=False, repeat=False,
)

# Save options:
#   ani.save("gs_animation.mp4", writer="ffmpeg", dpi=150)
#   ani.save("gs_animation.gif", writer="pillow", fps=30)

plt.tight_layout()
plt.show()