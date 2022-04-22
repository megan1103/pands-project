>> Author: Megan O'Donovan  
>> Date: 29/04/2022
##  Programming and Scripting 

### Introduction 
<p align="justify">
This ReadMe file contains an overview of my research carried out on the Fisher’s Iris data set. The research project is part of my continuous assessment for the module Programming and Scripting. A description of the course and assignment can be found on the course homepage here. The ReadMe file will provide a summary of background information on the Fishers’ Iris data set and documentation of the Python programming code used for analytical research. Key aspects of the code used will be explained as well as detailed explanation of the resulting output. <br/> </p>
<p align="center">
  <img src="https://github.com/megan1103/pands-project/blob/main/Iris%20flowers%20in%20Fisher%20dataset.png" >
</p>
<br/> 


### Summary of Dataset 
>#### *Description* 
<p align="justify">The dataset was initially created as an example if linear analysis by British statistician and biologist Ronald Fisher. The dataset comprises of 50 flowers for each of the three species of iris. The species are Iris setosa, versicolor, and virginica. Four features were measured from each sample, they are the length and the width of sepal and petal respectively, in centimetres. From this dataset, Fisher developed a linear model; distinguishing species based on the combination of those four features. Fisher’s Iris data set is one of the most famous multivariate data set used for testing various Machine Learning Algorithms. To summarise the Each sample has 4 features (length of petal, width of petal, length of sepal, width of sepal) and a specie name. The following image shows the difference between a petal and sepal, when measuring width and length. From the imagine, it’s easy to appreciate how meticulous fisher was in recording the measurements of 150 flowers.  <br/> </p>

>#### *Loading Dataset*
<p align="justify">Before the dataset is loaded, python libraries are imported. These libraries allow users to create visualisation and preform quieres. The libaries are imported and assigned abbrivated names solely to save time.  <br/> </p>

```python 
import numpy as np    
import pandas as pd  
import matplotlib.pyplot as plt 
import seaborn as sns
```

<p align="justify">Using python, there are two possible ways of loading the dataset. Python can query a csv using the url or the csv can be downloaded and saved locally. Either of these methods will result in uploading the dataset which is then loaded into a data frame using the panda library.  <br/> </p>
 
```python
csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
col_names = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Class']
iris_data =  pd.read_csv(csv_url, names = col_names)
```
 
```python
csv_file = 'C:/Users/odonovanm/Documents/iris dataset.csv'
iris_data =  pd.read_csv(csv_file)
```

>#### *Data Overview*
<p align="justify">In terms of research analysis, this is considered a small dataset. The data frame consists of 150 cases, each row of the table representing an iris flower; including its species and dimensions of its botanical parts, sepal and petal, in centimetres. <br/> </p>

```python
names(iris_data)
class(iris_data)
dim(iris_data)
```

<p align="justify">Because of this, it’s easy to check if the dataset was loaded to the data frame correctly. Using head() and tail() , python checks the first and last rows of the data frame, comparisons to the original csv can easily be made.  The data is loaded in table format, all the measurements are in centimetres *(cm)* and in the head preview we can see how it is arranged. The command tail() is particularly useful as most issues with a dataset failing to load, occurs at the end of the dataset.    <br/> </p>

```python
head(iris_data)
tail(iris_data)
```

| Sepal.Length     | Sepal.Width      | Petal.Length     | Petal.Width     |Species   |
| ------------- | ------------- | -------- | -------- | -------- |
|      5.1    |      3.5    |      1.4    |      0.2    |      setosa|
|      4.9    |      3.0    |      1.4    |      0.2    |      setosa|
|      4.7    |      3.2    |      1.3    |      0.2    |      setosa|
|      4.6    |      3.1    |      1.5    |      0.2    |      setosa|
|      5.0    |      3.6    |      1.4    |      0.2    |      setosa|
|      5.4    |      3.9    |      1.7    |      0.4    |      setosa|


 <br/>

<p align="justify">The data frame is also checked for missing or null values and duplicate values. These values might skew our visualisation or lead to misleading reports. Since the dataframe is based on 'real world' data, duplicates are more commonly expected. A ratio between species was checked for imbalances and since there was no significant disproportion between species caused by duplicate results, these results were not excluded. Info() command is used to get details about the dataframe, such as the number of rows and column, if null values exist as well as the columns names and the types of data they contain. We have 4 numeric values and 1 non numeric value. The variables looking at length and width are floats, representing petal and sepal measurements, while species is a string variable. Within Python, Object is used to store string variables or if the column contains a mix of data types. <br/></p>

```python
iris_data[iris_data.duplicated()]
print(*iris_data.isna().any())
iris_data.info()
```

<p align="justify">The describe() command also provides statistical insight on the numeric type columns. Describe provides a summary of statistic calculations; showing that all 4 measures have the same count and sepal length has the largest mean value which would be expected based on the figure above. We know that sepal measurements are from a larger area of the flower but using the describe command confirms this since the min and max sepal measurements are larger than that of the petal measurements. The describe command also provides the std which is the amount of variation across the dataframe and the quantiles of the dataframe, which shows how the data is distributed between the minimum and maximum numbers.Describe can also be run on selected columns:  <br/></p>

```python
iris_data.describe()
iris_data[["sepal_length"]].describe()
```
### Visualization 
> #### *Scatter Plot*
<p align="justify">To better understand the dataset, different plots were used to analyse the comparison between various species based on sepal and petal measurements. Looking firstly at sepal length and width, the scatter plot shows that the Setosa spcies has a smaller sepal length but higher width while Virginica is the opposite having a larger sepal length then width. The Versicolor species lies in the middle between the two other species. From the scatter plot we can also tell that there is a high correlation between sepal lebth and weidth for Setosa flowers.In comparison, there is less correlation between the measures for both Vericolor and Virginica, where the data points are more spread out. The second scatter plot replaces sepal with petal data points and again there is a correlation between petal length and width for the Setosa flowers. There is also a slight correlation for Versicolor flowers though the data points aren't as densly populated as the Setosa flowers. From the scatter plots, there is not a large overlap of data points between Setosa flowers and the other species for petal measurements.  <br/></p>

```python
 sns.scatterplot(iris_data['sepal_length'],iris_data['sepal_width'],hue =iris_data['species'],s=50)
 ```
 
 <p align="center">
  <img src="https://github.com/megan1103/pands-project/blob/main/Comparison%20between%20various%20species%20via%20sepal.png" >
</p>
<br/> 

 <p align="center">
  <img src="https://github.com/megan1103/pands-project/blob/main/Comparison%20between%20various%20species%20via%20petal.png" >
</p>
<br/> 
 
 
> #### *Pair Plot*
<p align="justify">A pairplot shows the distribution and relationship between a number of variables at once instead of plotting them individually. Assigning hue="Species", adds mapping and changes the default histogram plot to a layered kernel density estimate. There is a high correlation between petal length and width across flower types. Petal length and width are also the most useful variables to distingush between various flower types. The relationship between flower type and measurements is distinctively different for Setosa flowers.The setosa flower type is linearly separable from the other flower types, although there is only slight overlapp between Virnica and Versicolor. Setosa is distinctly different from those of the other two species.  <br/></p>

```python
df2 = sns.pairplot(df,hue="Species")
```

 <p align="center">
  <img src="https://github.com/megan1103/pands-project/blob/main/pairplot.png" >
</p>
<br/> 

> #### *Correlation Plot*
<p align="justify">From the previous plots, a correlation between petal length and petal width. A correlation plot is used to futher valiate this claim. Pandas dataframe.corr() is used to find the pairwise correlation of all columns in the dataframe.
