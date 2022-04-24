# Programming and Scripting
# Project 2022
# Author: Megan O'Donovan
# Summary: Create a histogram of each variable
import pandas as pd 
import numpy as np
import matplotlib.pyplot as pl
import seaborn as sns


# Load the dataset into python
csv_file = 'C:/Users/odonovanm/Documents/iris dataset.csv'
iris =  pd.read_csv(csv_file)
##print(iris.head(10)) 

#pl.subplot(2, 2, 1)  ### want to create a 4x4 view https://nickmccullum.com/python-visualization/subplots/
## First Plot  
## Plot histogram of  petal lengths
#_ = pl.hist(iris.petal_length)

## Label axes
#_ = pl.xlabel('petal length (cm)')
#_ = pl.ylabel('count')

##Second Plot
## Plot histogram of petal width
#pl.subplot(2, 2, 2)    
#_ = pl.hist(iris.petal_width)

## Label axes
#_ = pl.xlabel('petal width (cm)')
#_ = pl.ylabel('count') 

##Third Plot
#pl.subplot(2, 2, 3)    
## Plot histogram of sepal lengths
#_ = pl.hist(iris.sepal_length)

## Label axes
#_ = pl.xlabel('sepal length (cm)')
#_ = pl.ylabel('count')

##Fourth Plot
## Plot histogram of sepal width
#pl.subplot(2,2,4)
#_ = pl.hist(iris.sepal_width)

## Label axes
#_ = pl.xlabel('sepal width (cm)')
#_ = pl.ylabel('count') 
## Show histogram
#pl.show()

dataset = pd.DataFrame(iris)
#df = dataset.rename  = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'species']
iris_data = dataset.rename({'sepal_length': 'Sepal-Length', 'sepal_width': 'Sepal-Width', 'petal_length': 'Petal-Length', 'petal_width': 'Petal-Width', 'species': 'Species'}, axis=1)

hist = iris_data.hist()
plt.show()

