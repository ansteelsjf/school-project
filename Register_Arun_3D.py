# -*- coding: utf-8 -*-
"""
@author(s): ______
"""
# Import library
import numpy as np #(2 points)

# Function register_Arun_3D
# Input: Two 3xN matrices of points to register: 
#    fixed dataset F of N points and moving dataset M of N points
# Output: R = 3x3 rotation matrix, t = 3x1 column vector
# such that M = R@F+t
# Note: the operator @ is used for matrix multiplication.

def register_Arun_3D(F, M):
    # Ensure the matrices F and M have the same shape: same dimension and same amount of points to register
    if F.shape != M.shape: #(5 points)
        raise Exception("The datasets do not have the same size")
    
    # Ensure the points have 3D coordinates
    num_rows, num_cols = F.shape #(5 points)
    if num_rows != 3:
        raise Exception("The datasets do not have a 3xN size")

    #  (i) Find R 
    # Step 1, Arun's algorithm
    # Find centroids of F and M column wise
    centroid_F = np.mean(F, axis=1) #(3 points)
    centroid_M = np.mean(M, axis=1) #(3 points)

    # Ensure F and M have same centroid
    Fc =  F- centroid_F.reshape(-1, 1) #(5 points)
    Mc =  M - centroid_M.reshape(-1, 1) #(5 points)

    # Step 2, Arun's algorithm
    # Calculate the 3x3 matrix H
    H = Fc @ np.transpose(Mc) #(5 points)

    # Step 3, Arun's algorithm
    # Find the SVD of H
    U, S, Vt = np.linalg.svd(H) #(7 points)
    
    # Step 4, Arun's algorithm
    # Calculate X    
    X = Vt.T @ U.T #(5 points)

    # Step 5, Arun's algorithm
    R = X
    # Calculate, det (x), the determinant of X
    if (np.linalg.det(X) < 0): #(6 points)
    # if X is a reflection
    # check if one of the singular values of H is zero
        if (np.any(H==0)): #(6 points)
            raise Exception("Arun's method is not appropriate for this dataset. Use a RANSAC-like technique.")
        else:
            Vt[2,:] *= -1 #(6 points)
            R = U.T @ Vt.T #(4 points)

    #(i) Find t
    t = centroid_M - R @ centroid_F #(6 points)

    return R, t