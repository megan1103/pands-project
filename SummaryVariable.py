
# Programming and Scripting
# Project 2022
# Author: Megan O'Donovan
# Summary: Outputs a summary of each variable using decribe and info

import pandas as pd  
csv_file = 'C:/Users/odonovanm/Documents/iris dataset.csv'
iris =  pd.read_csv(csv_file)
iris = iris.rename({'sepal_length': 'Sepal-Length', 'sepal_width': 'Sepal-Width', 'petal_length': 'Petal-Length', 'petal_width': 'Petal-Width', 'species': 'Species'}, axis=1)

# Summary statistics of column Sepal_Length
print(iris.describe())

# Summary statistics of column Sepal_Length
print(iris['Sepal-Length'].describe())

#The output of the .info() method shows you the number of rows (or entries) and the number of columns, 
#as well as the columns names and the types of data they contain (e.g. float64 which is the default decimal type in Python).
print(iris.info())

## Groups the example dataframe by the species and then run the describe() method on iris. 
#This would run .describe() on the sepal_length values for each season as a grouped dataset. 

describe_species=iris.groupby(["Species"])[["Sepal-Length"]].describe()
print(describe_species)
