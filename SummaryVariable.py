
import pandas as pd  
# 2. Outputs a summary of each variable to a single text file
# Create a variable `csv_file` and pass to it the csv where the data set is available
import pandas as pd  
# Load the dataset into python

csv_file = 'C:/Users/odonovanm/Documents/iris dataset.csv'

iris =  pd.read_csv(csv_file)

#print(df['sepal_length'].describe()) # Summary statistics of column Sepal_Length

#print(df.info()) ##The output of the .info() method shows you the number of rows (or entries) and the number of columns, as well as the columns names and the types of data they contain (e.g. float64 which is the default decimal type in Python).

## group the example dataframe by the species and then run the describe() method on iris. This would run .describe() on the sepal_length values for each season as a grouped dataset. 
precip_by_season=iris.groupby(["species"])[["sepal_length"]].describe()
print(precip_by_season)