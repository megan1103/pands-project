>> Author: Megan O'Donovan  
>> Date: 29/04/2022
##  2022 HDip in Computing in Data Analytics - Programming and Scripting


### Table of Contents
***[Introduction](#introduction)***<br>
***[Summary of Dataset](#summary-of-dataset)***
  <br>>***[Load the Data](#load-the-data)***
  <br>>***[Data Overview](#data-overview)***<br>
***[Analyse and Visualize the Data](#analyse-and-visualize-the-data)***
  <br>>***[Statistical Summary Tables](#statistical-summary-tables)***
  <br>>***[Histogram Plot](#histogram-plot)***
  <br>>***[Scatter Plot](#scatter-plot)***
  <br>>***[Pair Plot](#pair-plot)***
  <br>>***[Correlation Plot](#correlation-plot)***<br>
***[Conclusion](#conclusion)***<br>
***[References](#references)***<br>

## Introduction 
<p align="justify">
This ReadMe file contains an overview of my research carried out on the Fisher’s Iris dataset. This research project was part of my continuous assessment for the module Programming and Scripting. A description of the course and assignment can be found on the course homepage <em><a href=https://learnonline.gmit.ie/course/view.php?id=5057>here</a></em>. This ReadMe file provides a summary of background information on the Fishers’ Iris dataset and documentation of the Python programming code used for analytical research. Key aspects of the code used will be explained as well as detailed explanation of any resulting output. My python code can be found <em><a href=https://github.com/megan1103/pands-project/blob/main/analysis.py>here</a></em> or in my pands-project repository labeled <em>analysis.py</em> <br/> </p>

<p align="justify">The dataset was initially created as an example of linear analysis by British statistician and biologist Ronald Fisher. The dataset comprises of 50 flowers for each of the three species of iris. The species of iris are Setosa, Versicolor, or Virginica. Four features were measured from each sample, they are the length and the width of sepal and petal respectively, in centimetres. From this dataset, Fisher developed a linear model; distinguishing species based on the combination of those four features.   <br/> </p>
  
<p align="justify">Fisher’s Iris dataset is one of the most famous multivariate datasets used for testing various Machine Learning Algorithms. Classification of iris flowers is perhaps the best-known example in machine learning. The aim is to classify iris flowers among three species (Setosa, Versicolor, or Virginica) from sepals' and petals' length and width measurements. The below image shows the difference between a petal and sepal, when measuring width and length. It’s easy to appreciate how meticulous Fisher was in recording the measurements of 150 flowers.  <br/> </p>

<p align="centre">
  <img src="https://github.com/megan1103/pands-project/blob/main/Iris%20flowers%20in%20Fisher%20dataset.png" >
</p>
<br/> 


## Summary of Dataset 
>#### *Load the data*
<p align="justify">Before the dataset was loaded, python libraries were imported. These libraries allowed for visualisations to be created and queries performed. Abbreviated names were assigned to the libraries once imported, solely to save time. <br/> </p>

```python 
import numpy as np    
import pandas as pd  
import matplotlib.pyplot as plt 
import seaborn as sns
```

<p align="justify">Using python, there are two possible methods of loading the dataset. Python can query a csv using the URL or the csv can be downloaded and saved locally. Either method resulted in the dataset being uploaded, which was then loaded into a data frame using the panda library.  <br/> </p>
 
```python
csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
col_names = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Class']
iris_data =  pd.read_csv(csv_url, names = col_names)
```
 
```python
csv_file = 'C:/Users/odonovanm/Documents/iris dataset.csv'
iris_data =  pd.read_csv(csv_file)
```

>#### **Data Overview**
<p align="justify">In terms of research analysis, this is considered a small dataset. The data frame consists of 150 cases, each row of the table representing an iris flower; including its species and dimensions of its botanical parts, sepal and petal, in centimetres. There are the same number of Virginica, Setosa, and Versicolor samples. <br/> </p>

```python
names(iris_data)
class(iris_data)
dim(iris_data)
```

<p align="justify">Due to the dataset being small, it was easy to check if the file was loaded to the data frame correctly. Python <em>head()</em> and <em>tail()</em>, output the first and last rows of the data frame, which allowed for easy comparison with the original csv. The data was loaded in table format, all the measurements are in centimetres <em>(cm)</em>. The <em>head()</em> preview showed how the data frame was arranged and if column names needed to be changed. The command <em>tail()</em> was particularly useful as most issues with a dataset failing to load correctly, occurs at the end of the dataset.   <br/> </p>

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

### Analyse and Visualize the Data
> #### *Statistical Summary Tables*
<p align="justify"> <em>Info()</em> command was used to obtain details about the data frame, such as the number of rows and column, if null values exist, columns names and the types of data. The dataset had 4 numeric values and 1 non-numeric value. The variables looking at length and width were floats, representing petal and sepal measurements, while species was a string variable. Within Python, <em>Object</em> describes a stored string variable or if the column contains a mix of data types. <br/></p>

```python
iris_data.info()
```

 <br/>

| Data  | Column | Count   | Type |
| ------------- | ------------- | -------- | -------- | 
| 0  | Sepal Length | 150 non-null   | float64|
| 1 |  Sepal Width  | 150 non-null  |  float64|
| 2  | Petal Length | 150 non-null  |  float64|
| 3|   Petal Width  | 150 non-null  |  float64|
| 4  | Species     |  150 non-null  |  object|


 <br/>


<p align="justify">The <em>describe()</em> command also provided statistical insight on the numeric type columns.<em>Describe</em> provided summary of statistic calculations; showing that all 4 measures had the same count and sepal length had the largest mean value which would be expected, based on the flower type image above. We know that sepal measurements are from a larger area of the flower but using the <em>describe()</em> command confirmed this, since the min and max sepal measurements were larger than that of the petal measurements. The <em>describe()</em> command also provides the standard deviation, which was amount of variation across the data frame. The quantiles of the data frame were also given, showing the distribution between the minimum and maximum values. A large proportion of sepal and petal length data points were found within the upper quantile range. <em>Describe()</em> command was also applied to selected columns and grouped by species.  <br/></p>

```python
iris_data.describe()
```
 <br/>

|   | Sepal Length     | Sepal Width      | Petal Length     | Petal Width     |
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
 <br/>
 
|Name: Sepal Length   | dtype: float64     |
| ------------- | ------------- |
|count |   150.000000 |
|mean  |     5.843333 |
|std   |     0.828066 |
|min   |     4.300000 |
|25%   |     5.100000 |
|50%   |     5.800000 |
|75%   |     6.400000 |
|max   |     7.900000 |

 <br/>
  
```python
print(iris.groupby(["Species"])[["Sepal Length"]].describe())
print(iris.groupby(["Species"])[["Sepal Width"]].describe())
print(iris.groupby(["Species"])[["Petal Length"]].describe())
print(iris.groupby(["Species"])[["Petal Width"]].describe())
```
 <br/>
 
**Sepal Length**
   | species     | count |    mean    |     std   | min   |   25%  |  50%  |  75% |   max |
| ------------- | ------------- | -------- | -------- | -------- |------------- | -------- | -------- | -------- |
| setosa        |       50.0   | 5.006   | 0.352490  |  4.3  |  4.800  |  5.0   | 5.2  |  5.8 |
| versicolor       |    50.0  |  5.936  |   0.516171  |  4.9  |  5.600   | 5.9   | 6.3  |  7.0 |
| virginica       |     50.0  |  6.588  |  0.635880  |  4.9   | 6.225 |   6.5  |  6.9   | 7.9 |

**Sepal Width**
   | species     | count |    mean    |     std   | min   |   25%  |  50%  |  75% |   max |
| ------------- | ------------- | -------- | -------- | -------- |------------- | -------- | -------- | -------- |
| setosa          |    50.0  |  3.418  |  0.381024  |  2.3  |  3.125   | 3.4  |  3.675   | 4.4 |
| versicolor      |    50.0  |  2.770   | 0.313798   | 2.0   | 2.525   | 2.8   | 3.000   | 3.4 |
| virginica      |     50.0   | 2.974  |  0.322497   | 2.2   | 2.800   | 3.0  |  3.175   | 3.8 |
          
**Petal Length**
   | species     | count |    mean    |     std   | min   |   25%  |  50%  |  75% |   max |
| ------------- | ------------- | -------- | -------- | -------- |------------- | -------- | -------- | -------- |
| setosa             |  50.0  |  1.464  |  0.173511  |  1.0 |   1.4  |  1.50  |  1.575  |  1.9 |
| versicolor         |  50.0   | 4.260  |  0.469911   | 3.0   | 4.0   | 4.35   | 4.600   | 5.1 |
| virginica          |  50.0   | 5.552  |  0.551895  |  4.5 |   5.1  |  5.55  |  5.875  |  6.9 |
           
**Petal Width**
   | species     | count |    mean    |     std   | min   |   25%  |  50%  |  75% |   max |
| ------------- | ------------- | -------- | -------- | -------- |------------- | -------- | -------- | -------- |
| setosa             | 50.0   | 0.244   | 0.107210   | 0.1   | 0.2   | 0.2   | 0.3   | 0.6 |
| versicolor        |  50.0   | 1.326  |  0.197753   | 1.0  |  1.2  |  1.3  |  1.5  |  1.8 |
| virginica        |   50.0   | 2.026   | 0.274650   | 1.4   | 1.8   | 2.0   | 2.3   | 2.5 |


 <br/>
 

> #### *Histogram Plot*
<p align="justify"> A histogram visualised the data point distribution and frequency for each feature. The petal-length, petal-width, and sepal-length had a probability distributes with a single peak. While Sepal Width had an almost normal distribution having symmetrical sides around its centre.
   <br/></p>
   
 <p align="centre">
   <img src="https://github.com/megan1103/pands-project/blob/main/histogram.png" >
</p>
<br/> 

> #### *Scatter Plot*
<p align="justify">To better understand the dataset, different plots were used to analyse the comparison between various species based on sepal and petal measurements. Looking firstly at sepal length and width, the scatter plot shows that the Setosa species had a smaller sepal length but higher width while Virginica is the opposite having a larger sepal length then width. The Versicolor species lies in the middle between the two other species. From the scatter plot we can also tell that there was a high correlation between sepal length and width for Setosa flowers. In comparison, there was less correlation between the measures for both Vericolor and Virginica, where the data points were more spread out. The second scatter plot replaces sepal with petal data points and again there was a correlation between petal length and width for the Setosa flowers. There was also a slight correlation for Versicolor flowers, though the data points weren't as densely populated as the Setosa flowers. From the scatter plot, there was not a large overlap of data points between Setosa flowers and the other species for petal measurements.  <br/></p>

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
<p align="justify">The seaborn library creates the pair plot which showed the distribution and relationship between several variables at once instead of plotting them individually. Assigning <em>hue="Species"</em>, added mapping and changed the default histogram plot to a layered kernel density estimate. There was a high correlation between petal length and width across flower types. Petal length and width were also the most useful variables to distinguish between various flower types. The relationship between flower type and measurements were distinctively different for setosa flowers. The setosa flower type was linearly separable from the other flower types, although there was only slight overlap between Virnica and Versicolor. Setosa was distinctly different from those of the other two species.  <br/></p>

```python
df2 = sns.pairplot(iris_data,hue="Species")
```

 <p align="centre">
  <img src="https://github.com/megan1103/pands-project/blob/main/pairplot.png" >
</p>
<br/> 

> #### *Correlation Plot*
<p align="justify">From the previous plots, a known correlation between petal length and petal width exists. A correlation plot was used to further validate this claim. Pandas <em>.corr()</em> was used to find the pairwise correlation of all columns in the data frame. Using python, the correlation was examined via a summary table and a heat chart, the difference between either results was based solely on visualisation. Seaborn package was used to create a heatmap, using <em>annot=True</em> to include the correlation values. The correlation table confirmed a high correlation between petal length and petal width. There was also a slight correlation between sepal length and both petal length and petal width.     <br/> </p>

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
 
### Conclusion
<p align="justify">The Iris dataset is often used as a test case to examine classification within machine learning. For this project, I used the Iris dataset to examine the overall dataset and the relationship between Iris flower types across flower measurements. The iris dataset contains three classes of flowers, Versicolor, Setosa, Virginica, and each class contains 4 features, ‘Sepal length’, ‘Sepal width’, ‘Petal length’, ‘Petal width’. <br/> </p> 

<p align="justify">The standard deviation in the petal lengths shows the highest variability of the four measurements at 1.76 while the standard deviations of the petal width is approx 0.43. By grouping the decribe command by species, showed that Virginica had the highest standard deviation across petal measurements and sepal length. The standard deviations also showed that the petal length measurements of the Iris Setosa were much less variable than that of the other two species. The measurements of the petal width has the lowest average measurements. <br/> </p> 
<p align="justify">When sparated by species, setosa flowers were considerably lower then the other flower types due to the minimun petal width being 0.1 cm and max width being 0.6cm which is considerably smaller compared to virginica min and max petal widths being 1.4 cm and 2.5cm. However, setosa flowers had the largest min and max widths for sepal measurements. The upper quartile for petal width ranged between 0.3 cm for setosa flowers and 2.3 for virginica flowers while the upper quartile for petal length ranged between 1.5cm and 5.8cm for Setosa and Virginica flowers respectivitly.  <br/> </p>

<p align="justify"> The histogram plot shows that sepal width is the only feature with a normal distribution. From the plot, the distribution is symetric on either side of the central point. The scatter plot showed quite a strong positive relationship overall between the petal length and petal width measurements.  The relationship between petal measurements appeared almost linear. This was not the case for sepal measurements. <br/> </p>

<p align="justify"> From the seaborn pair plot, the visualization showed that the Setosa flowers was well separated from the other flower types. The plot also shows that Setosa flowers are the shortest, while Versicolor flowers are the largest. There was not a large overlap of data points between Setosa flowers and the other species based on petal and sepal feautures.<br/> </p>

<p align="justify"> Both correlation plots showed that the highest correlation existed between petal length and width. A slightly high correlation also existed between sepal length and petal features. <br/> </p>
 
 <br/>
 
### References
<br /> - *[1] :* https://www.programiz.com/python-programming/methods/built-in/list
<br /> - *[2] :* https://pandas.pydata.org
<br /> - *[3] :* https://matplotlib.org
<br /> - *[4] :* https://seaborn.pydata.org
<br /> - *[5] :* https://pandas.pydata.org
<br /> - *[6] :* https://en.wikipedia.org/ 
<br /> - *[7] :* https://www.w3schools.com/python/
<br /> - *[8] :* https://www.w3schools.com/html/ 
<br /> - *[9] :* https://www.datacamp.com/community/tutorials/introduction-machine-learning-python
<br /> - *[10] :* http://www.lac.inpe.br/~rafael.santos/Docs/CAP394/WholeStory-Iris.html
<br /> - *[11] :* http://rstudio-pubs-static.s3.amazonaws.com/450733_9a472ce9632f4ffbb2d6175aaaee5be6.html
<br /> - *[12] :* https://www.earthdatascience.org/courses/intro-to-earth-data-science/scientific-data-structures-python/pandas-dataframes/run-calculations-summary-statistics-pandas-dataframes/
