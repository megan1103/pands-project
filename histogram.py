# Programming and Scripting
# Project 2022
# Author: Megan O'Donovan
# Summary: Create a histogram of each variable
import pandas as pd 
import numpy as np
import matplotlib.pyplot as pl
import seaborn as sns

csv_file = 'C:/Users/odonovanm/Documents/iris dataset.csv'
iris =  pd.read_csv(csv_file)
iris = iris.rename({'sepal_length': 'Sepal-Length', 'sepal_width': 'Sepal-Width', 'petal_length': 'Petal-Length', 'petal_width': 'Petal-Width', 'species': 'Species'}, axis=1)

hist = iris_data.hist()
plt.show()

