# Data Cleaning and Preprocessing Automation

This guide explains how the automation script cleans and preprocesses raw data, how to run it, and how to customize it for your projects.

---

## How Each Step Works

### Step 1: Load Data
Reads your CSV file into a pandas `DataFrame`. Supports Excel exports (save as CSV first) and SQL query results.

### Step 2: Remove Duplicates
Drops exact duplicate rows instantly. In manufacturing/production logs with repeated entries, this alone reduces dataset size by 20-30%.

### Step 3: Clean Text Columns
* **Strip whitespace:** `"Jane Smith"` -> `"jane smith"`
* **Lowercase:** `"Sales"` -> `"sales"` (prevents grouping issues)
* **Remove special characters:** Cleans names, emails, departments.
* **Normalize spaces:** Multiple spaces are reduced to a single space.

Perfect for messy form data or manual entries.

### Step 4: Handle Missing Values
* **Numerical columns:** Fills with median or mean (robust against outliers).
* **Categorical columns:** Fills with mode (most frequent value).
* **If all missing:** Uses `'Unknown'` or `0`.

No more blank cells breaking your Power BI visualizations.

### Step 5: Standardize Dates
Converts multiple formats to standard datetime:
* `*2021/03/20` -> `2021-03-20`
* `*15/06/2022` -> `2022-06-15`
* `*2020-01-15` -> `2020-01-15` (already standard)

Ready for time-series analysis and Power BI date hierarchies.

### Step 6: Fix Data Types
Forces correct types:
* Numbers stored as text are converted to `float`.
* Rounds decimals to 2 places (e.g., `50000.123456` -> `50000.12`).
* Handles errors gracefully (converts invalid entries to `0`).

Prevents "can't perform math operations" errors.

### Step 7: Remove Outliers (IQR Method)
Uses the Interquartile Range to detect and remove extreme values:
* Calculates `Q1` (25th percentile) and `Q3` (75th percentile).
* `IQR = Q3 - Q1`
* Removes values below `Q1 - 1.5 * IQR` or above `Q3 + 1.5 * IQR`.

**Example:** If Salary range is 40k-70k, it removes entries like 999k or -5k.

Safe method that keeps 99% of valid data while removing errors.

### Step 8: Encode Categories (Optional)
Converts text categories to numbers for machine learning:
* `"sales"` -> `0`
* `"marketing"` -> `1`
* `"finance"` -> `2`

Only applies to low-cardinality columns (less than 10 unique values).

---

## How to Run the Script

### Step 1: Install Libraries
Open your terminal/command prompt and run:
```bash
uv pip install -r requirements.txt
```

### Step 2: Save Your Data
Export your messy data as a CSV file:
* **From Excel:** File > Save As > CSV
* **From SQL:** Export query results as CSV
* **From Power BI:** Export data to CSV

### Step 3: Run the Script
In Jupyter Notebook, VS Code, or a Python file:
```python
# Standard usage
df_clean = auto_clean_data('your_file.csv')

# Custom output path
df_clean = auto_clean_data('sales_data.csv', output_path='sales_cleaned.csv')

# Silent mode (no print statements)
df_clean = auto_clean_data('data.csv', verbose=False)
```

### Step 4: Check Results
The script automatically prints:
* Original row count
* Rows after duplicate removal
* Final shape
* Data types summary
* First few rows preview

Review output data in Excel or load it into Power BI.

---

## Pro Tips for Beginners

### Tip 1: Test on Small Samples First
Before running on your full dataset (10,000+ rows), test on the first 100 rows:
```python
df = pd.read_csv('huge_file.csv', nrows=100)
```

### Tip 2: Comment Out Steps You Don't Need
If you want to keep duplicate rows:
```python
# df = df.drop_duplicates()  # Commented out
```
If you do not want outlier removal:
```python
# Step 7: Remove outliers (IQR method, safe for beginners)
# Comment out the entire for loop
```

### Tip 3: Check Before and After
Always compare shapes and information:
```python
df_original = pd.read_csv('data.csv')
print("Before:", df_original.shape)
print(df_original.info())

df_clean = auto_clean_data('data.csv')
print("After:", df_clean.shape)
```

### Tip 4: Visualize Your Data
After cleaning:
```python
import matplotlib.pyplot as plt

# Check distributions
df_clean['Salary'].hist()
plt.show()

# Summary statistics
print(df_clean.describe())
```

### Tip 5: Save Intermediate Steps
For debugging, save the state after each major step:
```python
df.to_csv('after_duplicates.csv', index=False)
df.to_csv('after_missing.csv', index=False)
df.to_csv('after_outliers.csv', index=False)
```

---

## Customize for Your Projects

### Add Column Dropping
Remove unwanted columns before cleaning:
```python
def auto_clean_data(file_path, output_path='cleaned_data.csv', drop_cols=None, verbose=True):
    df = pd.read_csv(file_path)
    
    # Drop columns if specified
    if drop_cols:
        df = df.drop(columns=drop_cols, errors='ignore')
    
    # Rest of cleaning steps...
```

### Change Imputation Strategy
Use mean instead of median:
```python
# Replace in Step 4
df[col].fillna(df[col].mean(), inplace=True)  # Instead of median
```

### Adjust Outlier Sensitivity
Make outlier detection stricter (keeps less data):
```python
# Replace 1.5 with 1.0 in Step 7
lower = Q1 - 1.0 * IQR
upper = Q3 + 1.0 * IQR
```
Or make it more lenient (keeps more data):
```python
lower = Q1 - (3.0 * IQR)
upper = Q3 + (3.0 * IQR)
```

### Add Date Extraction
Extract year, month, and day details for analysis:
```python
# After Step 5
for col in date_cols:
    df[col] = pd.to_datetime(df[col], errors='coerce')
    df[f'{col}_year'] = df[col].dt.year
    df[f'{col}_month'] = df[col].dt.month
    df[f'{col}_day'] = df[col].dt.day
```

---

## For more than 1 GB data

* **Error:** `MemoryError`
* **Solution:** Process the dataset in chunks

```python
chunk_size = 10000
for chunk in pd.read_csv(file_path, chunksize=chunk_size):
    # Process each chunk
    cleaned_chunk = auto_clean_data(chunk)
```