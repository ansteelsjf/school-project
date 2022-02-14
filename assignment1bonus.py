import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt

nii = nib.load('D:/t1s/img1.nii.gz')
img = nii.get_data()

from sklearn.cluster import MiniBatchKMeans
from skimage.morphology import dilation,square,erosion
from skimage.segmentation import flood_fill

plt.hist(img.ravel(),bins=100)

plt.imshow((img[:,:,250]>65) * (img[:,:,250]<95))

mb=MiniBatchKMeans(n_clusters=3)

for i in range(384):

    mb.fit(np.expand_dims(np.ravel(img[:,:,i]),axis=1))
    
    labs = np.reshape(mb.labels_,[img.shape[0],img.shape[1]])
    
    bg = labs ==0
    origwm=labs==1
    wm=labs==1
    gmsk=labs==2
    
    
    
    flood = flood_fill(erosion(wm+gmsk,square(3)).astype(float),(101,205),10,tolerance=0.5)
    
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider
import nibabel as nib

def showimage(img):
    #img = img.get_data()
    image_dim_len = len(np.array(img).shape)
    if image_dim_len==3:
        sz_x = img.shape[0]
        sz_y = img.shape[1]
        sz_z = img.shape[2]
        fig= plt.figure()
        ax = fig.add_subplot()
        fig.subplots_adjust(left=0.25, bottom=0.25)
        im = img[:,:,int(sz_z/2)]
        ax.imshow(im)
        ax1 = fig.add_axes([0.25, 0.1, 0.65, 0.03])
        s1 = Slider(ax1, 'z', 0, sz_z)
        def update(val):
            im = img[:,:,int(s1.val)]
            ax.imshow(im)
            fig.canvas.draw()
        s1.on_changed(update)
        plt.show()
    elif image_dim_len==4:
        sz_x = img.shape[0]
        sz_y = img.shape[1]
        sz_z = img.shape[2]
        sz_t = img.shape[3]
        fig= plt.figure()
        ax = fig.add_subplot()
        fig.subplots_adjust(left=0.25, bottom=0.25)
        im = img[:,:,int(sz_z/2),0]
        ax.imshow(im)
        ax1 = fig.add_axes([0.25, 0.15, 0.65, 0.03])
        ax2 = fig.add_axes([0.25, 0.1, 0.65, 0.03])
        s1 = Slider(ax1, 'z', 0, sz_z)
        s2 = Slider(ax2, 'time', 0, sz_t)
        def update_4d(val):
            imm = img[:,:,int(s1.val),int(s2.val)]
            ax.imshow(imm)
            fig.canvas.draw()
        s1.on_changed(update_4d)
        s2.on_changed(update_4d)
        plt.show()
    else:
        print("error")
img = nib.load("D:/t1s/img1.nii.gz")
showimage(img3)