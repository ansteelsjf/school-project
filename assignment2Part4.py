import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp2d
import math

#(a)

I2 = plt.imread('D:\Data\I2.jpg')
J2 = plt.imread('D:\Data\J2.jpg')
BrainMRI_1 = plt.imread('D:\Data\BrainMRI_1.jpg')
BrainMRI_2 = plt.imread('D:\Data\BrainMRI_2.jpg')
BrainMRI_3 = plt.imread('D:\Data\BrainMRI_3.jpg')
BrainMRI_4 = plt.imread('D:\Data\BrainMRI_4.jpg')
#cers = J2[0:500,0:500]

t=np.array([])
def translation(I,t):

    sz_x=I.shape[0]
    sz_y=I.shape[1]
    
    x= np.linspace(0,sz_x,sz_x)
    y= np.linspace(0,sz_y,sz_y)
    
    f= interp2d(x+t[0],y+t[1],I,kind='cubic',fill_value=0)
    znew=f(x,y)
    return znew


move=translation(I2[:500,:500],[200,200])
plt.imshow(move)

#(b)


def ssd(I,J):
    return np.sum((I-J)**2)

iters=500
lr=0.0000001
#ssd(Icers,Jcers)

def gra_move(I,J,u):
    for i in range(iters):
        curr=translation(J,u)
        gy,gx = np.gradient(curr)
        dx,dy = 0.,0.
        dx = -((curr-I)*gx).sum()*2
        dy = -((curr-I)*gy).sum()*2
        du=np.array([dx,dy])
        cu = lr*du
        u = u-cu
        print(ssd(curr,BrainMRI_1),u)
        data.append(ssd(curr,I))
    return curr
data=[]
curr2=gra_move(BrainMRI_1, BrainMRI_2, [10,10])
plt.plot(data)
plt.imshow(curr2)

data=[]
curr3=gra_move(BrainMRI_1, BrainMRI_3, [10,10])
plt.plot(data)
plt.imshow(curr3)

data=[]
curr4=gra_move(BrainMRI_1, BrainMRI_4, [10,10])
plt.plot(data)
plt.imshow(curr4)
 
#(c)

def rotation(I, theta):
    H, W = I.shape 
    theta = np.deg2rad(theta)

    matrix = np.array([[math.cos(theta), -math.sin(theta), 0],
                       [math.sin(theta), math.cos(theta), 0],
                       [0, 0, 1]])


    znew = np.zeros_like(I, dtype=np.uint8)

    for i in range(H):
        for j in range(W):

            new_coordinate = np.matmul(np.array([i, j, 1]), matrix)

            new_i = int(math.floor(new_coordinate[0]))
            new_j = int(math.floor(new_coordinate[1]))

            if new_j>=W or new_i >=H or new_i<1 or new_j<1:
                continue

            znew[i, j] = I[new_i, new_j]

    return znew

znew = rotation(BrainMRI_4, 30)
plt.imshow(znew)

#(d)
def gra_rotate(I,J,t):
    x,y = np.arange(J.shape[0]),np.arange(J.shape[1])
    for itr in range(iters):
        curr = rotation(J,t)
        c,s =np.cos(np.deg2rad(t)),np.sin(np.deg2rad(t))
        gy,gx = np.gradient(curr)
        dt = 0.
        dt = -2*((curr-I)*(gy*(x*c-y*s)-gx*(x*s+y*c))).sum()
        ct = lr*dt
        t-=ct
        print(ssd(curr,I),t)
        data.append(ssd(curr,I))
    return curr
data=[]
lr=0.00000001
iters=100
curr2=gra_rotate(BrainMRI_1, BrainMRI_2, 45)
plt.plot(data)
plt.imshow(curr2)

data=[]
iters=150
lr=0.0000000001
curr3=gra_rotate(BrainMRI_1, BrainMRI_3, 0)
plt.plot(data)
plt.imshow(curr3)

data=[]
lr=0.00000001
iters=100
curr4=gra_rotate(BrainMRI_1, BrainMRI_4, 45)
plt.plot(data)
plt.imshow(curr4)
#(e)
def gra_all(I,J,u,t):
    x,y = np.arange(J.shape[0]),np.arange(J.shape[1])
    for itr in range(iters):
        currt = translation(J,u)
        curr = rotation(currt,t)
        c,s =np.cos(np.deg2rad(t)),np.sin(np.deg2rad(t))
        gy,gx = np.gradient(curr)
        dx,dy,dt = 0.,0.,0.
        dx = -((curr-I)*gx).sum()*2
        dy = -((curr-I)*gy).sum()*2
        dt = -2*((curr-I)*(gy*(x*c-y*s)-gx*(x*s+y*c))).sum()
        
        du=np.array([dx,dy])
        
        cu = lr*du
        ct = lr*dt
        
        u-=cu
        t-=ct
        print(ssd(curr,I),t,u)
        data.append(ssd(curr,I))
    return curr
data=[]
lr=0.0000000001
iters=200
curr2=gra_all(BrainMRI_1, BrainMRI_3, [0,0], 0)
plt.plot(data)   
plt.imshow(curr2)



