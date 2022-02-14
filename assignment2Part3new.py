import numpy as np
import matplotlib.pyplot as plt
import copy

add = np.array([[0,0,0,1]])
arr = np.array([[0,0,0,1]])

add[0,2]
for t in range(0,20):
    add[0,1]=0
    add[0,2]=0
    for s in range(0,20):
        add[0,2]=0
        for r in range(0,5):
            add[0,2]=add[0,2]+1
            arr =np.append(arr,add,axis=0)
        add[0,1]=add[0,1]+1
    add[0,0]=add[0,0]+1   
arr =arr.T
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(arr[0,:], arr[1,:], arr[2,:], c = 'black', marker='o')

#(b)
def rigid_transform(arr, theta, omega, phi, p, q, r):
    Rxz=np.array([[np.cos(theta),0,np.sin(theta),0],[0,1,0,0],[-np.sin(theta),0,np.cos(theta),0],[0,0,0,1]])
    Rzy=np.array([[1,0,0,0],[0,np.cos(omega),-np.sin(omega),0],[0,np.sin(omega),np.cos(omega),0],[0,0,0,1]])
    Ryx=np.array([[np.cos(phi),-np.sin(phi),0,0],[np.sin(phi),np.cos(phi),0,0],[0,0,1,0],[0,0,0,1]])
    trans = np.array([[1,0,0,p],[0,1,0,q],[0,0,1,r],[0,0,0,1]])
    for m in range(0,2001):
        arr[:,m] = np.dot(Rxz,arr[:,m])
    for n in range(0,2001):
        arr[:,n] = np.dot(Rzy,arr[:,n])
    for c in range(0,2001):
        arr[:,c] = np.dot(Ryx,arr[:,c])
    for d in range(0,2001):
        arr[:,d] = np.dot(trans,arr[:,d])

Arr = copy.copy(arr)
rigid_transform(arr, np.pi/3, np.pi/3, np.pi/3, 1, 1, 1)
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(arr[0,:], arr[1,:], arr[2,:], c = 'r', marker='o')
ax.scatter(Arr[0,:], Arr[1,:], Arr[2,:], c = 'black', marker='o')
#(c)

def affine_transform(arr, theta, omega, phi, p, q, r,s):
    Rxz=np.array([[np.cos(theta),0,np.sin(theta),0],[0,1,0,0],[-np.sin(theta),0,np.cos(theta),0],[0,0,0,1]])
    Rzy=np.array([[1,0,0,0],[0,np.cos(omega),-np.sin(omega),0],[0,np.sin(omega),np.cos(omega),0],[0,0,0,1]])
    Ryx=np.array([[np.cos(phi),-np.sin(phi),0,0],[np.sin(phi),np.cos(phi),0,0],[0,0,1,0],[0,0,0,1]])
    trans = np.array([[s,0,0,p],[0,s,0,q],[0,0,s,r],[0,0,0,1]])
    for m in range(0,2001):
        arr[:,m] = np.dot(Rxz,arr[:,m])
    for n in range(0,2001):
        arr[:,n] = np.dot(Rzy,arr[:,n])
    for c in range(0,2001):
        arr[:,c] = np.dot(Ryx,arr[:,c])
    for d in range(0,2001):
        arr[:,d] = np.dot(trans,arr[:,d])

affine_transform(arr,np.pi/2, np.pi/2, np.pi/2, 1, 1, 1,0.5)
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(arr[0,:], arr[1,:], arr[2,:], c = 'r', marker='o')
ax.scatter(Arr[0,:], Arr[1,:], Arr[2,:], c = 'black', marker='o')

#(d)
M1=np.array([[0.9045,-0.3847,-0.1840,10.000],[0.2939,0.8750,-0.3847,10.000],[0.3090,0.2939,0.9045,10.000],[0,0,0,1.000]])
M2=np.array([[-0.0,-0.2598,0.1500,-3.000],[0.000,-0.1500,-0.2598,1.5000],[0.3000,-0.000,0.000,0],[0,0,0,1.000]])
M3=np.array([[0.7182,-1.3727,-0.5660,1.8115],[-1.9236,-4.6556,-2.5512,0.2873],[-0.6426,-1.7985,-1.6285,0.7404],[0,0,0,1]])



Arr = copy.copy(arr)
for m in range(0,2001):
    arr[:,m]=np.dot(M1,arr[:,m])
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(arr[0,:], arr[1,:], arr[2,:], c = 'r', marker='o')
ax.scatter(Arr[0,:], Arr[1,:], Arr[2,:], c = 'black', marker='o')

for n in range(0,2001):
    arr[:,n]=np.dot(M2,Arr[:,n])
ax.scatter(arr[0,:], arr[1,:], arr[2,:], c = 'y', marker='o')

for z in range(0,2001):
    arr[:,z]=np.dot(M3,Arr[:,z])
ax.scatter(arr[0,:], arr[1,:], arr[2,:], c = 'g', marker='o')




