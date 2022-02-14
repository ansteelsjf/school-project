
import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib
import SimpleITK as sitk
from numpy.fft import fft,ifft,ifft2,fftfreq,fft2,fftshift,fftn,ifftn
img1 = nib.load("D:/modalities/cardiac_axial.nii.gz")
img1 = img1.get_data()
img1 = img1[:,:,:,0]

def gaussfilter(img,sig):
    img_freqs =fftshift(fftn(img))

    sz_x = img.shape[0]
    sz_y = img.shape[1]
    sz_z = img.shape[2]


    [X,Y,Z]= np.mgrid[0:sz_x,0:sz_y,0:sz_z]
    xpr = X-int(sz_x)//2
    ypr = Y-int(sz_y)//2
    zpr = Z-int(sz_z)//2

    sigma =sig

    gaussfilt = np.exp(-((xpr**2+ypr**2+zpr**2)/(2*sigma**2)))/(2*np.pi*sigma**2)
    gaussfilt = gaussfilt/np.max(gaussfilt)

    filtered_freqs= img_freqs*gaussfilt

    filtered = np.abs(ifftn(fftshift(filtered_freqs)))

    return(filtered)


filtered=gaussfilter(img1, 2)


plt.subplot(3,3,1)
plt.imshow(filtered[:,:,2],cmap='jet')
plt.title('cardiac_ax_sig2')
plt.xticks([])
plt.yticks([])

img2 = nib.load("D:/modalities/cardiac_realtime.nii.gz")
img2 = img2.get_data()
img2=img2[:,:,:,0]
filtered2=gaussfilter(img2, 2)
plt.subplot(3,3,2)
plt.imshow(filtered2[:,:,0],cmap='jet')
plt.title('cardiac_real_sig2')
plt.xticks([])
plt.yticks([])

img3 = nib.load("D:/modalities/ct.nii.gz")
img3 = img3.get_data()
filtered3=gaussfilter(img3, 2)
plt.subplot(3,3,3)
plt.imshow(filtered3[:,:,120],cmap='jet')
plt.title('ct_sig2')
plt.xticks([])
plt.yticks([])

img4 = nib.load("D:/modalities/fmri.nii.gz")
img4 = img4.get_data()
img4=img4[:,:,:,0]
filtered4=gaussfilter(img4, 2)
plt.subplot(3,3,4)
plt.imshow(filtered4[:,:,18],cmap='jet')
plt.title('fmri_sig2')
plt.xticks([])
plt.yticks([])

img5 = nib.load("D:/modalities/meanpet.nii.gz")
img5 = img5.get_data()
filtered5=gaussfilter(img5, 2)
plt.subplot(3,3,5)
plt.imshow(filtered5[:,:,104],cmap='jet')
plt.title('meanpet_sig2')
plt.xticks([])
plt.yticks([])

img6 = nib.load("D:/modalities/swi.nii.gz")
img6 = img6.get_data()
filtered6=gaussfilter(img6, 2)
plt.subplot(3,3,6)
plt.imshow(filtered6[:,:,250],cmap='jet')
plt.title('swi_sig2')
plt.xticks([])
plt.yticks([])

img7 = nib.load("D:/modalities/T1_with_tumor.nii.gz")
img7 = img7.get_data()
filtered7=gaussfilter(img7, 2)
plt.subplot(3,3,7)
plt.imshow(filtered7[:,:,128],cmap='jet')
plt.title('T1_sig2')
plt.xticks([])
plt.yticks([])

img8 = nib.load("D:/modalities/tof.nii.gz")
img8 = img8.get_data()
filtered8=gaussfilter(img8, 2)
plt.subplot(3,3,8)
plt.imshow(filtered8[:,:,75],cmap='jet')
plt.title('tof_sig2')
plt.xticks([])
plt.yticks([])
