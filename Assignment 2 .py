# -*- coding: utf-8 -*-
"""
Assignment 2
"""

import pandas as pd
from sklearn import cluster
import numpy as np
import matplotlib.pyplot as plt

# Create a dataset
movieRatings = [['james',5,5,2,1],['margaret',4,5,3,2],['brandon',4,4,4,3],['linda',2,2,4,5],['liam',1,2,3,4],['harper',2,1,5,5]]
columnsTitles = ['user','Titanic','La La Land','The Purge','A Quiet Place']
moviesDataset = pd.DataFrame(movieRatings,columns=columnsTitles)
# Visulize the dataset
moviesDataset

# To perform a k-means analysis on the dataset, extract only the numerical attributes: remove the "user" attribute 
data = moviesDataset.drop('user',axis=1)


# Suppose you want to determine the number of clusters k in the initial data 'data'
# Apply k-means with a varying number of clusters k and compute the corresponding sum of squared errors (SSE) 
k = range(1,6) #(10 points)
SSE = []
for clusterNumber in k:
    k_means_analysis = cluster.KMeans(n_clusters=clusterNumber) #(10 points)
    k_means_analysis.fit(data) #(10 points)
    SSE.append(k_means_analysis.inertia_)

#  Plot to find the SSE vs the Number of Cluster to visually find the "elbow" that estimates the number of clusters
plt.plot(k, SSE)
plt.xlabel('Number of Clusters')
plt.ylabel('SSE')

# Look at the plot and determine the number of clusters k (value of the "elbow" as explained in lecture)
k = 2 #(10 points)

# Using k, apply k-means
k_means = cluster.KMeans(n_clusters=k, max_iter=50, random_state=1) #(2 points)
# Compute k-means clustering
k_means.fit(data) #(2 points)
# Save in variable labels the labels of each points
labels = k_means.labels_
# Display the assignments of each users to a cluster 
pd.DataFrame(labels, index=moviesDataset.user, columns=['Cluster ID'])

# Display the cluster_centers_ for each clusters
centroids = k_means.cluster_centers_ #(10 points)
pd.DataFrame(centroids,columns=data.columns)
# You should observe that clusters have higher ratings for their respective type of movies compared to the other types movies.


# Now suppose we are provided with new users
# These are the new users' firstnames
newUsersNames = np.array(['peter','kourtney','lisa','terry','bob']).reshape(-1,1)
# These are the new users' movies ratings
newUsersRatings = np.array([[4,5,1,2],[3,2,4,4],[2,3,4,1],[3,2,3,3],[5,4,1,4]])

# Determine their cluster assignment so that it is consistent with the training set: predict the closest cluster each new user belongs to.
labels = k_means.predict(newUsersRatings) #(10 points)

# We want to visualize the data. In turn, we want to concatenate 'labels' with 'newUsersNames' and 'newUsersRatings'.
# However, 'labels' does not have the proper size to be concatenated with newUsersNames and newUsersRatings
# Give a new shape to the labels array without changing its data by making sure the labels are only a single column. The number of lines needs to be inferred automatically
labels = labels.reshape(-1,1) #(6 points)
# Concatenate the data
newUsersAnalysis = np.array((newUsersNames, newUsersRatings, labels), axis=1) #(4 points)
# The columns are not labelled. To label them properly, it is easier to do so with a pandas dataframe.
# The columns' labels should exactly be the same as in columnsTitles + an extra one at the end for the Cluster ID.
# In turn, append Cluster ID at the end of columnsTitles
columnsTitles.append('Cluster ID') #(6 points)
# Using a pandas dataframe, label the columns newUsersAnalysis using columnsTitles.
newUsersAnalysis = pd.DataFrame(np.concatenate(newUsersAnalysis, newUsersNames, labels)) #(6 points)
# Display the assignments of each users to a cluster 
newUsersAnalysis

