import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
from nilearn import image

nii = nib.load('D:/t1s/t2.nii.gz')
img = nii.get_data()

from sklearn.cluster import MiniBatchKMeans

plt.hist(img.ravel(),bins=100)

plt.imshow((img[:,:,250]>65) * (img[:,:,250]<95))

mb=MiniBatchKMeans(n_clusters=3)

mb.fit(np.expand_dims(np.ravel(img[:,:,250]),axis=1))

labs = np.reshape(mb.labels_,[img.shape[0],img.shape[1]])

bg = labs ==0
origwm=labs==1
wm=labs==1
gmsk=labs==2

from skimage.morphology import dilation,square,erosion
from skimage.segmentation import flood_fill

flood = flood_fill(erosion(wm+gmsk,square(3)).astype(float),(101,205),10,tolerance=0.5)

plt.imshow(img[:,:,250]*flood/10)



for i in np.arange(0,10):
    wm =dilation(wm,square(3))
    wm = wm*gmsk+origwm
    
#multi modal

t2nii = nib.load('D:/t1s/img2.nii.gz')
t2img=t2nii.get_data()
t1nii=nib.load('D:/t1s/img1.nii.gz')
t1img=t1nii.get_data()
features = np.zeros([t1img[:,:,250].ravel().shape[0],2])
features[:,0] = t1img[:,:,250].ravel();features[:,1]=t2img[:,:,250].ravel();
mb=MiniBatchKMeans(n_clusters=5)
mb.fit(features)
plt.imshow(np.reshape(mb.labels_,[t1img.shape[0],t1img.shape[1]]))


#generate some features
base_dx = np.zeros(t1img[:,:,250].shape);base_dy = np.zeros(t1img[:,:,250].shape)
dx=np.diff(t1img[:,:,250],axis=1);base_dx[:,0:-1]=dx
dy=np.diff(t1img[:,:,250],axis=0);base_dy[0:-1,:]=dy
features = np.zeros([base_dx.ravel().shape[0],2])
features[:,0]=base_dx.ravel();features[:,1]=base_dy.ravel()
mb=MiniBatchKMeans(n_clusters=3)
mb.fit(features)
plt.imshow(np.reshape(mb.labels_,[base_dx.shape[0],base_dx.shape[1]]))