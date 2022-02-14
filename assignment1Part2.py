
import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib

img = nib.load("D:/modalities/tof.nii.gz")
img = img.get_data()

#Michelson contrast
min = np.min(img)
max = np.max(img)
C_Michelson = (max-min)/(max+min)
print('min%s'%min,'max%s'%max,'Michelson%s'%C_Michelson)

#Root Mean Square contrast
rms = np.sqrt(np.mean(np.square(img)))
print('rms%s'%rms)

#Entropy contrast
from sklearn.metrics.cluster import entropy
ent=entropy(img)
print('entropy%s'%ent)


