# Programming and Scripting
# Project 2022
# Author: Megan O'Donovan
# Summary: Download the dataset Iris and save the file to my documents folder. 
import pandas as pd  
csv_file = 'C:/Users/odonovanm/Documents/iris dataset.csv'
iris =  pd.read_csv(csv_file)
head(iris)
tail(iris)
