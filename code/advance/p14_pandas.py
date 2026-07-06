# Topic: Pandas & PandasAI library
# Pandas:
# Pandas is a python library used for data manipulation and analysis. It is used for data cleaning, data transformation, handling structured datasets, data exploration, and data visualization. It works with series and dataframe (2D tabular data).

# Functions:
# pd.read_csv("filename or path") - To read csv files.
# pd.read_excel("filename or path") - To read excel files.
# pd.read_txt("filename or path") - To read text files.
# pd.read_html("filename or path") - To read html files.
# data.head() - will display dat from upper rows.
# data.tail() - will display dat from lower rows.
# data.info() - will display the datatypes of the data.
# data.shape - will display the shape of the data.(coloumns and rows)
# data.describe() - will display the basic statistics of the data.
# data.columns - will display the columns of the data.
# data.index - will display the index of the data.
# data.dtypes - will display the data types of the data.
# data.nunique() - will display the number of unique values of the data.
# data.value_counts() - will display the count of each value in the data.
# data.unique() - will display the unique values of the data.
# data.isnull().sum() - will display the number of null values of the data.
# data.dropna() - will drop the null values of the data.
# data.fillna() - will fill the null values of the data.
# data.drop_duplicates() - will drop the duplicate values of the data.
# data.drop() - will drop the values of the data.

import pandas as pd 
data = pd.read_csv("your_data_file.csv")

print(data)
print(data.head(10))
print(data.tail(10))
print(data.info())
print(data.shape)
print(data.describe()) # Only will run for onlly integer data in dataset
print(data.columns)
print(data.index)
print(data.dtypes)
print(data.nunique())
print(data.value_counts()) 
print(data.unique())
print(data.isnull().sum())
print(data.dropna())
print(data.fillna())  # Give value to null value. example data.fillna(0)
print(data.drop_duplicates())
print(data.drop()) # Put values in () to drop values. example data.drop(0)

# PandasAI:
# PandasAI is an advanced Python library that combines the power of Pandas with Artificial Intelligence and Large Language Models (LLMs). It allows users to interact with datasets using natural language queries instead of writing complex Pandas code manually. By integrating AI models such as OpenAI or Hugging Face models, PandasAI can automatically analyze data, generate insights, create visualizations, and perform data manipulation tasks from simple text instructions. It is mainly used in data analysis, business intelligence, and AI-driven analytics systems to simplify data operations and improve productivity. PandasAI reduces coding complexity, speeds up exploratory data analysis, and makes data interaction more accessible for both technical and non-technical users.

# Working
# User Query
#      ↓
# LLM Understands Instruction
#      ↓
# Generates Pandas Code
#      ↓
# Executes Code on DataFrame
#      ↓
# Returns Result / Graph / Insight
# PandasAI works by combining a Pandas DataFrame with a Large Language Model (LLM). Instead of manually writing complex Pandas operations, the user gives instructions in natural language such as “show average salary,” “plot sales graph,” or “find missing values.” PandasAI sends the prompt to the AI model, interprets the request, generates the required Pandas code internally, executes it on the dataset, and returns the output in the form of tables, summaries, or visualizations. Internally, it acts as an intelligent layer on top of Pandas by converting human language into executable Python data analysis operations. This makes exploratory data analysis faster, easier, and more interactive.

# Example
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm.openai import OpenAI

data = {
    "Name": ["Meet", "Rahul", "Priya"],
    "Marks": [90, 80, 95]
}

df = pd.DataFrame(data)

# Connect OpenAI model
llm = OpenAI(api_token="YOUR_API_KEY") # Always keep any API KEY into .env file at root folder never commit and push that in any git server because that key is private.

# Convert normal dataframe into AI dataframe
smart_df = SmartDataframe(df, config={"llm": llm})

response = smart_df.chat("What is the average marks?")
print(response)

smart_df.chat("Show highest marks")
smart_df.chat("Plot a bar graph of marks")
smart_df.chat("Which student scored above 85?")
smart_df.chat("Calculate average marks")