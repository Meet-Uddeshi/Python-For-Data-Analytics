"""
Instagram Post Performance Dashboard
=====================================
Interactive single-page analytics dashboard built with:
  NumPy · Pandas · Matplotlib · Seaborn

Usage:
    python app.py

Requirements:
    pip install numpy pandas matplotlib seaborn
"""

import os
import numpy as np
import pandas as pd

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RangeSlider, RadioButtons, Button
from matplotlib.patches import Rectangle
import seaborn as sns


# ═══════════════════════════════════════════════════════════════
# COLOUR PALETTE  (strict spec)
# ═══════════════════════════════════════════════════════════════
CANVAS_BG   = '#0F1117'
CARD_BG     = '#1A1D27'
PRIMARY     = '#7B61FF'       # bars, lines
ENGAGEMENT  = '#FF6B9D'       # engagement accent
REACH       = '#00D4FF'       # reach accent
POSITIVE    = '#00C48C'       # positive trend
NEGATIVE    = '#FF4D6A'       # negative trend
TEXT_PRI    = '#FFFFFF'       # primary text
TEXT_SEC    = '#A0A3B1'       # secondary text / labels
GRID_CLR    = '#2A2D3A'       # grid / borders

# Traffic-source colours  (stacked bar + donut)
SOURCE_COLORS = {
    'From Home':     PRIMARY,
    'From Hashtags': ENGAGEMENT,
    'From Explore':  REACH,
    'From Other':    TEXT_SEC,
}

# Engagement-breakdown colours  (clustered bar)
ENGAGE_COLORS = {
    'Likes':    ENGAGEMENT,
    'Comments': REACH,
    'Shares':   POSITIVE,
    'Saves':    PRIMARY,
}

# KPI card left-border accent colours  (one per card, in order)
KPI_ACCENTS = [REACH, ENGAGEMENT, POSITIVE, PRIMARY, TEXT_SEC]

# Column names expected in the CSV  (no header row in default file)
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
    """Convert *#RRGGBB* to an (r, g, b, a) tuple in 0-1 range."""
    h = hex_color.lstrip('#')
    return (int(h[:2], 16) / 255,
            int(h[2:4], 16) / 255,
            int(h[4:6], 16) / 255,
            alpha)


def format_number(n):
    """Render large numbers with K / M suffixes."""
    if abs(n) >= 1_000_000:
        return f'{n / 1_000_000:.1f}M'
    if abs(n) >= 1_000:
        return f'{n / 1_000:.1f}K'
    return f'{n:,.0f}'


# ═══════════════════════════════════════════════════════════════
# MAIN DASHBOARD
# ═══════════════════════════════════════════════════════════════

