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

