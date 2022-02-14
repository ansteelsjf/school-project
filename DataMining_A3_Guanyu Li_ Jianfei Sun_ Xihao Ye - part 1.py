# -*- coding: utf-8 -*-
"""
Assignment 3 - Part 1
"""

import pandas as pd
from scipy.cluster import hierarchy

# Import the data
data = pd.read_csv('D:/vertebrate.csv',header='infer') # (4 points)
# Check the data
data

# Single link (MIN) analysis
objectNames = data['Name']
Classifications = data['Class']
NumericalAttributes = data.drop(['Name','Class'],axis=1)
# Perform the single link analysis
min_analysis = hierarchy.linkage(pd.DataFrame(NumericalAttributes).to_numpy(), 'single') # (3 points)
# Visualize the results using a dendrogram
dn = hierarchy.dendrogram(min_analysis,labels=objectNames.tolist(),orientation='right') # (3 points)

# Complete Link (MAX) analysis 
# Perform the complete link analysis
max_analysis = hierarchy.linkage(pd.DataFrame(NumericalAttributes).to_numpy(), 'complete') # (3 points)
dn = hierarchy.dendrogram(max_analysis,labels=objectNames.tolist(),orientation='right') # (2 points)

# Group Average analysis
# Perform the group average analysis
average_analysis =hierarchy.linkage(pd.DataFrame(NumericalAttributes).to_numpy(), 'average') # (3 points)
dn = hierarchy.dendrogram(average_analysis,labels=objectNames.tolist(),orientation='right') # (2 points)
