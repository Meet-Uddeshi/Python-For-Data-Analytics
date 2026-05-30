# Instagram Post Performance Dashboard

An interactive, single-page analytics dashboard built purely in Python for analysing Instagram post performance.

## Features

- **Pure Python**: Built using only `numpy`, `pandas`, `matplotlib`, and `seaborn`. No HTML, CSS, JavaScript, or web frameworks.
- **Interactive UI**: Custom sliders for Impressions and Follows, radio buttons for categorical filtering, and dynamic hover tooltips.
- **7 Chart Types**: Stacked bar, donut, scatter, funnel, clustered bar, line, and horizontal bar charts.
- **5 KPI Cards**: Displays high-level metrics for Impressions, Engagement Rate, Follows, Save Rate, and Profile Visit Rate.
- **Dark Theme**: Strict adherence to a custom, modern dark UI aesthetic.
- **CSV Upload**: Built-in native file picker to load your own datasets at runtime.

## Requirements

Ensure you have Python 3.7+ installed.

```bash
pip install numpy pandas matplotlib seaborn
```

## Running the Dashboard

You can launch the dashboard directly from your terminal:

```bash
cd src
python app.py
```

The application will automatically load the default dataset (`data/Instagram data.csv`) if it's available. To upload your own dataset, click the "**Upload CSV**" button in the top right corner of the dashboard.

## Dataset Format

If you upload your own CSV, it should either have no headers (matching the default order) or be a standard CSV. The script expects up to 13 columns (numeric columns will be coerced, missing will be filled with 0):

1. Impressions (INT)
2. From Home (INT)
3. From Hashtags (INT)
4. From Explore (INT)
5. From Other (INT)
6. Saves (INT)
7. Comments (INT)
8. Shares (INT)
9. Likes (INT)
10. Profile Visits (INT)
11. Follows (INT)
12. Caption (String)
13. Hashtags (String)
