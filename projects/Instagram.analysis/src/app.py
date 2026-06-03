import os
import sys
import numpy as np
import pandas as pd

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


# ═══════════════════════════════════════════════════════════════
# COLOUR PALETTE (Classic Professional Light Theme)
# ═══════════════════════════════════════════════════════════════
APP_BG      = '#F8FAFC'       # Slate 50
CARD_BG     = '#FFFFFF'
PRIMARY     = '#4F46E5'       # Indigo
ENGAGEMENT  = '#EC4899'       # Pink
REACH       = '#06B6D4'       # Cyan
POSITIVE    = '#10B981'       # Emerald
NEGATIVE    = '#EF4444'       # Red
TEXT_PRI    = '#0F172A'       # Slate 900
TEXT_SEC    = '#64748B'       # Slate 500
GRID_CLR    = '#E2E8F0'       # Slate 200

SOURCE_COLORS = {
    'From Home':     PRIMARY,
    'From Hashtags': ENGAGEMENT,
    'From Explore':  REACH,
    'From Other':    TEXT_SEC,
}

ENGAGE_COLORS = {
    'Likes':    PRIMARY,
    'Comments': ENGAGEMENT,
    'Shares':   REACH,
    'Saves':    POSITIVE,
}

KPI_ACCENTS = [PRIMARY, ENGAGEMENT, REACH, POSITIVE, TEXT_SEC]

COLUMNS = [
    'Impressions', 'From Home', 'From Hashtags', 'From Explore',
    'From Other', 'Saves', 'Comments', 'Shares', 'Likes',
    'Profile Visits', 'Follows', 'Caption', 'Hashtags',
]

FONT = 'Segoe UI'

# ═══════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════
def hex_to_rgba(hex_color, alpha=1.0):
    h = hex_color.lstrip('#')
    return (int(h[:2], 16) / 255, int(h[2:4], 16) / 255, int(h[4:6], 16) / 255, alpha)

def format_number(n):
    if abs(n) >= 1_000_000: return f'{n / 1_000_000:.1f}M'
    if abs(n) >= 1_000: return f'{n / 1_000:.1f}K'
    return f'{n:,.0f}'

