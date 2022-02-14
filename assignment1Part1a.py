import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib

img = nib.load("D:/modalities/ct.nii.gz")
img = img.get_data()
plt.subplot(3,3,3)
plt.imshow(img[:,:,120],cmap='jet')
plt.title('M%s'%129+' R%s'%1556+' E%s'%5.3)
plt.xticks([])
plt.yticks([])

img2 = nib.load("D:/modalities/meanpet.nii.gz")
img2 = img2.get_data()
plt.subplot(3,3,5)
plt.imshow(img2[:,:,103],cmap='jet')
plt.title('M%s'%1.0+' R%s'%3836+' E%s'%3.0)
plt.xticks([])
plt.yticks([])

img3 = nib.load("D:/modalities/swi.nii.gz")
img3 = img3.get_data()
plt.subplot(3,3,6)
plt.imshow(img3[:,:,250],cmap='jet')
plt.title('M%s'%1.0+' R%s'%35+' E%s'%2.7)
plt.xticks([])
plt.yticks([])

img4 = nib.load("D:/modalities/T1_with_tumor.nii.gz")
img4 = img4.get_data()
plt.subplot(3,3,7)
plt.imshow(img4[:,:,128],cmap='jet')
plt.title('M%s'%1.0+' R%s'%30.2+' E%s'%4.1)
plt.xticks([])
plt.yticks([])

img5 = nib.load("D:/modalities/tof.nii.gz")
img5 = img5.get_data()
plt.subplot(3,3,8)
plt.imshow(img5[:,:,75],cmap='jet')
plt.title('M%s'%1.0+' R%s'%72.2+' E%s'%4.8)
plt.xticks([])
plt.yticks([])

img6 = nib.load("D:/modalities/cardiac_axial.nii.gz")
img6 = img6.get_data()
plt.subplot(3,3,1)
img6_3d=img6[:,:,:,0]
plt.imshow(img6_3d[:,:,2],cmap='jet')
plt.title('M%s'%1.0+' R%s'%2787+' E%s'%5.5)
plt.xticks([])
plt.yticks([])

img7 = nib.load("D:/modalities/cardiac_realtime.nii.gz")
img7 = img7.get_data()
plt.subplot(3,3,2)
img7_3d=img7[:,:,:,0]
plt.imshow(img7_3d[:,:,0],cmap='jet')
plt.title('M%s'%1.0+' R%s'%25906+' E%s'%5.4)
plt.xticks([])
plt.yticks([])

img8 = nib.load("D:/modalities/fmri.nii.gz")
img8 = img8.get_data()
plt.subplot(3,3,4)
img8_3d=img8[:,:,:,0]
plt.imshow(img8_3d[:,:,18],cmap='jet')
plt.title('M%s'%1.0+' R%s'%37.8+' E%s'%5.6)
plt.xticks([])
plt.yticks([])