# 2d - graphical representation
# scatter, pie, line graph
# graph realted functions to be remembered.
# pie():	Pie chart
# scatter():	Scatter plot
# line()	: Line graph
# bar()	: Bar chart
# show()  : To display the graph

# legends: indentation tags
# markers: {"s"(square), "o"(circle), "^"(triangle), "*"(star), "D"(diamond), "X"(X), "|"(vertical line), "_"(horizontal line)}
# colors: {"red", "green", "blue", "yellow", "purple", "orange", "pink", "brown", "gray", "black"}
# seaborn - 3d graphs other remains same.
# has 3 axis and 360 degree rotating ability.

# scatter, pie, line graph
# graph realted functions to be remembered.
# pie():	Pie chart
# scatter():	Scatter plot
# line()	: Line graph
# bar()	: Bar chart
# show()  : To display the graph
# .pyplot - used to plot the graph and mandatory while importing matplotlib library
# import matplotlib.pyplot as plt


import matplotlib.pyplot as plt
import numpy as np

# scatter
x= [10,20,30,40,50]
y= [1,2,3,4,5]
plt.scatter(x,y)
plt.show()

# Pie Chart
plt.pie(y, labels=x)
plt.legend(labels=x, title="Categories", bbox_to_anchor=(1.5, 0.5), loc='center left')
plt.show()

# Line Graph
plt.plot(x, y)
plt.title('Line Graph of x vs y')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()

# colour
plt.plot(x, y)
plt.title('Line Graph of x vs y')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()

# colab used for research purpose, run on cloud, no installation, free to use, no memory management, secure connection.
# alternate for jupyter notebook.
# you can cnnect with your gdrive
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns



# matplotlib is used to plot graphs and charts.
# 2D graphs- line plot, histogram, bar plot, scatter plot, pie chart
#each graphs has different functions- bar-bar(), hist-hist(), plot-plot(), scatter-scatter(), pie-pie()
#functions are used to display the graph- show()
#use matplotlib.pyplot as plt
#legends- indention tag (tichku boxes on graph-it tells which color belongs to which data)
#pyplot- it is submodule of matplotlib, used for graph ploting 

import matplotlib.pyplot as plt
import numpy as np

x= np.array([10,20,30,40,5]) #numpy array
y= [1,2,3,4,50]  #simple array
# plt.scatter(x,y)
# plt.show()

plt.pie(x,labels=y)  #labels means showing category in different chart
plt.legend(labels= x, bbox_to_anchor=(1.158,-0.790), loc="center", colormap="tab10")  
plt.show()

#labels can be changed, it depends on the chart we are creating!
#bbox_to_anchor=(1.158,-0.790)- it tells the position of the legend
#loc="center"- it tells the position of the legend
#colormap="tab10"- it tells the color of the legend




