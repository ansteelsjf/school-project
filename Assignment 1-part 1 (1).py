# -*- coding: utf-8 -*-
"""
Assignment 1. 
Instructions:
    This assignment can be completed in groups of 1-5 students
    Please read the comments to understand what is expected. 
    Some lines have already been completed. Only fill the blanks "___________________"
    Please return by email to elugez@ubishops.ca the completed .py with the name as follows:
        CS405_A1_FirstLastName1_FirstLastName2_FirstLastName3.py if you a group of undergraduate students
        CS505_A1_FirstLastName1_FirstLastName2_FirstLastName3.py if you a group of graduate students
"""

#  Import the required libraries


import pandas as pd
from pandas.api.types import is_numeric_dtype
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates

url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
data = pd.read_csv(url)
# Read the dataset from here 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'


# Assign new headers to the dataset 
data.columns = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class']

# Visualize the first 5 rows of objects 
data.head(5)



# Calculate the mean, standard deviation, minimum, and maximum values of each quantitative attribute
for col in data.columns:
    if is_numeric_dtype(data[col]):
        print('%s:' % (col)) # Prints the name of the column
        print( '\t Mean = %.2f'%data[col].mean()) # Prints the mean of the column
        print('\t Standard deviation = %.2f' % data[col].std()) # Prints the standard deviation of the column
        print('\t Minimum = %.2f' % data[col].min()) # Prints the minimum value in the column
        print('\t Maximum = %.2f' % data[col].max()) # Prints the maximum value in the column
        
# Count the frequency of the distinct values in the qualitative attribute "class"



data.apply(pd.value_counts)


a=pd.Series(data.iloc[:,0])
a.value_counts()
b=pd.Series(data.iloc[:,1])
b.value_counts()


pd.value_counts(data.iloc[:,1].values.flatten())
# Display the summary of the previous measures in a table using the describe() function. 
data.describe(include='all')
 
# Compute the covariance  between pairs of attributes

print('Covariance:')
data.cov()

# Compute the correlation between pairs of attributes
print('Correlation:')
data.corr()

# Data Visualization
# The goal is to display the information in a graphic or tabular format, in order to visualize the characteristics 
# and relationships among data items.

# 1. Display the histogram for the "sepal length" attribute using 8 bins
hist = data.hist(bins=8)

# 2. Display the data distribution for each attribute using a boxplot
boxplot = data.boxplot

# 3. Display the joint distribution for each pair of attributes using a scatter plot
fig, axes = plt.subplots(3, 2, figsize=(12,12))
index = 0
for i in range(3):
    for j in range(i+1,4):
        ax1 = int(index/2)
        ax2 = index % 2
        axes[ax1][ax2].scatter(data[data.columns[i]],data[data.columns[j]],color='red')
        axes[ax1][ax2].set_xlabel(data.columns[i])
        axes[ax1][ax2].set_ylabel(data.columns[j])
        index = index + 1
        
# 4. Display all the data points on the same plot using parallel coordinates
pd.plotting.parallel_coordinates(
    data, 'class', color=('#556270', '#4ECDC4', '#C7F464')
)
