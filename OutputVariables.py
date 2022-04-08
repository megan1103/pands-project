
import pandas as pd  
# 2. Outputs a summary of each variable to a single text file
# Create a variable `csv_file` and pass to it the csv where the data set is available
import pandas as pd  
# Load the dataset into python

csv_file = 'C:/Users/odonovanm/Documents/iris dataset.csv'

iris =  pd.read_csv(csv_file)

#print(iris) # prints to data frame

df = pd.DataFrame(iris)

df.to_csv (r'C:/Users/odonovanm/Documents/iris datasetExport.csv', index = False, header=True)

