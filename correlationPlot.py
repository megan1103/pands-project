import numpy as np    
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
csv_file = 'C:/Users/odonovanm/Documents/iris dataset.csv'
iris =  pd.read_csv(csv_file)
dataset = pd.DataFrame(iris)
#df = dataset.rename  = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'species']
df = dataset.rename({'sepal_length': 'Sepal-Length', 'sepal_width': 'Sepal-Width', 'petal_length': 'Petal-Length', 'petal_width': 'Petal-Width', 'species': 'Species'}, axis=1)

# Plotting heat map
sns.heatmap(df.corr(),  linecolor = 'white', linewidths = 1,annot=True) ## annot adds the numeric value of the tile
plt.show()