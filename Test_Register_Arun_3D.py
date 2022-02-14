# -*- coding: utf-8 -*-
"""
@author(s): ______
"""
import sys
sys.path.append('D:\python')


import numpy as np#(2 points)
import matplotlib.pyplot as plt
from Register_Arun_3D import register_Arun_3D

# Import fixed data points
fixed = np.genfromtxt('D:\\FixedPoints.csv', delimiter=',') #(2 points)
# Prepare data points: transpose matrix to pass from Nx3 to a 3xN matrix
fixedT = fixed.T #(2 points)
# Plot fixed data points
fig = plt.figure()
ax = plt.axes(projection="3d")
ax.scatter(fixed[:,0], fixed[:,1], fixed[:,2], 'o', color='red', label='Fixed') #(2 points)

# Import moving data points
moving = np.genfromtxt('D:\\MovingPoints.csv', delimiter=',') #(2 points)
# Prepare data points: transpose matrix to pass from Nx3 to a 3xN matrix
movingT = moving.T #(2 points)
# Plot moving data points
ax.scatter(moving[:,0], moving[:,1], moving[:,2], 'o', color='blue', label='Moving') #(2 points)

# Register the fixed and moving points as moving = R @ fixed + t
[R, t] = register_Arun_3D(fixedT, movingT) #(3 points)

# Plot registered data points
registered = (R @ fixedT) + t.reshape(-1, 1) #(3 points)
ax.scatter(registered.T[:,0], registered.T[:,1], registered.T[:,2], 'o', color='black', label='Fixed registered') #(2 points)
plt.legend(loc='upper left');
plt.show()

# Enlarge figure, notice the black dots (search until you find, the black dots 
# are almost not noticeable because the registration is almost perfect). 
# To convince yourself, rerun code without plotting the registered points this time.
# Submit a PDF document, where you include the two figures and draw on one of them to 
# show the location of the fixed points that were registered onto the moving points. (5 points)
 