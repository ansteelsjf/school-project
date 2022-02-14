
import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib
import SimpleITK as sitk
from numpy.fft import fft,ifft,ifft2,fftfreq,fft2,fftshift,fftn,ifftn
img = nib.load("D:/modalities/ct.nii.gz")
img = img.get_data()

img_freqs =fftshift(fftn(img))

sz_x = img.shape[0]
sz_y = img.shape[1]
sz_z = img.shape[2]


[X,Y,Z]= np.mgrid[0:sz_x,0:sz_y,0:sz_z]
xpr = X-int(sz_x)//2
ypr = X-int(sz_y)//2
zpr = X-int(sz_z)//2

sigma =40

gaussfilt = np.exp(-((xpr**2+ypr**2+zpr**2)/(2*sigma**2)))/(2*np.pi*sigma**2)
gaussfilt = gaussfilt/np.max(gaussfilt)

filtered_freqs= img_freqs*gaussfilt


filtered = np.abs(ifftn(fftshift(filtered_freqs)))
plt.figure()
plt.hist((filtered[:,:,120]), bins=512)
plt.show()


# edges
edges = img- filtered
plt.imshow(edges[:,:,120])

img = sitk.ReadImage('D:/modalities/ct.nii.gz')
img = sitk.Cast(sitk.RescaleIntensity(img),sitk.sitkUInt8)
img = sitk.GetArrayFromImage(img)
img=img[:,:,120]
plt.figure()
plt.hist(img, bins=100)
plt.show()


