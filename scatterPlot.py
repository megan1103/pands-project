# Programming and Scripting
# Project 2022
# Author: Megan O'Donovan
# Summary: Looking for a relationship between Species and the 4 measures using scatter plots
import numpy as np    
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

csv_file = 'C:/Users/odonovanm/Documents/iris dataset.csv'
iris =  pd.read_csv(csv_file)
iris_data = iris.rename({'sepal_length': 'Sepal-Length', 'sepal_width': 'Sepal-Width', 'petal_length': 'Petal-Length', 'petal_width': 'Petal-Width', 'species': 'Species'}, axis=1)

#scatter plot showing relationship between sepal features for the different flower types
plt.title("Comparison between various species based on Sepal length and width")
plt.xlabel('Sepal length',fontsize=15)
plt.ylabel('Sepal width',fontsize=15)
sns.scatterplot(iris_data['Sepal-Length'],iris_data['Sepal-Width'],hue =iris_data['Species'],s=50)
plt.savefig('C:/Users/odonovanm/Documents/sepal_scatterplot.png')
plt.show()

#scatter plot showing relationship between petal features for the different flower types
plt.title("Comparison between various species based on Petal length and width")
plt.xlabel('Petal length',fontsize=15)
plt.ylabel('Petal width',fontsize=15)
sns.scatterplot(iris_data['Petal-Length'],iris_data['Petal-Width'],hue =iris_data['Species'],s=50)
plt.savefig('C:/Users/odonovanm/Documents/petal-scatterplot.png')
plt.show()