# ═══════════════════════════════════════════════════════════════
# MAIN DASHBOARD
# ═══════════════════════════════════════════════════════════════
class InstagramDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Instagram Post Performance Dashboard")
        self.root.configure(bg=APP_BG)
        self.root.state('zoomed') # Maximize

        self._load_default_data()
        self._apply_global_style()
        self._build_ui()
        self._draw_all()

    def _apply_global_style(self):
        sns.set_style('whitegrid', {
            'axes.facecolor':   CARD_BG,
            'figure.facecolor': CARD_BG,
            'grid.color':       GRID_CLR,
        })
        plt.rcParams.update({
            'font.family':     FONT,
            'font.size':       10,
            'text.color':      TEXT_PRI,
            'axes.labelcolor': TEXT_SEC,
            'axes.labelsize':  10,
            'axes.edgecolor':  GRID_CLR,
            'axes.linewidth':  0.8,
            'xtick.color':     TEXT_SEC,
            'ytick.color':     TEXT_SEC,
            'grid.linewidth':  0.6,
        })

    def _load_default_data(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(base_dir, '..', 'data', 'Instagram data.csv')
        if not os.path.isfile(csv_path):
            raise FileNotFoundError("Default dataset not found.")
        self._parse_csv(csv_path)

    def _parse_csv(self, filepath):
        try:
            df = pd.read_csv(filepath, encoding='latin-1', on_bad_lines='skip')
        except TypeError:
            df = pd.read_csv(filepath, encoding='latin-1', error_bad_lines=False)

        first_col = str(df.columns[0]).strip().replace(',', '').replace('.', '').replace('-', '')
        if first_col.isdigit():
            try:
                df = pd.read_csv(filepath, header=None, names=COLUMNS, encoding='latin-1', on_bad_lines='skip')
            except TypeError:
                df = pd.read_csv(filepath, header=None, names=COLUMNS, encoding='latin-1', error_bad_lines=False)
        else:
            if len(df.columns) >= len(COLUMNS):
                df.columns = COLUMNS[: len(df.columns)]

        for col in COLUMNS[:11]:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)

        df['Engagement Total'] = df['Likes'] + df['Comments'] + df['Shares'] + df['Saves']
        df['Engagement Rate'] = np.where(df['Impressions'] > 0, df['Engagement Total'] / df['Impressions'] * 100, 0.0)
        df['Save Rate'] = np.where(df['Impressions'] > 0, df['Saves'] / df['Impressions'] * 100, 0.0)
        df['Profile Visit Rate'] = np.where(df['Impressions'] > 0, df['Profile Visits'] / df['Impressions'] * 100, 0.0)
        df['Post Index'] = np.arange(1, len(df) + 1)
        self.df = df

    def _get_filtered(self):
        df = self.df.copy()
        
        try: min_imp = int(self.min_imp_var.get())
        except: min_imp = 0
        df = df[df['Impressions'] >= min_imp]
        
        try: min_fol = int(self.min_fol_var.get())
        except: min_fol = 0
        df = df[df['Follows'] >= min_fol]

        bkt = self.eng_var.get()
        if bkt == 'Low (<2%)': df = df[df['Engagement Rate'] < 2]
        elif bkt == 'Mid (2-5%)': df = df[(df['Engagement Rate'] >= 2) & (df['Engagement Rate'] <= 5)]
        elif bkt == 'High (>5%)': df = df[df['Engagement Rate'] > 5]

        # Apply moving average to smooth line charts
        df['Profile Visits Smoothed'] = df['Profile Visits'].rolling(window=5, min_periods=1).mean()
        df['Follows Smoothed'] = df['Follows'].rolling(window=5, min_periods=1).mean()

        return df.reset_index(drop=True)

    def _build_ui(self):
        # Header + Filters
        top_frame = tk.Frame(self.root, bg=APP_BG)
        top_frame.pack(fill=tk.X, padx=20, pady=10)

        lbl_title = tk.Label(top_frame, text="Instagram Dashboard", font=(FONT, 18, "bold"), bg=APP_BG, fg=TEXT_PRI)
        lbl_title.pack(side=tk.LEFT, padx=(0, 30))

        # Filters
        f_frame = tk.Frame(top_frame, bg=APP_BG)
        f_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Impression filter
        tk.Label(f_frame, text="Min Impressions:", bg=APP_BG, fg=TEXT_SEC).grid(row=0, column=0, padx=5, sticky="e")
        self.min_imp_var = tk.StringVar(value="0")
        imp_entry = ttk.Entry(f_frame, textvariable=self.min_imp_var, width=10)
        imp_entry.grid(row=0, column=1, padx=5)
        imp_entry.bind("<Return>", lambda e: self._draw_all())

        # Follows filter
        tk.Label(f_frame, text="Min Follows:", bg=APP_BG, fg=TEXT_SEC).grid(row=0, column=2, padx=5, sticky="e")
        self.min_fol_var = tk.StringVar(value="0")
        fol_entry = ttk.Entry(f_frame, textvariable=self.min_fol_var, width=10)
        fol_entry.grid(row=0, column=3, padx=5)
        fol_entry.bind("<Return>", lambda e: self._draw_all())

        # Engagement dropdown
        tk.Label(f_frame, text="Engagement:", bg=APP_BG, fg=TEXT_SEC).grid(row=0, column=4, padx=5, sticky="e")
        self.eng_var = tk.StringVar(value="All")
        eng_cb = ttk.Combobox(f_frame, textvariable=self.eng_var, values=["All", "Low (<2%)", "Mid (2-5%)", "High (>5%)"], state="readonly", width=12)
        eng_cb.grid(row=0, column=5, padx=5)
        eng_cb.bind("<<ComboboxSelected>>", lambda e: self._draw_all())

        # Traffic Source dropdown
        tk.Label(f_frame, text="Traffic Source:", bg=APP_BG, fg=TEXT_SEC).grid(row=0, column=6, padx=5, sticky="e")
        self.src_var = tk.StringVar(value="All")
        src_cb = ttk.Combobox(f_frame, textvariable=self.src_var, values=["All", "Home", "Hashtags", "Explore", "Other"], state="readonly", width=12)
        src_cb.grid(row=0, column=7, padx=5)
        src_cb.bind("<<ComboboxSelected>>", lambda e: self._draw_all())

        btn_apply = ttk.Button(f_frame, text="Apply Filters", command=self._draw_all)
        btn_apply.grid(row=0, column=8, padx=15)

        # Export Button
        btn_export = ttk.Button(top_frame, text="Export Output", command=self._on_export)
        btn_export.pack(side=tk.RIGHT, padx=(10, 0))

        # Upload Button
        btn_upload = ttk.Button(top_frame, text="Upload CSV", command=self._on_upload)
        btn_upload.pack(side=tk.RIGHT)

        # KPIs Frame
        self.kpi_frame = tk.Frame(self.root, bg=APP_BG)
        self.kpi_frame.pack(fill=tk.X, padx=20, pady=(0, 10))
        self.kpi_labels = []
        for i in range(5):
            frm = tk.Frame(self.kpi_frame, bg=CARD_BG, highlightbackground=KPI_ACCENTS[i], highlightthickness=2)
            frm.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
            val_lbl = tk.Label(frm, text="-", font=(FONT, 16, "bold"), bg=CARD_BG, fg=TEXT_PRI)
            val_lbl.pack(pady=(10, 0))
            name_lbl = tk.Label(frm, text="-", font=(FONT, 9), bg=CARD_BG, fg=TEXT_SEC)
            name_lbl.pack(pady=(0, 10))
            self.kpi_labels.append((val_lbl, name_lbl))

        # Matplotlib Figure
        self.fig = plt.Figure(figsize=(16, 8), facecolor=APP_BG, tight_layout=True)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))

        # GridSpec layout: 2 Rows, 4 Columns
        gs = self.fig.add_gridspec(2, 4)
        self.ax_stacked   = self.fig.add_subplot(gs[0, 0])
        self.ax_donut     = self.fig.add_subplot(gs[0, 1])
        self.ax_scatter   = self.fig.add_subplot(gs[0, 2])
        self.ax_funnel    = self.fig.add_subplot(gs[0, 3])
        self.ax_clustered = self.fig.add_subplot(gs[1, 0])
        self.ax_line      = self.fig.add_subplot(gs[1, 1:3])
        self.ax_hbar      = self.fig.add_subplot(gs[1, 3])

        self.chart_axes = [self.ax_stacked, self.ax_donut, self.ax_scatter, self.ax_funnel, self.ax_clustered, self.ax_line, self.ax_hbar]

    def _on_upload(self):
        filepath = filedialog.askopenfilename(filetypes=[('CSV files', '*.csv'), ('All files', '*.*')])
        if filepath:
            self._parse_csv(filepath)
            self._draw_all()

    def _on_export(self):
        import datetime
        from tkinter import messagebox
        output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'projects','Instagram.analysis','output')
        output_dir = os.path.abspath(output_dir)
        os.makedirs(output_dir, exist_ok=True)
        
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Save filtered data
        df = self._get_filtered()
        csv_path = os.path.join(output_dir, f"filtered_data_{timestamp}.csv")
        df.to_csv(csv_path, index=False)
        
        # Save figure
        fig_path = os.path.join(output_dir, f"dashboard_{timestamp}.png")
        self.fig.savefig(fig_path, dpi=300, facecolor=self.fig.get_facecolor(), bbox_inches='tight')
        
        messagebox.showinfo("Export Successful", f"Results stored in:\n{output_dir}")

    def _update_kpis(self, df):
        metrics = [
            ("Total Impressions", format_number(df['Impressions'].sum())),
            ("Avg Engagement Rate", f"{df['Engagement Rate'].mean():.2f}%"),
            ("Total Follows", format_number(df['Follows'].sum())),
            ("Avg Save Rate", f"{df['Save Rate'].mean():.2f}%"),
            ("Avg Profile Visit Rate", f"{df['Profile Visit Rate'].mean():.2f}%"),
        ]
        for i, (name, val) in enumerate(metrics):
            self.kpi_labels[i][0].config(text=val)
            self.kpi_labels[i][1].config(text=name)

    @staticmethod
    def _style_ax(ax, title, xlabel='', ylabel=''):
        ax.set_facecolor(CARD_BG)
        ax.set_title(title, fontsize=11, fontweight='bold', color=TEXT_PRI, pad=5, loc='left')
        if xlabel: ax.set_xlabel(xlabel, fontsize=9, color=TEXT_SEC)
        if ylabel: ax.set_ylabel(ylabel, fontsize=9, color=TEXT_SEC)
        ax.tick_params(colors=TEXT_SEC, labelsize=8)

    def _draw_all(self):
        df = self._get_filtered()
        if df.empty:
            for ax in self.chart_axes: ax.clear()
            self.canvas.draw()
            return

        self._update_kpis(df)
        
        self._draw_stacked(df)
        self._draw_donut(df)
        self._draw_scatter(df)
        self._draw_funnel(df)
        self._draw_clustered(df)
        self._draw_line(df)
        self._draw_hbar(df)

        self.fig.tight_layout()
        self.canvas.draw()

    def _draw_stacked(self, df):
        ax = self.ax_stacked
        ax.clear()
        x = np.arange(len(df))
        bottom = np.zeros(len(df))
        src_filter = self.src_var.get()
        active_map = {'Home':'From Home', 'Hashtags':'From Hashtags', 'Explore':'From Explore', 'Other':'From Other'}

        for src in ['From Home', 'From Hashtags', 'From Explore', 'From Other']:
            alpha = 1.0 if src_filter == 'All' or src == active_map.get(src_filter) else 0.2
            ax.bar(x, df[src], bottom=bottom, color=SOURCE_COLORS[src], alpha=alpha, label=src, edgecolor='none')
            bottom += df[src]
        
        self._style_ax(ax, 'Impression Source Breakdown', 'Post', 'Impressions')
        step = max(1, len(df)//10)
        ax.set_xticks(x[::step])
        ax.set_xticklabels(df['Post Index'].values[::step])
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.25), ncol=4, frameon=True, fancybox=True, edgecolor='#CCC', fontsize=8)

    def _draw_donut(self, df):
        ax = self.ax_donut
        ax.clear()
        sources = ['From Home', 'From Hashtags', 'From Explore', 'From Other']
        values = [df[s].sum() for s in sources]
        
        if sum(values) == 0: return
        wedges, _, autotexts = ax.pie(values, colors=[SOURCE_COLORS[s] for s in sources], autopct='%1.1f%%', pctdistance=0.75, wedgeprops=dict(width=0.4, edgecolor=CARD_BG))
        for t in autotexts: t.set_fontsize(9); t.set_color(TEXT_PRI); t.set_fontweight('bold')
        self._style_ax(ax, 'Traffic Sources')
        ax.legend(['Home', 'Hashtags', 'Explore', 'Other'], loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=2, frameon=True, fancybox=True, edgecolor='#CCC', fontsize=8)

    def _draw_scatter(self, df):
        ax = self.ax_scatter
        ax.clear()
        ax.scatter(df['Impressions'], df['Engagement Total'], c=PRIMARY, alpha=0.6, edgecolors='white')
        self._style_ax(ax, 'Impression vs Engagement', 'Impressions', 'Engagement')

    def _draw_funnel(self, df):
        ax = self.ax_funnel
        ax.clear()
        stages = ['Impressions', 'Profile Visits', 'Follows']
        values = [df[s].sum() for s in stages]
        if values[0] == 0: return

        colors = [PRIMARY, ENGAGEMENT, REACH]
        max_w = 0.8
        y_pos = [0.8, 0.45, 0.1]
        
        for i, val in enumerate(values):
            w = max(0.1, max_w * (val/values[0]))
            ax.barh(y_pos[i], w, height=0.15, left=0.5 - w/2, color=colors[i], alpha=0.9)
            ax.text(0.5, y_pos[i] + 0.12, f"{stages[i]}: {val:,.0f}", ha='center', va='center', color=TEXT_PRI, fontweight='bold', fontsize=9)

        ax.set_xlim(0, 1); ax.set_ylim(0, 1)
        ax.set_xticks([]); ax.set_yticks([])
        self._style_ax(ax, 'Conversion Funnel')

    def _draw_clustered(self, df):
        ax = self.ax_clustered
        ax.clear()
        cats = ['Likes', 'Comments', 'Shares', 'Saves']
        n = len(cats)
        bar_w = 0.8 / n
        x = np.arange(len(df))

        for j, cat in enumerate(cats):
            ax.bar(x + (j - n/2 + 0.5)*bar_w, df[cat], bar_w, color=ENGAGE_COLORS[cat], label=cat, alpha=0.8)

        self._style_ax(ax, 'Engagement Breakdown', 'Post', 'Count')
        step = max(1, len(df)//10)
        ax.set_xticks(x[::step])
        ax.set_xticklabels(df['Post Index'].values[::step])
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.25), ncol=4, frameon=True, fancybox=True, edgecolor='#CCC', fontsize=8)

    def _draw_line(self, df):
        ax = self.ax_line
        ax.clear()
        x = df['Post Index'].values
        # Using smoothed data to fix fluctuations
        ax.plot(x, df['Profile Visits Smoothed'], color=ENGAGEMENT, lw=2, label='Profile Visits (Moving Avg)')
        ax.plot(x, df['Follows Smoothed'], color=REACH, lw=2, label='Follows (Moving Avg)')

        self._style_ax(ax, 'Profile Visits & Follows Trend', 'Post', 'Smoothed Count')
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.25), ncol=2, frameon=True, fancybox=True, edgecolor='#CCC', fontsize=8)

    def _draw_hbar(self, df):
        ax = self.ax_hbar
        ax.clear()
        top = df.nlargest(10, 'Saves').sort_values('Saves')
        if top.empty: return

        bars = ax.barh([f"Post {i}" for i in top['Post Index']], top['Saves'], color=POSITIVE)
        for bar in bars:
            ax.text(bar.get_width(), bar.get_y() + bar.get_height()/2, f" {bar.get_width():,.0f}", va='center', fontsize=8)

        self._style_ax(ax, 'Top 10 Posts by Saves', 'Saves', '')

if __name__ == '__main__':
    root = tk.Tk()
    app = InstagramDashboard(root)
    root.mainloop()
