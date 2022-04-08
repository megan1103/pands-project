# Programming and Scripting
# Project 2022
# Author: Megan O'Donovan
# Summary: Download the dataset Iris and save the file to my documents folder. 
import pandas as pd  
# Load the dataset into python

csv_file = 'C:/Users/odonovanm/Documents/iris dataset.csv'

iris =  pd.read_csv(csv_file)
#print(iris.head(10)) #using the pandas DataFrame method head to return the first rows of the DataFrame and check that the file was correctly loaded

print(iris) # prints to data frame