class InstagramDashboard:
    """
    Builds and runs the full interactive dashboard in a single
    Matplotlib window.  All charts, KPIs, and filters live inside
    one figure and are redrawn reactively whenever a filter changes.
    """

    # ──────────────────────────────────────────────────────────
    # INITIALISATION
    # ──────────────────────────────────────────────────────────

    def __init__(self):
        self._apply_global_style()
        self._load_default_data()
        self._init_filter_state()
        self._build_figure()
        self._build_widgets()
        self._draw_all()
        self._connect_events()
        plt.show()

    # ──────────────────────────────────────────────────────────
    # GLOBAL STYLE
    # ──────────────────────────────────────────────────────────

    def _apply_global_style(self):
        """Configure Matplotlib + Seaborn for the dark dashboard theme."""
        sns.set_style('dark', {
            'axes.facecolor':   CARD_BG,
            'figure.facecolor': CANVAS_BG,
            'grid.color':       GRID_CLR,
        })
        plt.rcParams.update({
            'font.family':     FONT,
            'font.size':       11,
            'text.color':      TEXT_PRI,
            'axes.labelcolor': TEXT_SEC,
            'axes.labelsize':  11,
            'axes.edgecolor':  GRID_CLR,
            'axes.linewidth':  0.8,
            'xtick.color':     TEXT_SEC,
            'ytick.color':     TEXT_SEC,
            'xtick.labelsize': 9,
            'ytick.labelsize': 9,
            'grid.linewidth':  0.4,
            'grid.alpha':      0.30,
        })

    # ──────────────────────────────────────────────────────────
    # DATA LOADING
    # ──────────────────────────────────────────────────────────

    def _load_default_data(self):
        """Load the bundled *Instagram data.csv* from the data/ folder."""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(base_dir, '..', 'data', 'Instagram data.csv')
        if not os.path.isfile(csv_path):
            raise FileNotFoundError(
                f"Default dataset not found at:\n  {csv_path}\n"
                "Please place 'Instagram data.csv' in the data/ folder."
            )
        self._parse_csv(csv_path)

    def _parse_csv(self, filepath):
        """
        Read a CSV, auto-detect whether it contains a header row,
        coerce numeric columns, and compute all derived metrics.
        """
        # --- Read with auto header detection ---
        try:
            df = pd.read_csv(filepath, encoding='latin-1',
                             on_bad_lines='skip')
        except TypeError:                       # pandas < 1.3
            df = pd.read_csv(filepath, encoding='latin-1',
                             error_bad_lines=False)

        # If the first column name *looks* numeric, there is no header row
        first_col = str(df.columns[0]).strip()
        first_col_clean = first_col.replace(',', '').replace('.', '').replace('-', '')
        if first_col_clean.isdigit():
            try:
                df = pd.read_csv(filepath, header=None, names=COLUMNS,
                                 encoding='latin-1', on_bad_lines='skip')
            except TypeError:
                df = pd.read_csv(filepath, header=None, names=COLUMNS,
                                 encoding='latin-1', error_bad_lines=False)
        else:
            # Standardise column names to our expected set
            if len(df.columns) >= len(COLUMNS):
                df.columns = COLUMNS[: len(df.columns)]

        # --- Coerce numeric columns ---
        for col in COLUMNS[:11]:
            if col in df.columns:
                df[col] = (pd.to_numeric(df[col], errors='coerce')
                             .fillna(0)
                             .astype(int))

        # --- Computed metrics ---
        df['Engagement Total'] = (df['Likes'] + df['Comments']
                                  + df['Shares'] + df['Saves'])
        df['Engagement Rate'] = np.where(
            df['Impressions'] > 0,
            df['Engagement Total'] / df['Impressions'] * 100, 0.0)
        df['Save Rate'] = np.where(
            df['Impressions'] > 0,
            df['Saves'] / df['Impressions'] * 100, 0.0)
        df['Profile Visit Rate'] = np.where(
            df['Impressions'] > 0,
            df['Profile Visits'] / df['Impressions'] * 100, 0.0)
        df['Post Index'] = np.arange(1, len(df) + 1)

        self.df = df

    # ──────────────────────────────────────────────────────────
    # FILTER STATE
    # ──────────────────────────────────────────────────────────

    def _init_filter_state(self):
        self.traffic_source    = 'All'
        self.engagement_bucket = 'All'

    def _get_filtered(self):
        """Apply every active filter and return the resulting DataFrame."""
        df = self.df.copy()

        # Impressions range
        lo, hi = self.w_imp_slider.val
        df = df[(df['Impressions'] >= lo) & (df['Impressions'] <= hi)]

        # Follows threshold
        df = df[df['Follows'] >= int(self.w_fol_slider.val)]

        # Engagement-rate bucket
        bkt = self.engagement_bucket
        if bkt == 'Low (<2%)':
            df = df[df['Engagement Rate'] < 2]
        elif bkt == 'Mid (2-5%)':
            df = df[(df['Engagement Rate'] >= 2)
                    & (df['Engagement Rate'] <= 5)]
        elif bkt == 'High (>5%)':
            df = df[df['Engagement Rate'] > 5]

        return df.reset_index(drop=True)

    # ──────────────────────────────────────────────────────────
    # FIGURE & AXES LAYOUT
    # ──────────────────────────────────────────────────────────

    def _build_figure(self):
        """Create the figure window and every sub-axis."""

        self.fig = plt.figure(figsize=(24, 13.5), facecolor=CANVAS_BG)

        # Maximise window on Windows
        try:
            plt.get_current_fig_manager().window.state('zoomed')
        except Exception:
            pass
        try:
            self.fig.canvas.manager.set_window_title(
                'Instagram Post Performance Dashboard')
        except Exception:
            pass

        # ── Title ──
        self.fig.text(
            0.035, 0.98,
            '\u2728  Instagram Post Performance Dashboard',
            fontsize=20, fontweight='bold', color=TEXT_PRI, va='top',
            fontfamily=FONT)
        self.fig.text(
            0.035, 0.958,
            'Analyze reach, engagement & audience growth across posts',
            fontsize=10, color=TEXT_SEC, va='top', fontfamily=FONT)

        # ── Filter section labels ──
        lbl_y = 0.935
        self.fig.text(0.035, lbl_y, 'Impressions Range',
                      fontsize=10, color=TEXT_SEC, fontweight='bold')
        self.fig.text(0.265, lbl_y, 'Engagement Bucket',
                      fontsize=10, color=TEXT_SEC, fontweight='bold')
        self.fig.text(0.465, lbl_y, 'Traffic Source',
                      fontsize=10, color=TEXT_SEC, fontweight='bold')
        self.fig.text(0.680, lbl_y, 'Min Follows',
                      fontsize=10, color=TEXT_SEC, fontweight='bold')

        # ── Widget axes ──
        self.ax_w_imp = self.fig.add_axes(
            [0.035, 0.905, 0.205, 0.020], facecolor=CARD_BG)
        self.ax_w_eng = self.fig.add_axes(
            [0.265, 0.858, 0.170, 0.075], facecolor=CARD_BG)
        self.ax_w_src = self.fig.add_axes(
            [0.465, 0.848, 0.185, 0.088], facecolor=CARD_BG)
        self.ax_w_fol = self.fig.add_axes(
            [0.680, 0.905, 0.165, 0.020], facecolor=CARD_BG)
        self.ax_w_upl = self.fig.add_axes(
            [0.875, 0.898, 0.100, 0.040], facecolor=CARD_BG)

        for ax in (self.ax_w_imp, self.ax_w_eng, self.ax_w_src,
                   self.ax_w_fol, self.ax_w_upl):
            for sp in ax.spines.values():
                sp.set_color(GRID_CLR)
                sp.set_linewidth(0.6)

        # ── Separator below filters ──
        self.fig.add_artist(
            plt.Line2D([0.035, 0.975], [0.840, 0.840],
                       color=GRID_CLR, linewidth=0.6,
                       transform=self.fig.transFigure))

        # ── KPI card axes  (5 cards) ──
        self.kpi_axes = []
        kpi_y   = 0.790
        kpi_h   = 0.040
        kpi_gap = 0.008
        kpi_w   = (0.940 - 4 * kpi_gap) / 5
        for i in range(5):
            x = 0.035 + i * (kpi_w + kpi_gap)
            ax = self.fig.add_axes([x, kpi_y, kpi_w, kpi_h],
                                   facecolor=CARD_BG)
            ax.set_xticks([])
            ax.set_yticks([])
            for sp in ax.spines.values():
                sp.set_visible(False)
            self.kpi_axes.append(ax)

        # ── Separator below KPIs ──
        self.fig.add_artist(
            plt.Line2D([0.035, 0.975], [0.782, 0.782],
                       color=GRID_CLR, linewidth=0.6,
                       transform=self.fig.transFigure))

        # ── Chart axes ──
        gs = self.fig.add_gridspec(3, 3, left=0.035, right=0.975, bottom=0.05, top=0.74,
                                   wspace=0.25, hspace=0.55)

        # Row 1: Scatter (0), Clustered Bar (1), Stacked Bar (2)
        self.ax_scatter   = self.fig.add_subplot(gs[0, 0], facecolor=CARD_BG)
        self.ax_clustered = self.fig.add_subplot(gs[0, 1], facecolor=CARD_BG)
        self.ax_stacked   = self.fig.add_subplot(gs[0, 2], facecolor=CARD_BG)

        # Row 2: Line (0), Funnel (1), Donut (2)
        self.ax_line      = self.fig.add_subplot(gs[1, 0], facecolor=CARD_BG)
        self.ax_funnel    = self.fig.add_subplot(gs[1, 1], facecolor=CARD_BG)
        self.ax_donut     = self.fig.add_subplot(gs[1, 2], facecolor=CARD_BG)

        # Row 3: Horizontal Bar (spans all 3 columns)
        self.ax_hbar      = self.fig.add_subplot(gs[2, :], facecolor=CARD_BG)

        # Keep a list for easy iteration
        self.chart_axes = [
            self.ax_stacked, self.ax_donut, self.ax_scatter,
            self.ax_funnel, self.ax_clustered, self.ax_line,
            self.ax_hbar,
        ]

    # ──────────────────────────────────────────────────────────
    # INTERACTIVE WIDGETS
    # ──────────────────────────────────────────────────────────

    def _build_widgets(self):
        """Create sliders, radio buttons, and the upload button."""
        imp_min = int(self.df['Impressions'].min())
        imp_max = int(self.df['Impressions'].max())
        fol_max = int(self.df['Follows'].max())

        # ── Impressions range slider ──
        self.w_imp_slider = RangeSlider(
            self.ax_w_imp, '', imp_min, imp_max,
            valinit=(imp_min, imp_max), valstep=50,
            facecolor=PRIMARY,
            handle_style={'facecolor': PRIMARY,
                          'edgecolor': 'white', 'size': 8})
        self.w_imp_slider.valtext.set_color(TEXT_PRI)
        self.w_imp_slider.valtext.set_fontsize(8)

        # ── Follows threshold slider ──
        self.w_fol_slider = Slider(
            self.ax_w_fol, '', 0, max(fol_max, 1),
            valinit=0, valstep=1,
            color=POSITIVE,
            handle_style={'facecolor': POSITIVE,
                          'edgecolor': 'white', 'size': 8})
        self.w_fol_slider.valtext.set_color(TEXT_PRI)
        self.w_fol_slider.valtext.set_fontsize(8)

        # ── Engagement bucket radio buttons ──
        self.w_eng_radio = RadioButtons(
            self.ax_w_eng,
            ('All', 'Low (<2%)', 'Mid (2-5%)', 'High (>5%)'),
            activecolor=ENGAGEMENT)
        for lb in self.w_eng_radio.labels:
            lb.set_color(TEXT_SEC)
            lb.set_fontsize(9)

        # ── Traffic source toggle radio buttons ──
        self.w_src_radio = RadioButtons(
            self.ax_w_src,
            ('All', 'Home', 'Hashtags', 'Explore', 'Other'),
            activecolor=REACH)
        for lb in self.w_src_radio.labels:
            lb.set_color(TEXT_SEC)
            lb.set_fontsize(9)

        # ── Upload CSV button ──
        self.w_upload_btn = Button(
            self.ax_w_upl, '\U0001F4C1  Upload CSV',
            color=CARD_BG, hovercolor='#2A2D3A')
        self.w_upload_btn.label.set_color(TEXT_PRI)
        self.w_upload_btn.label.set_fontsize(9)

        # ── Wire callbacks ──
        self.w_imp_slider.on_changed(self._on_slider_change)
        self.w_fol_slider.on_changed(self._on_slider_change)
        self.w_eng_radio.on_clicked(self._on_engagement_change)
        self.w_src_radio.on_clicked(self._on_source_change)
        self.w_upload_btn.on_clicked(self._on_upload_click)

    # ──────────────────────────────────────────────────────────
    # CALLBACKS
    # ──────────────────────────────────────────────────────────

    def _on_slider_change(self, _val):
        """Triggered by either slider."""
        self._draw_all()

    def _on_engagement_change(self, label):
        self.engagement_bucket = label
        self._draw_all()

    def _on_source_change(self, label):
        self.traffic_source = label
        self._draw_all()

    def _on_upload_click(self, _event):
        """Open a native file picker and reload data."""
        try:
            import tkinter as tk
            from tkinter import filedialog
            root = tk.Tk()
            root.withdraw()
            filepath = filedialog.askopenfilename(
                title='Select Instagram CSV',
                filetypes=[('CSV files', '*.csv'), ('All files', '*.*')])
            root.destroy()
            if not filepath:
                return

            self._parse_csv(filepath)

            # Rebuild slider widgets with new data ranges
            imp_min = int(self.df['Impressions'].min())
            imp_max = int(self.df['Impressions'].max())
            fol_max = int(self.df['Follows'].max())

            self.ax_w_imp.clear()
            self.w_imp_slider = RangeSlider(
                self.ax_w_imp, '', imp_min, imp_max,
                valinit=(imp_min, imp_max), valstep=50,
                facecolor=PRIMARY,
                handle_style={'facecolor': PRIMARY,
                              'edgecolor': 'white', 'size': 8})
            self.w_imp_slider.valtext.set_color(TEXT_PRI)
            self.w_imp_slider.valtext.set_fontsize(8)
            self.w_imp_slider.on_changed(self._on_slider_change)

            self.ax_w_fol.clear()
            self.w_fol_slider = Slider(
                self.ax_w_fol, '', 0, max(fol_max, 1),
                valinit=0, valstep=1,
                color=POSITIVE,
                handle_style={'facecolor': POSITIVE,
                              'edgecolor': 'white', 'size': 8})
            self.w_fol_slider.valtext.set_color(TEXT_PRI)
            self.w_fol_slider.valtext.set_fontsize(8)
            self.w_fol_slider.on_changed(self._on_slider_change)

            self._draw_all()
        except Exception as exc:
            print(f'[Upload Error] {exc}')

    # ──────────────────────────────────────────────────────────
    # MASTER REDRAW
    # ──────────────────────────────────────────────────────────

    def _draw_all(self):
        """Clear and repaint every KPI card and chart."""
        df = self._get_filtered()

        # ── Empty-state guard ──
        if df.empty:
            for ax in self.chart_axes:
                ax.clear()
                ax.set_facecolor(CARD_BG)
                ax.text(0.5, 0.5, 'No data matches current filters',
                        transform=ax.transAxes, ha='center', va='center',
                        color=TEXT_SEC, fontsize=12)
            for ax in self.kpi_axes:
                ax.clear()
                ax.set_facecolor(CARD_BG)
                ax.set_xticks([])
                ax.set_yticks([])
                for sp in ax.spines.values():
                    sp.set_visible(False)
            self.fig.canvas.draw_idle()
            return

        self._draw_kpis(df)
        self._draw_stacked_bar(df)
        self._draw_donut(df)
        self._draw_scatter(df)
        self._draw_funnel(df)
        self._draw_clustered_bar(df)
        self._draw_line_chart(df)
        self._draw_top_saves(df)

        self.fig.canvas.draw_idle()

    # ──────────────────────────────────────────────────────────
    # SHARED AXIS STYLING HELPER
    # ──────────────────────────────────────────────────────────

    @staticmethod
    def _style_ax(ax, title, xlabel='', ylabel=''):
        """Apply the standard dark-theme styling to a chart axis."""
        ax.set_facecolor(CARD_BG)
        ax.set_title(title, fontsize=13, fontweight='bold',
                     color=TEXT_PRI, pad=8, loc='left', fontfamily=FONT)
        if xlabel:
            ax.set_xlabel(xlabel, fontsize=10, color=TEXT_SEC)
        if ylabel:
            ax.set_ylabel(ylabel, fontsize=10, color=TEXT_SEC)
        ax.tick_params(colors=TEXT_SEC, labelsize=8)
        ax.grid(True, alpha=0.15, color=GRID_CLR, linewidth=0.4)
        for sp in ax.spines.values():
            sp.set_color(GRID_CLR)

    # ──────────────────────────────────────────────────────────
    # ROW 1 — KPI CARDS
    # ──────────────────────────────────────────────────────────

    def _draw_kpis(self, df):
        """Render the five metric cards with left-border accents."""
        metrics = [
            ('Total Impressions',
             format_number(df['Impressions'].sum())),
            ('Avg Engagement Rate',
             f"{df['Engagement Rate'].mean():.2f}%"),
            ('Total Follows',
             format_number(df['Follows'].sum())),
            ('Avg Save Rate',
             f"{df['Save Rate'].mean():.2f}%"),
            ('Avg Profile Visit Rate',
             f"{df['Profile Visit Rate'].mean():.2f}%"),
        ]

        for i, (label, value) in enumerate(metrics):
            ax = self.kpi_axes[i]
            ax.clear()
            ax.set_facecolor(CARD_BG)
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            ax.set_xticks([])
            ax.set_yticks([])
            for sp in ax.spines.values():
                sp.set_visible(False)

            # Left accent border (thin vertical bar)
            ax.add_patch(Rectangle(
                (0, 0.05), 0.018, 0.90,
                facecolor=KPI_ACCENTS[i],
                transform=ax.transAxes, clip_on=False, zorder=10))

            # Metric value  (large, white, bold)
            ax.text(0.10, 0.66, value,
                    fontsize=17, fontweight='bold', color=TEXT_PRI,
                    va='center', transform=ax.transAxes,
                    fontfamily=FONT)

            # Metric label  (smaller, secondary colour)
            ax.text(0.10, 0.28, label,
                    fontsize=9, color=TEXT_SEC,
                    va='center', transform=ax.transAxes,
                    fontfamily=FONT)

    # ──────────────────────────────────────────────────────────
    # ROW 2 LEFT — STACKED BAR CHART  (impression sources)
    # ──────────────────────────────────────────────────────────

    def _draw_stacked_bar(self, df):
        ax = self.ax_stacked
        ax.clear()

        x = np.arange(len(df))
        sources = ['From Home', 'From Hashtags', 'From Explore', 'From Other']
        active_map = {
            'Home': 'From Home', 'Hashtags': 'From Hashtags',
            'Explore': 'From Explore', 'Other': 'From Other',
        }
        bottom = np.zeros(len(df))

        for src in sources:
            alpha = 1.0
            if self.traffic_source != 'All':
                alpha = (1.0
                         if src == active_map.get(self.traffic_source)
                         else 0.18)
            ax.bar(x, df[src].values, bottom=bottom,
                   color=SOURCE_COLORS[src], alpha=alpha,
                   width=0.85, label=src, edgecolor='none')
            bottom += df[src].values

        self._style_ax(ax, 'Impression Source Breakdown',
                       'Post Index', 'Impressions')
        ax.set_xlim(-0.5, len(df) - 0.5)

        # Show every Nth tick so labels don't overlap
        step = max(1, len(df) // 15)
        ax.set_xticks(x[::step])
        ax.set_xticklabels(df['Post Index'].values[::step])

        ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.10),
                  ncol=4, fontsize=8, facecolor=CARD_BG,
                  edgecolor=GRID_CLR, labelcolor=TEXT_SEC,
                  framealpha=0.9)

    # ──────────────────────────────────────────────────────────
    # ROW 2 RIGHT — DONUT CHART  (aggregate traffic share)
    # ──────────────────────────────────────────────────────────

    def _draw_donut(self, df):
        ax = self.ax_donut
        ax.clear()
        ax.set_facecolor(CARD_BG)

        sources = ['From Home', 'From Hashtags', 'From Explore', 'From Other']
        values  = [df[s].sum() for s in sources]
        labels  = ['Home', 'Hashtags', 'Explore', 'Other']
        colors  = [SOURCE_COLORS[s] for s in sources]

        active_map = {'Home': 0, 'Hashtags': 1, 'Explore': 2, 'Other': 3}

        # Highlight selected source, dim others
        if (self.traffic_source != 'All'
                and self.traffic_source in active_map):
            idx = active_map[self.traffic_source]
            explode = [0.06 if i == idx else 0 for i in range(4)]
            colors  = [hex_to_rgba(c, 1.0 if i == idx else 0.20)
                       for i, c in enumerate(colors)]
        else:
            explode = [0] * 4

        total = sum(values)
        if total == 0:
            ax.text(0.5, 0.5, 'No Data', ha='center', va='center',
                    color=TEXT_SEC, fontsize=12, transform=ax.transAxes)
            return

        wedges, _, autotexts = ax.pie(
            values, colors=colors, explode=explode,
            autopct=lambda p: f'{p:.1f}%' if p > 3 else '',
            startangle=90, pctdistance=0.78,
            wedgeprops=dict(width=0.38, edgecolor=CARD_BG, linewidth=2))

        for t in autotexts:
            t.set_fontsize(9)
            t.set_color(TEXT_PRI)
            t.set_fontweight('bold')

        # Centre label
        ax.text(0, 0, 'Traffic\nSources', ha='center', va='center',
                fontsize=11, fontweight='bold', color=TEXT_PRI,
                fontfamily=FONT)

        ax.set_title('Aggregate Traffic Share', fontsize=13,
                     fontweight='bold', color=TEXT_PRI, pad=6,
                     loc='left', fontfamily=FONT)
        ax.legend(wedges, labels,
                  loc='upper center', bbox_to_anchor=(0.5, -0.03),
                  ncol=4, fontsize=8, facecolor=CARD_BG,
                  edgecolor=GRID_CLR, labelcolor=TEXT_SEC,
                  framealpha=0.9)

    # ──────────────────────────────────────────────────────────
    # ROW 3 LEFT — SCATTER PLOT  (Impressions vs Engagement)
    # ──────────────────────────────────────────────────────────

    def _draw_scatter(self, df):
        ax = self.ax_scatter
        ax.clear()

        self._scatter_pts = ax.scatter(
            df['Impressions'], df['Engagement Total'],
            c=PRIMARY, s=45, alpha=0.75,
            edgecolors='white', linewidth=0.3, zorder=5)
        self._scatter_df = df

        self._style_ax(ax, 'Impressions vs Engagement',
                       'Impressions', 'Engagement Total')

        # Hidden annotation for hover tooltips
        self._scatter_annot = ax.annotate(
            '', xy=(0, 0), xytext=(15, 15),
            textcoords='offset points',
            bbox=dict(boxstyle='round,pad=0.5', fc=CARD_BG,
                      ec=PRIMARY, lw=1.5, alpha=0.95),
            fontsize=9, color=TEXT_PRI, fontfamily=FONT,
            arrowprops=dict(arrowstyle='->', color=PRIMARY, lw=1.2))
        self._scatter_annot.set_visible(False)

    # ──────────────────────────────────────────────────────────
    # ROW 3 RIGHT — FUNNEL CHART
    # ──────────────────────────────────────────────────────────

    def _draw_funnel(self, df):
        ax = self.ax_funnel
        ax.clear()
        ax.set_facecolor(CARD_BG)

        stages = ['Impressions', 'Profile Visits', 'Follows']
        values = [df[s].sum() for s in stages]

        if values[0] == 0:
            ax.text(0.5, 0.5, 'No Data', ha='center', va='center',
                    color=TEXT_SEC, fontsize=12, transform=ax.transAxes)
            return

        # Gradient colours  (#00D4FF → blend → #7B61FF)
        gradient = [REACH, '#5C8CE6', PRIMARY]

        max_w   = 0.80
        y_pos   = [0.78, 0.45, 0.12]
        bar_h   = 0.22

        for i, (stg, val) in enumerate(zip(stages, values)):
            w = max_w * (val / values[0]) if values[0] else 0
            w = max(w, 0.10)       # ensure it's always visible
            left = 0.5 - w / 2

            ax.barh(y_pos[i], w, height=bar_h, left=left,
                    color=gradient[i], edgecolor='none',
                    alpha=0.90, zorder=3)

            # Stage label + value
            ax.text(0.5, y_pos[i], f'{stg}\n{val:,.0f}',
                    ha='center', va='center', fontsize=10,
                    fontweight='bold', color=TEXT_PRI,
                    fontfamily=FONT, zorder=4)

            # Drop-off percentage between stages
            if i > 0 and values[i - 1] > 0:
                drop = (values[i - 1] - val) / values[i - 1] * 100
                mid_y = (y_pos[i - 1] + y_pos[i]) / 2
                ax.text(0.93, mid_y, f'\u2193 {drop:.1f}%',
                        ha='center', va='center', fontsize=9,
                        color=NEGATIVE, fontweight='bold',
                        fontfamily=FONT)

        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_xticks([])
        ax.set_yticks([])
        for sp in ax.spines.values():
            sp.set_color(GRID_CLR)
        ax.set_title('Conversion Funnel', fontsize=13,
                     fontweight='bold', color=TEXT_PRI, pad=6,
                     loc='left', fontfamily=FONT)

    # ──────────────────────────────────────────────────────────
    # ROW 4 LEFT — CLUSTERED BAR  (engagement breakdown)
    # ──────────────────────────────────────────────────────────

    def _draw_clustered_bar(self, df):
        ax = self.ax_clustered
        ax.clear()

        categories = ['Likes', 'Comments', 'Shares', 'Saves']
        n_cats = len(categories)
        x = np.arange(len(df))
        bar_w = 0.8 / n_cats

        for j, cat in enumerate(categories):
            offset = (j - n_cats / 2 + 0.5) * bar_w
            ax.bar(x + offset, df[cat].values, bar_w,
                   color=ENGAGE_COLORS[cat], alpha=0.85,
                   label=cat, edgecolor='none')

        self._style_ax(ax, 'Engagement Breakdown',
                       'Post Index', 'Count')
        ax.set_xlim(-0.5, len(df) - 0.5)

        step = max(1, len(df) // 15)
        ax.set_xticks(x[::step])
        ax.set_xticklabels(df['Post Index'].values[::step])

        ax.legend(loc='upper right', fontsize=8,
                  facecolor=CARD_BG, edgecolor=GRID_CLR,
                  labelcolor=TEXT_SEC, framealpha=0.9)

    # ──────────────────────────────────────────────────────────
    # ROW 4 RIGHT — LINE CHART  (Profile Visits & Follows)
    # ──────────────────────────────────────────────────────────

    def _draw_line_chart(self, df):
        ax = self.ax_line
        ax.clear()

        x = df['Post Index'].values

        ax.plot(x, df['Profile Visits'].values,
                color=REACH, linewidth=1.8,
                marker='o', markersize=3, alpha=0.85,
                label='Profile Visits',
                markerfacecolor=REACH, markeredgecolor='none')
        ax.plot(x, df['Follows'].values,
                color=POSITIVE, linewidth=1.8,
                marker='o', markersize=3, alpha=0.85,
                label='Follows',
                markerfacecolor=POSITIVE, markeredgecolor='none')

        # Subtle fill beneath each curve
        ax.fill_between(x, df['Profile Visits'].values,
                        alpha=0.07, color=REACH)
        ax.fill_between(x, df['Follows'].values,
                        alpha=0.07, color=POSITIVE)

        self._style_ax(ax, 'Profile Visits & Follows',
                       'Post Index', 'Count')

        # Legend above chart
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15),
                  ncol=2, fontsize=9, facecolor=CARD_BG,
                  edgecolor=GRID_CLR, labelcolor=TEXT_SEC,
                  framealpha=0.9)

    # ──────────────────────────────────────────────────────────
    # ROW 5 — HORIZONTAL BAR  (Top 10 posts by Saves)
    # ──────────────────────────────────────────────────────────

    def _draw_top_saves(self, df):
        ax = self.ax_hbar
        ax.clear()

        top = (df.nlargest(min(10, len(df)), 'Saves')
                 [['Post Index', 'Saves']]
                 .sort_values('Saves'))

        if top.empty:
            ax.text(0.5, 0.5, 'No data', ha='center', va='center',
                    color=TEXT_SEC, fontsize=12,
                    transform=ax.transAxes)
            return

        y_labels = [f'Post {idx}' for idx in top['Post Index']]
        saves_vals = top['Saves'].values
        max_val = saves_vals.max()

        bars = ax.barh(y_labels, saves_vals, color=PRIMARY,
                       height=0.6, edgecolor='none', alpha=0.85)

        # Value labels at end of each bar
        for bar, val in zip(bars, saves_vals):
            ax.text(bar.get_width() + max_val * 0.012,
                    bar.get_y() + bar.get_height() / 2,
                    f' {val:,}',
                    va='center', ha='left', fontsize=9,
                    color=TEXT_PRI, fontweight='bold',
                    fontfamily=FONT)

        self._style_ax(ax, 'Top 10 Posts by Saves', 'Save Count', '')
        ax.set_xlim(0, max_val * 1.18 if max_val > 0 else 1)

    # ──────────────────────────────────────────────────────────
    # HOVER TOOLTIP  (scatter plot)
    # ──────────────────────────────────────────────────────────

    def _connect_events(self):
        """Register the mouse-motion event for hover tooltips."""
        self.fig.canvas.mpl_connect('motion_notify_event',
                                    self._on_hover)

    def _on_hover(self, event):
        """Show / hide the scatter-plot tooltip on mouse move."""
        if not hasattr(self, '_scatter_annot'):
            return
        annot = self._scatter_annot
        was_visible = annot.get_visible()

        if event.inaxes == self.ax_scatter:
            contained, ind = self._scatter_pts.contains(event)
            if contained:
                idx = ind['ind'][0]
                row = self._scatter_df.iloc[idx]
                pos = self._scatter_pts.get_offsets()[idx]
                annot.xy = pos
                annot.set_text(
                    f"Post {int(row['Post Index'])}\n"
                    f"Impressions: {int(row['Impressions']):,}\n"
                    f"Engagement: {int(row['Engagement Total']):,}\n"
                    f"Rate: {row['Engagement Rate']:.2f}%")
                annot.set_visible(True)
                self.fig.canvas.draw_idle()
                return

        if was_visible:
            annot.set_visible(False)
            self.fig.canvas.draw_idle()


# ═══════════════════════════════════════════════════════════════
# ENTRY POINT
# ═══════════════════════════════════════════════════════════════

if __name__ == '__main__':
    InstagramDashboard()
