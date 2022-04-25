# Programming and Scripting
# Project 2022
# Author: Megan O'Donovan
# Summary: Create a correlation table and a heat map to see if there is a strong relationship between features

import numpy as np    
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
csv_file = 'C:/Users/odonovanm/Documents/iris dataset.csv'
iris =  pd.read_csv(csv_file)
iris = iris.rename({'sepal_length': 'Sepal-Length', 'sepal_width': 'Sepal-Width', 'petal_length': 'Petal-Length', 'petal_width': 'Petal-Width', 'species': 'Species'}, axis=1)

# Plotting heat map
sns.heatmap(iris.corr(),  linecolor = 'white', linewidths = 1,annot=True) ## annot adds the numeric value of the tile
plt.show()

# Plot a correlation table
print(iris.corr())

