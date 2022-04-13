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
dataset = pd.DataFrame(iris)
#df = dataset.rename  = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'species']
df = dataset.rename({'sepal_length': 'Sepal-Length', 'sepal_width': 'Sepal-Width', 'petal_length': 'Petal-Length', 'petal_width': 'Petal-Width', 'species': 'Species'}, axis=1)
plt.figure(4, figsize=(10, 8))
df.plot(kind ="scatter",
          x ='Sepal-Length',
          y ='Petal-Length')
plt.grid()
plt.show()

# sepal_length, petal_length are iris
# feature data height used to define
# Height of graph whereas hue store the
# class of iris dataset.
sns.FacetGrid(df, hue ="Species",
              height = 6).map(plt.scatter,
                              'Sepal-Length',
                              'Sepal-Width').add_legend()
plt.xlabel('Sepal length',fontsize=15)
plt.ylabel('Sepal width',fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.title('Sepal length vs. Sepal width',fontsize=15)
plt.legend(prop={'size': 13})
plt.show()
sns.FacetGrid(df, hue ="Species",
              height = 6).map(plt.scatter,
                              'Petal-Length',
                              'Petal-Width').add_legend()
plt.xlabel('Petal length',fontsize=15)
plt.ylabel('Petal width',fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.title('Petal length vs. Petal width',fontsize=15)
plt.legend(prop={'size': 13})
plt.show()