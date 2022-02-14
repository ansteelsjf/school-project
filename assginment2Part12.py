import numpy as np
import matplotlib.pyplot as plt

I1 = plt.imread('D:\Data\I1.png')
J1 = plt.imread('D:\Data\J1.png')
I2 = plt.imread('D:\Data\I2.jpg')
J2 = plt.imread('D:\Data\J2.jpg')
I3 = plt.imread('D:\Data\I3.jpg')
I4 = plt.imread('D:\Data\I4.jpg')
I5 = plt.imread('D:\Data\I5.jpg')
I6 = plt.imread('D:\Data\I6.jpg')
J3 = plt.imread('D:\Data\J3.jpg')
J4 = plt.imread('D:\Data\J4.jpg')
J5 = plt.imread('D:\Data\J5.jpg')
J6 = plt.imread('D:\Data\J6.jpg')
BrainMRI_1 = plt.imread('D:\Data\BrainMRI_1.jpg')
BrainMRI_2 = plt.imread('D:\Data\BrainMRI_2.jpg')
BrainMRI_3 = plt.imread('D:\Data\BrainMRI_3.jpg')
BrainMRI_4 = plt.imread('D:\Data\BrainMRI_4.jpg')

#Part 1: Joint histogram 10/100
#(a)Write a python function JointHist(I, J, bin) which calculates the joint histogram of two images of the same size.
def JointHist(I,J,bin):
    
    plt.hist2d(np.ravel(I), np.ravel(J), bins=bin)
    plt.xlabel('img1')
    plt.ylabel('img2')
    cbar = plt.colorbar()
    cbar.ax.set_ylabel('Count')
    
def JointHist_log(I,J,bin):
    hist_2d, x_edges, y_edges = np.histogram2d(I.ravel(),J.ravel(),bins=bin)
    hist_2d_log = np.zeros(hist_2d.shape)
    non_zeros = hist_2d != 0
    hist_2d_log[non_zeros] = np.log(hist_2d[non_zeros])
    plt.imshow(hist_2d_log.T, origin='lower')
JointHist(I2, J2, 30)

#hist_2d, x_edges, y_edges = np.histogram2d(I1.ravel(),J1.ravel(),bins=20)

#(b) For images of size n x p, verify that:
hist,edges,qqq,ppp = plt.hist2d(np.ravel(I2),np.ravel(J2))
hist.sum()
I2.size

#(c) Calculate and show the joint histogram of different pairs of images given in 
#the handout (I1,J1 I2,J2, etc.). Describe briefly what you observe 
#(you may want to use the logarithmic scale to visualize joint hist).

I1 = plt.imread('D:\Data\I1.png')
I1 = I1[:,:,2]
J1 = plt.imread('D:\Data\J1.png')


JointHist(I1, J1, 30)
JointHist_log(I1, J1, 20)


BrainMRI_1 = plt.imread('D:\Data\BrainMRI_1.jpg')
BrainMRI_2 = plt.imread('D:\Data\BrainMRI_2.jpg')
JointHist(BrainMRI_1, BrainMRI_2, 5)
JointHist_log(BrainMRI_1, BrainMRI_2, 20)
#plt.xscale('log')

I3 = plt.imread('D:\Data\I3.jpg')
I3 = I3[:231,:195]
I4 = plt.imread('D:\Data\I4.jpg')
JointHist(I3, I4, 20)
JointHist_log(I3, I4, 20)


J3 = plt.imread('D:\Data\J3.jpg')
J3 = J3[:231,:195]
J4 = plt.imread('D:\Data\J4.jpg')
JointHist(J3, J4, 30)
JointHist_log(J3, J4, 20)

BrainMRI_3 = plt.imread('D:\Data\BrainMRI_3.jpg')
BrainMRI_4 = plt.imread('D:\Data\BrainMRI_4.jpg')
JointHist(BrainMRI_3, BrainMRI_4, 5)
JointHist_log(BrainMRI_3, BrainMRI_4, 20)

I5 = plt.imread('D:\Data\I5.jpg')
I6 = plt.imread('D:\Data\I6.jpg')
JointHist(I5, I6, 20)
JointHist_log(I5, I6, 20)

J5 = plt.imread('D:\Data\J5.jpg')
J6 = plt.imread('D:\Data\J6.jpg')
JointHist(J5, J6, 20)
JointHist_log(J5, J6, 20)

#Part 2: similarity criteria
#(a) Write a python function SSD(I,J) that calculates the sum squared difference 
#between two images I and J of the same size. No ‘for’ loops!

def ssd(I,J):
    return np.sum((I-J)**2)
print("ssd_I2_J2 %d" %ssd(I2,J2))
print("ssd_I1_J1 %d" %ssd(I1,J1))
print("ssd_I3_I4 %d" %ssd(I3,I4))
print("ssd_J3_J4 %d" %ssd(J3,J4))
print("ssd_I5_I6 %d" %ssd(I5,I6))
print("ssd_J5_J6 %d" %ssd(J5,J6))
print("ssd_BrainMRI_1_BrainMRI_2 %d" %ssd(BrainMRI_1,BrainMRI_2))
print("ssd_BrainMRI_3_BrainMRI_4 %d" %ssd(BrainMRI_3,BrainMRI_4))

#(b) Write a python function corr(I,J) that calculates the pearson correlation coefficient
# between two images of the same size. No ‘for’ loops!

def corr(I,J):
    A=sum((np.ravel((I)-np.mean(I)))*(np.ravel((J)-np.mean(J))))
    B=(np.sqrt(sum((np.ravel(I-np.mean(I))**2))))*(np.sqrt(sum(np.ravel((J-np.mean(J))**2))))
    return(A/B)

corr(I2,J2)
print("corr_I2_J2 %f" %corr(I2,J2))
print("corr_I1_J1 %f" %corr(I1,J1))
print("corr_I3_I4 %f" %corr(I3,I4))
print("corr_J3_J4 %f" %corr(J3,J4))
print("corr_I5_I6 %f" %corr(I5,I6))
print("corr_J5_J6 %f" %corr(J5,J6))
print("corr_BrainMRI_1_BrainMRI_2 %f" %corr(BrainMRI_1,BrainMRI_2))
print("corr_BrainMRI_3_BrainMRI_4 %f" %corr(BrainMRI_3,BrainMRI_4))


#(c) Write a function MI(I,J) that calculates the mutual information between two images of the same size.

def MI(I,J):
    hist_2d, x_edges, y_edges = np.histogram2d(I.ravel(),J.ravel())
    pij = hist_2d / float(np.sum(hist_2d))
    pi = np.sum(pij, axis=1)
    pj = np.sum(pij, axis=0)
    pi_pj = pi[:, None] * pj[None, :]
    nzs = pij > 0
    return np.sum(pij[nzs] * np.log(pij[nzs] / pi_pj[nzs]))
MI(I2,J2)
print("MI_I2_J2 %f" %MI(I2,J2))
print("MI_I1_J1 %f" %MI(I1,J1))
print("MI_I3_I4 %f" %MI(I3,I4))
print("MI_J3_J4 %f" %MI(J3,J4))
print("MI_I5_I6 %f" %MI(I5,I6))
print("MI_J5_J6 %f" %MI(J5,J6))
print("MI_BrainMRI_1_BrainMRI_2 %f" %MI(BrainMRI_1,BrainMRI_2))
print("MI_BrainMRI_3_BrainMRI_4 %f" %MI(BrainMRI_3,BrainMRI_4))
