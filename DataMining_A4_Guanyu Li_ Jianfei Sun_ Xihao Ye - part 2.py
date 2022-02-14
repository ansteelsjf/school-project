# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 18:41:50 2020

@author: elugez
"""

# -*- coding: utf-8 -*-
"""
A4-Part 2
"""

import numpy as np #(2 points)
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split #(2 points)
from sklearn import tree #(2 points)
from sklearn.metrics import accuracy_score #(2 points)

# Load the data (Y is the class labels of X)
X = np.load('D://Xdata.npy')  #(2 points)
Y = np.load('D://Ydata.npy') #(2 points)

# Split the training and test data as follows: 80% of the data for training and 20% for testing
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.8, random_state=1)  #(7 points)

# Test the fit of different decision tree depths 
# Use the range function to create different depths options (1 to 50(or 49)) for the decision trees
depthOptions = range(1,50)#(5 points)

# Prepare to save the training and testing accuracies as a function of the different decision tree depth options
trainAccuracy = np.zeros(len(depthOptions))
testAccuracy = np.zeros(len(depthOptions))

index = 0
# Iterate through the tree depth options
for depth in depthOptions: #(4 points)
    # Decision tree creation
    cltree = tree.DecisionTreeClassifier(max_depth=depth) #(4 points)
    # Decision tree training
    cltree = cltree.fit(X_train, Y_train) #(4 points)
    # Training error
    Y_predTrain = cltree.predict(X_train) #(4 points)
    # Testing error
    Y_predTest = cltree.predict(X_test) #(3 points)
    # Training accuracy
    trainAccuracy[index] = accuracy_score(Y_train, Y_predTrain) #(4 points)
    # Testing accuracy
    testAccuracy[index] = accuracy_score(Y_test, Y_predTest) #(3 points)
    index += 1
    
# Plot of training and test accuracies    
plt.plot(depthOptions,trainAccuracy,'rv-',depthOptions,testAccuracy,'bo--')
plt.legend(['Training Accuracy','Test Accuracy'])
plt.xlabel('Tree Depth')
plt.ylabel('Classifier Accuracy')

# Complete this sentence:
# Model overfitting happens when the tree depth is approximately greater than _________________ #(6 points)