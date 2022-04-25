# Programming and Scripting
# Project 2022
# Author: Megan O'Donovan
# Summary: Imports the csv file and then exports the csv file to local desktop

import pandas as pd  
csv_file = 'C:/Users/odonovanm/Documents/iris dataset.csv'
iris =  pd.read_csv(csv_file)
iris.to_csv (r'C:/Users/odonovanm/Documents/iris datasetExport1.csv', index = False, header=True)

