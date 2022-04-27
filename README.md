>> Author: Megan O'Donovan  
>> Date: 29/04/2022
##  Programming and Scripting 


### Table of Contents
**[Introduction](#introduction)**<br>

**[Summary of Dataset](#summary-of-dataset)**<br>
>**[Description](#description)**<br>
>**[Data Overview](#data-overview)**<br>

**[Results](#results)**<br>
>**[Histogram Plot](#histogram-plot)**<br>
>**[Scatter Plot](#scatter-plot)**<br>
>**[Pair Plot](#pair-plot)**<br>
>**[Correlation Plot](#correlation-plot)**<br>

### Introduction 
<p align="justify">
This ReadMe file contains an overview of my research carried out on the Fisher’s Iris data set. The research project is part of my continuous assessment for the module Programming and Scripting. A description of the course and assignment can be found on the course homepage <em>here</em>. The ReadMe file will provide a summary of background information on the Fishers’ Iris data set and documentation of the Python programming code used for analytical research. Key aspects of the code used will be explained as well as detailed explanation of the resulting output. <br/> </p>

### Summary of Dataset 
>#### *Description* 
<p align="justify">The dataset was initially created as an example of linear analysis by British statistician and biologist Ronald Fisher. The dataset comprises of 50 flowers for each of the three species of iris. The species are Iris Setosa, Versicolor, or Virginica. Four features were measured from each sample, they are the length and the width of sepal and petal respectively, in centimetres. From this dataset, Fisher developed a linear model; distinguishing species based on the combination of those four features.   <br/> </p>
  
<p align="justify">Fisher’s Iris dataset is one of the most famous multivariate datasets used for testing various Machine Learning Algorithms. Classification of iris flowers is perhaps the best-known example in machine learning. The aim is to classify iris flowers among three species (Setosa, Versicolor, or Virginica) from sepals' and petals' length and width measurements. The below image shows the difference between a petal and sepal, when measuring width and length. It’s easy to appreciate how meticulous Fisher was in recording the measurements of 150 flowers.  <br/> </p>

<p align="centre">
  <img src="https://github.com/megan1103/pands-project/blob/main/Iris%20flowers%20in%20Fisher%20dataset.png" >
</p>
<br/> 


<p align="justify">Before the dataset was loaded, python libraries were imported. These libraries allowed for visualisations to be created and queries performed. Abbreviated names are assigned to the libraries once imported, solely to save time. <br/> </p>

```python 
import numpy as np    
import pandas as pd  
import matplotlib.pyplot as plt 
import seaborn as sns
```

<p align="justify">Using python, there are two possible ways of loading the dataset. Python can query a csv using the URL or the csv can be downloaded and saved locally. Either of these methods result in the dataset being uploaded, which was then loaded into a data frame using the panda library.  <br/> </p>
 
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
<p align="justify">In terms of research analysis, this is considered a small dataset. The data frame consists of 150 cases, each row of the table representing an iris flower; including its species and dimensions of its botanical parts, sepal and petal, in centimetres. There are the same number of Virginica, Setosa, and Versicolor samples. <br/> </p>

```python
names(iris_data)
class(iris_data)
dim(iris_data)
```

<p align="justify">Due to the dataset being small, it was easy to check if the file was loaded to the data frame correctly. Python <em>head()</em> and <em>tail()</em>, outputs the first and last rows of the data frame, which allowed for easy comparison with the original csv. The data was loaded in table format, all the measurements are in centimetres <em>(cm)</em> and in the <em>head()</em> preview showed how it was arranged and if column names needed to be changed. The command <em>tail()</em> was particularly useful as most issues with a dataset failing to load, occurs at the end of the dataset.   <br/> </p>

```python
head(iris_data)
tail(iris_data)
iris_data = iris_data.rename({'sepal_length': 'Sepal-Length', 'sepal_width': 'Sepal-Width',
      'petal_length': 'Petal-Length', 'petal_width': 'Petal-Width', 'species': 'Species'}, axis=1)
```
 <br/>

| Sepal_Length     | Sepal_Width      | Petal_Length     | Petal_Width     |Species   |
| ------------- | ------------- | -------- | -------- | -------- |
|      5.1    |      3.5    |      1.4    |      0.2    |      setosa|
|      4.9    |      3.0    |      1.4    |      0.2    |      setosa|
|      4.7    |      3.2    |      1.3    |      0.2    |      setosa|
|      4.6    |      3.1    |      1.5    |      0.2    |      setosa|
|      5.0    |      3.6    |      1.4    |      0.2    |      setosa|
|      5.4    |      3.9    |      1.7    |      0.4    |      setosa|


 <br/>

<p align="justify">The data frame was also checked for missing or null values and duplicate values. These values might have skewed our visualisations or led to misleading reports. Since the data frame was based on 'real world' data, duplicates are more commonly expected. A ratio between species was checked for imbalances and since there was no significant disproportion between species caused by duplicate results, these results were not excluded. 

```python
iris_data[iris_data.duplicated()]
print(*iris_data.isna().any())
```

### Analysis and Results
> #### *Satistical Summary Tables*
<p align="justify"> <em>Info()</em> command is used to get details about the data frame, such as the number of rows and column, if null values exist, columns names and the types of data. The dataset has 4 numeric values and 1 non-numeric value. The variables looking at length and width are floats, representing petal and sepal measurements, while species is a string variable. Within Python, Object is used to store string variables or if the column contains a mix of data types. <br/></p>

```python
iris_data.info()
```

 <br/>

| RangeIndex: | 150 entries, 0 to 149 |
| Data columns | (total 5 columns): |
| ------------- | ------------- | -------- | -------- | 
| 0  | Sepal Length | 150 non-null   | float64|
| 1 |  Sepal Width  | 150 non-null  |  float64|
| 2  | Petal Length | 150 non-null  |  float64|
| 3|   Petal Width  | 150 non-null  |  float64|
| 4  | Species     |  150 non-null  |  object|
|dtypes: float64(4), object(1) |
|memory usage: 6.0+ KB|
|None|


 <br/>


<p align="justify">The <em>describe()</em> command also provided statistical insight on the numeric type columns.<em>Describe</em> provides a summary of statistic calculations; showing that all 4 measures have the same count and sepal length has the largest mean value which would be expected based on the figure above. We know that sepal measurements are from a larger area of the flower but using the describe command confirmed this since the min and max sepal measurements are larger than that of the petal measurements. The <em>describe()</em> command also provides the standard deviation, amount of variation across the data frame. The quantiles of the data frame are also given, showing the distribution between the minimum and maximum values. <em>Describe()</em> can also be run on selected columns:  <br/></p>

```python
iris_data.describe()
```
 <br/>

|   | Sepal_Length     | Sepal_Width      | Petal_Length     | Petal_Width     |
| ------------- | ------------- | -------- | -------- | -------- |
| count |   150.000000  | 150.000000  |  150.000000  | 150.000000 |
| mean     |  5.843333   |  3.054000      | 3.758667    | 1.198667 |
| std      |  0.828066     | 0.433594     | 1.764420     | 0.763161 | 
| min      |  4.300000    | 2.000000     | 1.000000     | 0.100000 |
| 25%     |   5.100000    | 2.800000     | 1.600000     | 0.300000 |
| 50%      |  5.800000    | 3.000000     | 4.350000     | 1.300000 |
| 75%       | 6.400000    | 3.300000     | 5.100000     | 1.800000 |
| max       | 7.900000    | 4.400000     | 6.900000    | 2.500000 |

 <br/>
 
```python

iris_data[["Sepal_Length"]].describe()
```

> #### *Histogram Plot*
<p align="justify"> A histogram visualises the data point distribution and frequency for one feature. The petal-length, petal-width, and sepal-length have probability distributes with a single peak. While Sepal Width has an almost normal distribution having symmetrical sides around its centre.
   <br/></p>
   
 <p align="centre">
   <img src="https://github.com/megan1103/pands-project/blob/main/histogram.png" >
</p>
<br/> 

> #### *Scatter Plot*
<p align="justify">To better understand the dataset, different plots were used to analyse the comparison between various species based on sepal and petal measurements. Looking firstly at sepal length and width, the scatter plot shows that the Setosa species has a smaller sepal length but higher width while Virginica is the opposite having a larger sepal length then width. The Versicolor species lies in the middle between the two other species. From the scatter plot we can also tell that there is a high correlation between sepal length and width for Setosa flowers. In comparison, there is less correlation between the measures for both Vericolor and Virginica, where the data points are more spread out. The second scatter plot replaces sepal with petal data points and again there is a correlation between petal length and width for the Setosa flowers. There is also a slight correlation for Versicolor flowers though the data points aren't as densely populated as the Setosa flowers. From the scatter plots, there is not a large overlap of data points between Setosa flowers and the other species for petal measurements.  <br/></p>

```python
 sns.scatterplot(iris_data['Sepal_Length'],iris_data['Sepal_Width'],hue =iris_data['Species'],s=50)
 ```
 
 <p align="centre">
  <img src="https://github.com/megan1103/pands-project/blob/main/Comparison%20between%20various%20species%20via%20sepal.png" >
</p>
<br/> 


```python
 sns.scatterplot(iris_data['Petal_Length'],iris_data['Petal_Width'],hue =iris_data['Species'],s=50)
 ```
 

 <p align="centre">
  <img src="https://github.com/megan1103/pands-project/blob/main/Comparison%20between%20various%20species%20via%20petal.png" >
</p>
<br/> 
 
 
> #### *Pair Plot*
<p align="justify">The seaborn library creates the pair plot which shows the distribution and relationship between several variables at once instead of plotting them individually. Assigning <em>hue="Species"</em>, adds mapping and changes the default histogram plot to a layered kernel density estimate. There is a high correlation between petal length and width across flower types. Petal length and width are also the most useful variables to distinguish between various flower types. The relationship between flower type and measurements is distinctively different for Setosa flowers. The setosa flower type is linearly separable from the other flower types, although there is only slight overlap between Virnica and Versicolor. Setosa is distinctly different from those of the other two species.  <br/></p>

```python
df2 = sns.pairplot(iris_data,hue="Species")
```

 <p align="centre">
  <img src="https://github.com/megan1103/pands-project/blob/main/pairplot.png" >
</p>
<br/> 

> #### *Correlation Plot*
<p align="justify">From the previous plots, a known correlation between petal length and petal width exists. A correlation plot is used to further validate this claim. Pandas <em>.corr()</em> is used to find the pairwise correlation of all columns in the data frame. Using python, a correlation can be created either as a table or as a heat chart, the difference between either result is based solely on visualisation. Seaborn package is used to create a heatmap, using <em>annot=True</em> to include the correlation values. The correlation table confirms a high correlation between petal length and petal width. There is also a slight correlation between sepal length and both petal length and petal width.     <br/> </p>

```python
iris_data.corr()
sns.heatmap(iris_data.corr(),  linecolor = 'white', linewidths = 1,annot=True) 
```

 <br/>


|      | Sepal_Length     | Sepal_Width      | Petal_Length     | Petal_Width     |
| ------------- | ------------- | -------- | -------- | -------- |
|      Sepal-Length    |      1.000000    |      -0.109369    |      0.871754    |      0.817954|
|      Sepal-Width    |      -0.109369    |      1.000000    |      -0.420516    |      -0.356544|
|      Petal-Length    |      0.871754    |      -0.420516    |      1.000000    |      0.962757|
|      Petal-Width    |      0.817954    |      -0.356544    |      0.962757    |      1.000000|


 <br/>
