# Programming and Scripting
# Project 2022
# Author: Megan O'Donovan
# Summary: Using describe that gives you the count, mean, max, min of the data in a tabular format.
import numpy as np    
import pandas as pd
import matplotlib.pyplot as plt
csv_file = 'C:/Users/odonovanm/Documents/iris dataset.csv'
iris =  pd.read_csv(csv_file)
dataset = pd.DataFrame(iris)
#df = dataset.rename  = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'species']
df = dataset.rename({'sepal_length': 'Sepal-Length', 'sepal_width': 'Sepal-Width', 'petal_length': 'Petal-Length', 'petal_width': 'Petal-Width', 'species': 'Species'}, axis=1)
print(df)
