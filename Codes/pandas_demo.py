#data manupulation 
#Pandas is a software library written in the Python programming language for data manipulation
#and analysis. In particular, it offers data structures and operations for manipulating
#numerical tables and time series.
#convert data frames to csv files(visevarse)
#inbuild functions-read_excel(), to_excel() pd.read_csv(), pd.to_csv(), pd.read_excel(),pd.to_excel()
#Pandas provides two main data structures:
#1. Series (1-D)
#2. DataFrame (2-D)

#Series – like a column in Excel
#DataFrame – like a whole Excel sheet

import pandas as pd
data = pd.read_csv("C:/Python-For-Data-Analytics/data/Amazon_Big_Sales_Dataset_2026.csv")
# print(data)

# print(data.head(6))

# print(data.tail(5))

#inbuild function-info, shape, describe, is null, fillna, dropna, duplicated, drop_duplicates

# print(data.info()) will give the information about the data frame
# print(data.shape()) will give the shape of the data frame
# print(data.describe()) will give the description of the data frame
# print(data.isnull()) will give the null values in the data frame
# print(data.fillna()) will fill the null values in the data frame
# print(data.dropna()) will drop the null values in the data frame
# print(data.duplicated()) will give the duplicated values in the data frame
# print(data.drop_duplicates()) will drop the duplicated values in the data frame

# print(data.info())
# print(data.shape)
# print(data.describe())
# print(data.isnull().sum())
# print(data.duplicated())
# print(data.drop_duplicates())
# print(data.dropna())
# print(data.fillna())

df = pd.DataFrame(data)
print(df)

