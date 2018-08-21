# Import these packages
import matplotlib.pyplot as plt
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import pydicom #Read mammogram images stored in DICOM files
import cv2
import time
from utility import *

print('Finished importing packages...')
df = pd.read_csv('main_woMM.csv',index_col='name')
df1=df[(df.aspectratio<1.51) & (df.aspectratio>0.49) & (df['calc/mass']=='CALC')]

# Return all images as a tuple (label,img_array)
df1=df1.sample(frac=1)
img=df1.path
img=img.apply(lambda x: return_image(x,resize=299).flatten())
print('Finished resizing the images...\n')
img=np.vstack(img.values).astype(np.uint16)
print('...Converting them to a numpy array...\n')
lbl=df1.label
lbl=lbl.values.astype('S')
print('...Doing the same with labels... Done!\n')
print('\nTaking a break...')
time.sleep(5)

# Write and Create a file
print('\nSaving the dataset as an HDF5 file \n')
import h5py
rows=df1.shape[0]
with h5py.File("images_1227.hdf5", "w") as f:
    dset1 = f.create_dataset("images",shape=(rows,89401), dtype='uint16')
    dset2 = f.create_dataset("labels",shape=(rows,), dtype='|S9')
    dset1[...]=img
    dset2[...]=lbl
print('Done! For real this time!!')
