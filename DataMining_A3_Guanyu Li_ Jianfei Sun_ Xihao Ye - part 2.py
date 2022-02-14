# -*- coding: utf-8 -*-
"""
Assignment 3 - part 2

Density-Based analysis
Identify high-density clusters separated by regions of low density. 
In the populqr DBScan, data points are classified into 3 types:
     core points, border points, and noise points
Classification is applied as a function of two parameters: 
     the radius of the neighborhood size (eps) and the minimum number of points in the neighborhood (minpts).
"""
    
import pandas as pd

from sklearn.cluster import DBSCAN

# Import the data 'chameleon.data' using the pandas read_csv function
data = pd.read_csv('D:/chameleon.data', delimiter=' ', names=['x','y']) # (4 points)
# Create a scatter plot of the data (and check it)
data.plot.scatter(x='x',y='y')  # (3 points)

# Apply DBScan: eps set to 15.5 and minpts set to 5. 
DBScanAnalysis = DBSCAN(eps=15.5,min_samples=5).fit(data) # (10 points)
# Concatenate data with cluster classification:
# 1. Convert labels as a pandas dataframe
clustersLabels = pd.DataFrame(DBScanAnalysis.labels_,columns=['ClusterLable']) # (4 points)
# 2. Concatenate the two dataframes data and clustersLabels (hint: concatenation along the column axis is axis = 1)
result = pd.concat((data,clustersLabels), axis=1) # (4 points)

# Create a scatter plot of the data: 
# each point with coordinates x and y is represented as a dot; use the 'Cluster ID' to color the dot based on their cluster ID 
result.plot.scatter(x='x',y='y',c='ClusterLable', colormap='jet') # (5 points)
