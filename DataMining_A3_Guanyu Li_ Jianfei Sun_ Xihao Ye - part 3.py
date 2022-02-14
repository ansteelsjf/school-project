# -*- coding: utf-8 -*-
"""
Assignment 3 - part 3

Spectral Clustering Analysis
"""

# Import packages
import pandas as pd # (2 points)
import matplotlib.pyplot as plt # (2 points)
from sklearn import cluster # (2 points)

# Import the data '2d_data.txt' and 'elliptical.txt'
data2D = pd.read_csv('D:/2d_data.txt', delimiter=' ', names=['x','y']) # (2 points)
dataElliptical = pd.read_csv('D:/elliptical.txt', delimiter=' ', names=['x','y']) # (2 points)

# Create two scatter subplots of both datasets (1 figure only)
fig, (ax1,ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10,4)) # (2 points)
data2D.plot(x='x',y='y',ax=ax1) # (2 points)
dataElliptical.plot(x='x',y='y',ax=ax2) # (2 points)

# Perform spectral clustering on data2D
spectral_data2D = cluster.SpectralClustering(n_clusters=2, affinity='rbf',gamma=3000) # (4 points)
spectral_data2D = cluster.KMeans(n_clusters = 2,random_state=0).fit(data2D) #(4 points)
# Add clusters labels to data2D:
# 1. convert labels to pandas dataframe
labels_data2D = pd.DataFrame(spectral_data2D.labels_,columns=['Cluster ID']) # (2 points)
# 2. concatenate labels with data2D
result_data2D = pd.concat((data2D,labels_data2D), axis=1) # (2 points)

# Perform spectral clustering on dataElliptical
spectral_dataElliptical = cluster.SpectralClustering(n_clusters=2,affinity='rbf',gamma=3000) # (4 points)
spectral_dataElliptical = cluster.KMeans(n_clusters = 2,random_state=0).fit(dataElliptical) # (4 points)
# Add clusters labels to data2D:
# 1. convert labels to pandas dataframe
labels_dataElliptical = pd.DataFrame(spectral_dataElliptical.labels_,columns=['Cluster ID']) # (2 points)
# 2. concatenate labels with dataElliptical
result_dataElliptical =pd.concat((dataElliptical, labels_dataElliptical), axis=1) # (2 points)

# Create scatter plots of both clustered datasets:
# 1. organize both plots in a single figure
fig, (ax1,ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12,5)) # (2 points)
# 2. create scatter plot of the clusters of data2D in ax1
result_data2D.plot.scatter(x='x',y='y',c='Cluster ID',colormap='jet',ax=ax1) # (2 points)
# 3. add title to this first scatter plot
ax1.set_title('Spectral Clustering') # (2 points)
# 4. create scatter plot of the clusters of dataElliptical in ax2
result_dataElliptical.plot.scatter(x='x',y='y',c='Cluster ID',colormap='jet',ax=ax2) # (2 points)
# 5. add title to this first scatter plot
ax2.set_title('Spectral Clustering') # (2 points)