# Programming and Scripting
# Project 2022
# Author: Megan O'Donovan
# Summary: Code used to upload and analysis Iris dataset for final project
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset into python
csv_file = 'C:/Users/odonovanm/Documents/iris dataset.csv'
iris =  pd.read_csv(csv_file)


dataset = pd.DataFrame(iris)
# Changing column names
iris_data = dataset.rename({'sepal_length': 'Sepal-Length', 'sepal_width': 'Sepal-Width', 'petal_length': 'Petal-Length', 'petal_width': 'Petal-Width', 'species': 'Species'}, axis=1)

# Using the pandas DataFrame method head/tail to return the first/last rows of the DataFrame and check that the file was correctly loaded
print(iris_data.head(10)) 
print(iris_data.tail(10))

# Check what data type are in the dataset
print(iris_data.dtypes)

# Check if there are duplicates
# Check if there are null or na values
print(iris_data[iris_data.duplicated()])
print(*iris_data.isna().any())

# Describes give statistical calulcation summary like mean, count, Q1/Q4
# Info gives info summary i.e the number of rows/columns, type of measures
print(iris_data.describe())
print(iris_data.info())

## group the example dataframe by the species and then run the describe() method on iris. This would run .describe() on the sepal_length values for each season as a grouped dataset. 
print(iris_data.groupby(["Species"])[["Sepal-Length"]].describe())

##plots
# Histogram
hist = iris_data.hist()
plt.show()

# Scatter Plots showing length vs width split by flower type
plt.title("Comparison between various species based on Sepal length and width")
plt.xlabel('Sepal length',fontsize=15)
plt.ylabel('Sepal width',fontsize=15)
sns.scatterplot(iris_data['Sepal-Length'],iris_data['Sepal-Width'],hue =iris_data['Species'],s=50)
plt.show()

plt.title("Comparison between various species based on Petal length and width")
plt.xlabel('Petal length',fontsize=15)
plt.ylabel('Petal width',fontsize=15)
sns.scatterplot(iris_data['Petal-Length'],iris_data['Petal-Width'],hue =iris_data['Species'],s=50)
plt.show()

#Pairs Plot
## Compares Petal and Sepal features at once
df2 = sns.pairplot(iris_dataset,hue="Species")
plt.show()

# Correlation Plot
## Heat Map 
sns.heatmap(iris_data.corr(),  linecolor = 'white', linewidths = 1,annot=True) 
plt.show()

## Correlation Table
print(iris_data.corr())
