# Topic: Matplotlib & seaborn library
# Commomn Graphs:
# Line Plot     -> Trend over time
# Bar Plot      -> Category comparison
# Histogram     -> Frequency distribution
# Scatter Plot  -> Relationship between variables
# Box Plot      -> Outlier detection
# Heatmap       -> Correlation visualization
# Pie Chart     -> Proportion of each category to the whole

# Matplotlib:
# Matplotlib is a python library used for data visualization. It is used for creating static, animated, and interactive visualizations in Python. It is a comprehensive library for creating a wide variety of plots and charts, including line plots, scatter plots, histograms, bar charts, and more. Matplotlib is widely used in data analysis, machine learning, and scientific computing.

# Functions:
# plt.plot() - creates a line plot.
# plt.scatter() - creates a scatter plot.
# plt.hist() - creates a histogram.
# plt.bar() - creates a bar chart.
# plt.pie() - creates a pie chart.
# plt.show() - displays the plot.
# plt.title() - sets the title of the plot.
# plt.xlabel() - sets the label of the x-axis.
# plt.ylabel() - sets the label of the y-axis.
# plt.legend() - displays the legend.
# plt.grid() - displays the grid.

# Example:
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Student": ["A", "B", "C", "D", "E"],
    "Marks": [75, 85, 90, 60, 95]
}

df = pd.DataFrame(data)

# Line chart
plt.figure(figsize=(6, 4))
plt.plot(df["Student"], df["Marks"], marker='o')
plt.title("Student Marks Line Plot")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Bar chart
plt.figure(figsize=(6, 4))
plt.bar(df["Student"], df["Marks"])
plt.title("Student Marks Bar Graph")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Histogram chart
marks = [55, 60, 65, 70, 75, 80, 85, 90, 95]

plt.figure(figsize=(6, 4))
plt.hist(marks)
plt.title("Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# Searborn:
# Seaborn is a Python data visualization library based on Matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics. Seaborn works well with Pandas DataFrames and NumPy arrays, making it a popular choice for exploratory data analysis. It includes various statistical plots like heatmaps, violin plots, pair plots, and more, which are not easily available in standard Matplotlib.

# Functions:
# sns.lineplot() - creates a line plot.
# sns.scatterplot() - creates a scatter plot.
# sns.histplot() - creates a histogram.
# sns.barplot() - creates a bar chart.
# sns.pieplot() - creates a pie chart.
# sns.show() - displays the plot.
# sns.title() - sets the title of the plot.
# sns.xlabel() - sets the label of the x-axis.
# sns.ylabel() - sets the label of the y-axis.
# sns.legend() - displays the legend.
# sns.grid() - displays the grid.

# Example:
import seaborn as sns 

data = {
    "Student": ["A", "B", "C", "D", "E"],
    "Marks": [75, 85, 90, 60, 95]
}

df = pd.DataFrame(data)

# Scatter plot chart
plt.figure(figsize=(6, 4))
sns.scatterplot(x=df["Student"], y=df["Marks"])
plt.title("Scatter Plot")
plt.show()

# Box plot chart
plt.figure(figsize=(6, 4))
sns.boxplot(y=df["Marks"])
plt.title("Box Plot")
plt.show()

# Heatmap chart
correlation_data = pd.DataFrame({
    "Math": [90, 85, 80],
    "Science": [88, 82, 78],
    "English": [75, 70, 72]
})

plt.figure(figsize=(5, 4))
sns.heatmap(correlation_data.corr(), annot=True)
plt.title("Heatmap")
plt.show()
