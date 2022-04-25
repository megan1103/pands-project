# Programming and Scripting
# Project 2022
# Author: Megan O'Donovan
# Summary: Using rename to change the column names in the data file
# pands library allows csv to be imported/read
import pandas as pd 
csv_file = 'C:/Users/odonovanm/Documents/iris dataset.csv'
iris =  pd.read_csv(csv_file)

df = iris.rename({'sepal_length': 'Sepal-Length', 'sepal_width': 'Sepal-Width', 'petal_length': 'Petal-Length', 'petal_width': 'Petal-Width', 'species': 'Species'}, axis=1)
print(df)
