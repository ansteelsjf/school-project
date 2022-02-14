
import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib


img = nib.load("D:/modalities/swi.nii.gz")
img = img.get_data()
img=img[:,:,200:250]
img= np.min(img, axis=2)
plt.subplot(1,2,1)
plt.imshow(img,cmap='jet')
plt.title('swi MIP')
plt.xticks([])
plt.yticks([])



img2 = nib.load("D:/modalities/tof.nii.gz")
img2 = img2.get_data()

img2= np.max(img2, axis=2)
plt.subplot(1,2,2)
plt.imshow(img2,cmap='jet')
plt.title('tof MIP')
plt.xticks([])
plt.yticks([])