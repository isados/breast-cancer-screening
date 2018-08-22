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

# Randomly shuffle the images
df1=df1.sample(frac=1)

# Create another column in the Dataframe to hold the numpy arrays of each image located at their path
df1.loc[:,'arr']=df1.path.apply(lambda x: return_image(x,resize=299).flatten())
print('Finished resizing the images...\n')

# Picking Benign cases
dfb=df1.loc[df1.label=='BENIGN']
img_b=np.vstack(dfb.arr.values)
lbl_b=dfb.label.values.astype('S9')

# Picking Malignant cases
dfm=df1.loc[df1.label=='MALIGNANT']
img_m=np.vstack(dfm.arr.values)
lbl_m=dfm.label.values.astype('S9')

print('Finished splitting Benign & Malignant cases...\n')

# Write and Create a file
import h5py
print('\nSaving the dataset as an HDF5 file...')
file_name="images_1227.hdf5"
with h5py.File(file_name, "w") as f:
    # Create two groups or "subfolders" within the HDF5 file
    bn=f.create_group('benign')
    mg=f.create_group('malignant')

    # Store each Benign & Malignant datasets within
    dset = bn.create_dataset("images",data=img_b)
    dset = bn.create_dataset("labels",data=lbl_b)
    dset = mg.create_dataset("images",data=img_m)
    dset = mg.create_dataset("labels",data=lbl_m)

print('Done!!!\n')
print('The file {} contains 2 subgroups: benign & malignant with 2 datasets under each...'.format(file_name))
print("benign/ :\n\timages\n\tlabels")
print("malignant/ :\n\timages\n\tlabels")
