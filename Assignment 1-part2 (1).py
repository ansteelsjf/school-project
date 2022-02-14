# -*- coding: utf-8 -*-
"""
Assignment 1, part 2: Data preprocessing. 
Instructions:
    This assignment can be completed in groups of 1-5 students
    Please read the comments to understand what is expected. 
    Some lines have already been completed. Only fill the blanks
    Please return by email to elugez@ubishops.ca the completed .py with the name as follows:
        CS405_A1_FirstLastName1_FirstLastName2_FirstLastName3.py if you a group of undergraduate students
        CS505_A1_FirstLastName1_FirstLastName2_FirstLastName3.py if you a group of graduate students
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Read the dataset located here 'https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data'
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data'
data = pd.read_csv(url)
data.columns = ['Sample code', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape',
                'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin',
                'Normal Nucleoli', 'Mitoses','Class']

# Drop the unnecessary "Sample Code" column  

data = data.drop(columns=["Sample code"])

# Visualize the first 5 rows of objects 
data.head(5)


# 1. Missing Values
# Missing values are encoded as '?'. Convert the '?' to NaN
data = data.replace('?',np.NaN)

# Compute the number (sum) of missing values in each column
print('Number of missing values:')
for col in data.columns:
    print('\t%s: %d' % (col,data[col].isna().sum()))
    
# Only the column 'Bare Nuclei' is missing values. Save that column into a new variable data2
data2 = data['Bare Nuclei']
# Impute the median value of that column to the NaN values 

data2 = data2.fillna(data2.median())
# Instead of replacing the missing values, discard the data points that contain missing values
data2 = data2.dropna(how='all')

# 2. Outliers 
# Drop the "Class" column

data2 = data.drop(['Class'],axis=1)
# Convert the column 'Bare Nuclei' into numeric values
data2['Bare Nuclei'] = pd.to_numeric(data2['Bare Nuclei'])

# Draw a boxplot to identify the columns in the table that contain outliers 
data2.boxplot(figsize=(20,3))

# The boxplots suggest that only 5 of the columns (Marginal Adhesion, Single Epithetial Cell Size, Bland Cromatin, Normal Nucleoli, and Mitoses) contain abnormally high values. 
# Find a method to discard the outliers (several lines can be entered)




# 3. Duplicate Data
# Check for duplicate instances.
dups = data.duplicated()
print('Number of duplicate rows = %d' % (dups.sum()))

# Drop the row duplicates
data2 = data.drop_duplicates(keep=False)

# 4. Sampling
# Randomly select 1% of the data without replacement
sample = data.sample(frac=0.01,replace=False,random_state=1)
sample

# Randomly select 1% of the data with replacement
sample = data.sample(frac=0.01,replace=True,random_state=1)
sample

# 5. Discretization
# Transform a continuous-valued attribute to a categorical attribute.

# Plot a 10-bin histogram of the attribute values 'Clump Thickness' distribution
data.hist(bin=10)
data['Clump Thickness'].plot

# Discretize the 'Clump Thickness' attribute into 4 bins of equal width.
bins = pd.cut(data['Clump Thickness'],bins=4)
bins.value_counts(sort=False)

# Discretize the 'Clump Thickness' attribute into 4 bins of equal frequency.
bins = pd.qcut(data['Clump Thickness'],q=4)
bins.value_counts(sort=False)