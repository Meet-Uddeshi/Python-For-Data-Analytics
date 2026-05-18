# Used for data manipulation
# any type of data can be imported in a pandas. like (excel, txt,csv,html etc)
# convert dataframe to any data format. like (csv,excel,json etc) and vice versa
# inbuilt functions:
# pd.read_csv("filename or path")
# pd.read_excel("filename or path")
# pd.read_txt("filename or path")
# pd.read_html("filename or path")
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
data = pd.read_csv("C:/Users/Admin/Documents/Python-For-Data-Analytics/data/swiggy_vs_zomato_3000.csv")
# print(data)

# print(data.head(10))

# print(data.tail(10))

# print(data.info())

# print(data.shape)

# print(data.describe()) - Only will run for onlly integer data in dataset

# print(data.columns)

# print(data.index)

# print(data.dtypes)

# print(data.nunique())

# print(data.value_counts()) - put coloumn name in () to get the value counts of that column

# print(data.unique())

# print(data.isnull().sum())

# print(data.dropna())

# print(data.fillna())  - give value to null value. example data.fillna(0)

# print(data.drop_duplicates())

# print(data.drop()) - put values in () to drop values. example data.drop(0)
