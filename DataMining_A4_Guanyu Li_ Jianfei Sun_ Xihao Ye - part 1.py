# -*- coding: utf-8 -*-
"""
A4-Part 1
"""
# Import the packages
import pandas as pd
from sklearn import tree #(2 points)
from sklearn.metrics import accuracy_score #(2 points)

# Read the vertebrate.csv data
data = pd.read_csv('D:/vertebrate.csv',header='infer') #(2 points)
# Visualize the data and notice that each vertebrate is classified into one of 5 classes
data

# The number of records is limited. Convert (hint: 'replace') the data into a binary classification: mammals versus non-mammals
data['Class'] = data['Class'].replace(['amphibians','birds','fishes','reptiles'],'non-mammals') #(6 points)
# Visualize the data
data

# Classification using a decision tree
# Extract the target class (class attribute) for training
C = data['Class'] #(2 points)
# Extract the predictor (data attributes) for training
D = data.drop(['Name','Class'],axis=1) #(2 points)

# Create a decision tree classifier object. The impurity measure should be based on entropy. Constrain the generated tree with a maximum depth of 3
clf = tree.DecisionTreeClassifier(criterion='entropy',max_depth=3) #(6 points)
# Train the classifier using the predictor (D) and target class (C) variable created earlier
clf = clf.fit(D, C) #(6 points)

# Suppose we have the following data
testData = [['lizard',0,0,0,0,1,1,'non-mammals'],
           ['monotreme',1,0,0,0,1,1,'mammals'],
           ['dove',1,0,0,1,1,0,'non-mammals'],
           ['whale',1,1,1,0,0,0,'mammals']]
testData = pd.DataFrame(testData, columns=data.columns)
testData

# Apply the decision tree to classify the data 'testData'.
# Extract the predictor and target class attributes from 'testData'
testC = testData['Class'] #(2 points)
testD = testData.drop(['Name','Class'],axis=1) #(2 points)

# Apply the decision tree to classify the data 'testData'.
predC = clf.predict(testD) #(6 points)
predictions = pd.concat([testData['Name'],pd.Series(predC,name='Predicted Class')], axis=1)
predictions
# The classifier should correctly label the vertabrae of 'testData' except for the monotreme

# Compute and print the accuracy of the classifier on 'testData'
print('The accuracy of the classifier is %.2f' % (accuracy_score(testC, predC))) #(6 points)