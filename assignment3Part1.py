import mne as mne
import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft,ifft,ifft2,fftfreq,fft2,fftshift,fftn,ifftn
import nibabel as nib
import pandas as pd
import scipy.stats as stats
import scipy.signal as signal
import scipy.ndimage as rotate
from scipy.signal import find_peaks
from scipy.signal import resample

eeg=mne.io.read_raw_brainvision('D:/subxp210/sub-xp210_task-2dNF_run-02_eeg.vhdr',preload=True)
eegdata=eeg.get_data()

eeg.info['bads'] = ['ECG']
eeg.set_montage('standard_1020',on_missing='ignore')

markers = mne.read_annotations('D:/subxp210/sub-xp210_task-2dNF_run-02_eeg.vmrk')
nmrks = 324
r128s = np.zeros(nmrks)
count = 0
for i in markers:
    if i['description'] == 'Response/R128' and count < 324:
        r128s[count] = i['onset']
        count = count + 1
        
plt.rcParams.update({'font.size':20})



st = int(r128s[0]*5000)
en = int(r128s[0]*5000+nmrks*5000)

#2b

trimmed = eegdata[:,st:en]
restrim = np.reshape(trimmed,[64,nmrks,5000])

restrim = restrim -np.mean(restrim,axis=1,keepdims=True) #broadcasting
subbed = np.reshape(restrim,trimmed.shape)

dchan=subbed
n_channels=64
sampling_freq=5000
info=mne.create_info(n_channels, sampling_freq)

raw =mne.io.RawArray(dchan,eeg.info)
raw.resample(sfreq=250)
 
rawdata=raw.get_data()


hignpass_raw=raw.copy()
hignpass_raw.filter(1,124)
ica=mne.preprocessing.ICA()
ica.fit(hignpass_raw)
comps=ica.get_sources(hignpass_raw).get_data()
#ica.plot_components()

bcg=comps[0,:]
peaks = find_peaks(bcg,distance=200)

plt.plot(bcg)

for xc in peaks[0]:
    plt.axvline(xc,color='red')


bcgpks = np.zeros([64,peaks[0].shape[0],250])
bcgpkinds =np.zeros([peaks[0].shape[0],250])
for i in np.arange(1,bcgpks.shape[1]-1):
    bcgpks[:,i,:]=rawdata[:,peaks[0][i]-125:peaks[0][i]+125]
    bcgpkinds[i,:]=np.arange(peaks[0][i]-125,peaks[0][i]+125)

bcgsubdat =rawdata.copy()
bcgpks = bcgpks-np.mean(bcgpks,axis=1,keepdims=True)
for i in np.arange(1,bcgpkinds.shape[0]-1):
    bcgsubdat[:,bcgpkinds[i,:].astype(int)]=bcgpks[:,i,:]
   
bcgsubdat[:,0:1000] = 0;
bcgsubdat[:,-1000]=0

plt.plot(rawdata[0,:]),plt.plot(bcgsubdat[0,:])

#2c
sub_eeg=mne.io.RawArray(bcgsubdat,raw.info)
highpass_sub = sub_eeg.copy()
highpass_sub.filter(1,45)
ica=mne.preprocessing.ICA()
ica.fit(highpass_sub)
newcomps=ica.get_sources(sub_eeg).get_data()
ica.plot_components()

#2d
from scipy.signal import welch
f,pxx=welch(newcomps,250)

plt.imshow(np.log(pxx[:,:]),aspect='auto') 
plt.gca().set_xticks(np.arange(0,130,10))
plt.gca().set_yticks(np.arange(0,63,2))
plt.xlabel('frequency(hz)');plt.ylabel('EEG component')
plt.title('EEG power 0-130 HZ in ICA components 0-63')

plt.plot(np.log(pxx[24,:]));plt.title('log power for component 24')
plt.xlabel('frequency(hz)');plt.ylabel('log power')



from scipy.signal import butter,lfilter

def butter_bandpass(lowcut,highcut,fs,order=5):
    nyq=0.5*fs
    low=lowcut/nyq
    high=highcut/nyq
    b,a=butter(order,[low,high],btype='band')
    return b,a
def butter_bandpass_filter(data,lowcut,highcut,fs,order=5):
    b,a=butter_bandpass(lowcut,highcut,fs,order=order)
    y=lfilter(b,a,data)
    return y

bp=butter_bandpass_filter(newcomps[10,:],8,13,250)

plt.plot(bp);plt.plot(np.abs(bp))
plt.plot(bp);plt.plot(newcomps[10,:])


#Step3
plt.rcParams.update({'font.size':20})
fmri = nib.load('D:/subxp210/sub-xp210_anat_sub-xp210_T1w.nii.gz')
fmri=fmri.get_data()

#mc= nib.load('D:/subxp210/motion_correction_result.nii.gz')
#mc = mc.get_data()



#Step4
nii= nib.load('D:/subxp210/blur.nii.gz')
nimg=nii.get_data()
resnii=np.reshape(nimg,[106*106*16,332])

resbp = resample(np.abs(bp),332)
resbp = np.roll(resbp,4)

conved = np.convolve(resbp,np.ones([15])/15,'same')

normnii = resnii -np.mean(resnii,axis=0,keepdims=True)

normbp= conved-np.mean(conved)

normbpimg =np.zeros(normnii.shape)
normbpimg = normbpimg+normbp

#compute r

r =np.sum(normbpimg*normnii,axis=1) \
    / np.sqrt((np.sum(normbpimg*normbpimg,axis=1) \
        *np.sum(normnii*normnii,axis=1)))

rbrain =np.reshape(r,nimg[:,:,:,0].shape)

for i in np.arange(0,16):
    plt.subplot(4,4,i+1)
    plt.imshow(rbrain[:,:,i],aspect='auto',vmin=-0.5,vmax=0.5,cmap='jet')
    
#nii= nib.load('D:/subxp210/mean.nii.gz')

boldnii=nib.Nifti1Image(rbrain.astype(np.float32),nii.affine)

nib.save(boldnii,'D:/subxp210/corr.nii.gz')

















