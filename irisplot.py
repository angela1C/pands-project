# I am creating a script for plots again.


# 1. IMPORT PYTHON LIBRARIES

print("First importing the python libraries")
import pandas as pd  
import matplotlib.pyplot as plt 
import seaborn as sns


csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
col_names = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Class']

iris =  pd.read_csv(csv_url, names = col_names)
print(iris.head(10))

# a simple scatter plot
# plot sepal length on the x axis and sepal width on the y axis.
iris.plot(kind="scatter", x = 'Sepal_Length', y="Sepal_Width", c= "DarkBlue")
plt.show()

# note the axes does not start at the origin (0,0)

plt.show()
# a simple scatter plot
# plot petal length on the x axis and petal width on the y axis.
ax3 = iris.plot.scatter(x = 'Sepal_Length', y='Sepal_Width', c= 'Red')
plt.show()
