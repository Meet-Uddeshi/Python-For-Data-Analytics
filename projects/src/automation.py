"""
This module provides a class and functional interface for automating the cleaning and
preprocessing of tabular datasets. It handles duplicate removal, string normalization,
missing value imputation, date standardization, data type casting, outlier removal
using the Interquartile Range (IQR) method, and categorical label encoding.
"""

import os
import warnings
# pyrefly: ignore [missing-import]
import numpy as np
import pandas as pd

# Suppress warnings for cleaner console output
warnings.filterwarnings("ignore")

class DataPreprocessor:
    """
    A class that automates standard data cleaning and preprocessing workflows
    on pandas DataFrames.
    
    This class encapsulates operations for removing duplicate rows, cleaning
    text columns, handling missing values, standardizing date-like columns,
    validating numeric data types, filtering outliers via the Interquartile
    Range (IQR) method, and performing Label Encoding on categorical features.
    """

    def __init__(self, verbose: bool = True):
        """
        Initializes the DataPreprocessor instance.

        Parameters:
            verbose (bool): If True, step-by-step logs and shapes will be printed.
        """
        self.verbose = verbose

    def load_data(self, file_path: str) -> pd.DataFrame:
        """
        Loads the dataset from the specified file path into a pandas DataFrame.

        Parameters:
            file_path (str): Path to the CSV file to load.

        Returns:
            pd.DataFrame: Loaded DataFrame.

        Raises:
            FileNotFoundError: If the input file does not exist.
            ValueError: If the file is empty or cannot be parsed as a CSV.
            IOError: If an unexpected error occurs while reading the file.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Input file not found at path: {file_path}")
        try:
            df = pd.read_csv(file_path)
            if df.empty:
                raise ValueError(f"The input CSV file at {file_path} is empty.")
            return df
        except pd.errors.EmptyDataError as e:
            raise ValueError(f"The input CSV file at {file_path} contains no data.") from e
        except pd.errors.ParserError as e:
            raise ValueError(f"Error parsing the CSV file at {file_path}: {str(e)}") from e
        except Exception as e:
            raise IOError(f"An unexpected error occurred while reading the file: {str(e)}") from e

    def remove_duplicates(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Removes duplicate rows from the DataFrame.

        Parameters:
            df (pd.DataFrame): The input DataFrame.

        Returns:
            pd.DataFrame: The DataFrame with duplicates removed.
        """
        return df.drop_duplicates()

    def clean_text_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Normalizes and cleans string/object columns in the DataFrame.
        This includes stripping leading/trailing whitespace, converting to lowercase,
        replacing multiple spaces with a single space, and removing non-alphanumeric characters.

        Parameters:
            df (pd.DataFrame): The input DataFrame.

        Returns:
            pd.DataFrame: The DataFrame with cleaned text columns.
        """
        str_cols = df.select_dtypes(include=['object']).columns
        for col in str_cols:
            # First, cast to string but preserve null values as actual NaNs to avoid "nan" string conversion
            null_mask = df[col].isna()
            df[col] = (
                df[col]
                .astype(str)
                .str.strip()
                .str.lower()
                .str.replace(r'\s+', ' ', regex=True)
                .str.replace(r'[^\w\s@]', '', regex=True)
            )
            # Re-apply null mask so missing values remain NaN/None for missing value handling
            df.loc[null_mask, col] = np.nan
        return df

    def handle_missing_values(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Imputes missing values in numerical columns using the median,
        and in categorical/object columns using the mode.

        Parameters:
            df (pd.DataFrame): The input DataFrame.

        Returns:
            pd.DataFrame: The DataFrame with imputed missing values.
        """
        num_cols = df.select_dtypes(include=[np.number]).columns
        for col in num_cols:
            df[col] = pd.to_numeric(df[col], errors='coerce')
            median_val = df[col].median()
            # If the entire column is NaN, fillna with a default value (e.g. 0)
            if pd.isna(median_val):
                median_val = 0.0
            df[col].fillna(median_val, inplace=True)

        cat_cols = df.select_dtypes(include=['object']).columns
        for col in cat_cols:
            if not df[col].empty:
                mode_series = df[col].mode()
                mode_val = mode_series[0] if not mode_series.empty else 'Unknown'
            else:
                mode_val = 'Unknown'
            df[col].fillna(mode_val, inplace=True)
        return df

    def standardize_dates(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Converts columns containing date/time keywords in their names to standardized datetime format.

        Parameters:
            df (pd.DataFrame): The input DataFrame.

        Returns:
            pd.DataFrame: The DataFrame with standardized date columns.
        """
        date_cols = df.select_dtypes(include=['object']).columns[
            df.columns.str.contains('date|Date|time|Time', case=False)
        ]
        for col in date_cols:
            df[col] = pd.to_datetime(df[col], errors='coerce').dt.normalize()
        return df

    def fix_data_types(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Ensures numeric columns are coerced to floats and rounded to 2 decimal places.

        Parameters:
            df (pd.DataFrame): The input DataFrame.

        Returns:
            pd.DataFrame: The DataFrame with standardized numeric data types.
        """
        num_cols = df.select_dtypes(include=[np.number]).columns
        for col in num_cols:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0.0)
        df[num_cols] = df[num_cols].astype(float).round(2)
        return df

    def remove_outliers(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Filters out outliers in numerical columns using the Interquartile Range (IQR) method.

        Parameters:
            df (pd.DataFrame): The input DataFrame.

        Returns:
            pd.DataFrame: The filtered DataFrame with outliers removed.
        """
        num_cols = df.select_dtypes(include=[np.number]).columns
        for col in num_cols:
            # If the column has zero variance or only contains one unique value, skip outlier removal
            if df[col].nunique() <= 1:
                continue
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR
            df = df[(df[col] >= lower) & (df[col] <= upper)]
        return df

    # def encode_categories(self, df: pd.DataFrame) -> pd.DataFrame:
    #     """
    #     Applies label encoding to low-cardinality categorical columns (< 10 unique values).

    #     Parameters:
    #         df (pd.DataFrame): The input DataFrame.

    #     Returns:
    #         pd.DataFrame: The DataFrame with encoded categories.
    #     """
    #     cat_cols = df.select_dtypes(include=['object']).columns
    #     for col in cat_cols:
    #         # Exclude date/datetime columns that might still be objects
    #         if df[col].nunique() < 10:
    #             le = LabelEncoder()
    #             df[col] = le.fit_transform(df[col].astype(str))
    #     return df

    def save_data(self, df: pd.DataFrame, output_path: str) -> None:
        """
        Saves the DataFrame to a CSV file.

        Parameters:
            df (pd.DataFrame): The DataFrame to save.
            output_path (str): Destination file path.

        Raises:
            IOError: If saving the file fails due to permissions or disk errors.
        """
        try:
            df.to_csv(output_path, index=False)
        except Exception as e:
            raise IOError(f"Failed to save cleaned data to {output_path}: {str(e)}") from e

    def process(self, file_path: str, output_path: str = "cleaned_data.csv") -> pd.DataFrame:
        """
        Executes the full pipeline: load, clean, transform, and save.

        Parameters:
            file_path (str): Path to the raw CSV data.
            output_path (str): Path to output the cleaned CSV.

        Returns:
            pd.DataFrame: Cleaned DataFrame.
        """
        if self.verbose:
            print(f"Starting automated data cleaning pipeline for: {file_path}")

        # Step 1: Load data
        df = self.load_data(file_path)
        original_shape = df.shape
        if self.verbose:
            print(f"Loaded data: {original_shape[0]} rows and {original_shape[1]} columns")

        # Step 2: Remove duplicates
        df = self.remove_duplicates(df)
        if self.verbose:
            print(f"After removing duplicates: {df.shape[0]} rows and {df.shape[1]} columns")

        # Step 3: Clean text columns
        df = self.clean_text_columns(df)

        # Step 4: Handle missing values
        df = self.handle_missing_values(df)

        # Step 5: Standardize dates
        df = self.standardize_dates(df)

        # Step 6: Fix data types
        df = self.fix_data_types(df)

        # Step 7: Remove outliers
        df = self.remove_outliers(df)
        if self.verbose:
            print(f"After removing outliers (IQR method): {df.shape[0]} rows and {df.shape[1]} columns")

        # Step 9: Save output
        self.save_data(df, output_path)

        if self.verbose:
            print(f"Cleaning complete. File saved to: {output_path}")
            print(f"Shape of cleaned data: {df.shape} and raw data shape: {original_shape}")
            print("\nData info:")
            df.info()

        return df


def auto_clean_data(file_path: str, output_path: str = "cleaned_data.csv", verbose: bool = True) -> pd.DataFrame:
    """
    Wrapper function to preserve backward compatibility for automated data cleaning.

    Parameters:
        file_path (str): Path to the input CSV file.
        output_path (str): Path to save the cleaned CSV file.
        verbose (bool): Whether to log status messages.

    Returns:
        pd.DataFrame: Cleaned pandas DataFrame.
    """
    preprocessor = DataPreprocessor(verbose=verbose)
    return preprocessor.process(file_path, output_path)


if __name__ == "__main__":
    # Example usage protected to prevent execution when imported
    try:
        df_clean = auto_clean_data("projects/data/covid_grouped.csv")
        print("\nSummary statistics of cleaned data:")
        print(df_clean.describe())
    except FileNotFoundError as err:
        print(f"Warning: Demo file 'raw_data.csv' not found. Exception details: {err}")
    except Exception as err:
        print(f"An unexpected error occurred during execution: {err}")
