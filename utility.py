# Important functions
import pydicom
import os
import cv2
import numpy as np
import h5py
def stacker(path):
    files=os.listdir(path)
    for x in range(0,len(files),10):
        img_top_stack=[return_image(path,file) for file in files[x:x+5]]
        img_bottom_stack=[return_image(path,file) for file in files[x+5:x+10]]
        yield np.vstack([np.hstack(img_top_stack),np.hstack(img_bottom_stack)])

def return_image(path,file='',resize=None):
    if file is not '':
        path= os.path.join(path,file)
    if resize is not None:
        return cv2.resize(pydicom.dcmread(path,force=True).pixel_array,(resize,resize))
    else: return pydicom.dcmread(path,force=True).pixel_array

def return_trn_test_split(data,frac=1):
    # Accepts numpy arrays; for the time being
    # Returns (train, test) tuple
    upto=0
    # if data is list:
    #     upto=int(len(data)*frac)
    # elif data is np.ndarray:
    upto=int(data.shape[0]*frac)
    return (data[:upto],data[upto:])

def read_hdf5_cancerdata(path,file_labels=False,dtype_=None):
    # Returns a tuple of images and their labels...
    # file_labels = True, then return labels from the file itself
    # file_labels = False, then generate the labels as...
    # BENIGN : 0 , MALIGNANT : 1
    with h5py.File(path, "r") as f:
        b=f['benign']
        m=f['malignant']
        img_b=b['images'][...]
        img_m=m['images'][...]
        if dtype_ is not None:
            img_b=img_b.astype(dtype_)
            img_m=img_m.astype(dtype_)
        if file_labels:
            lbl_b=b['labels'][...]
            lbl_m=m['labels'][...]
        else:
            lbl_b=np.zeros((img_b.shape[0],),dtype=np.int8)
            lbl_m=np.ones((img_m.shape[0],),dtype=np.int8)
    return (img_b,lbl_b,img_m,lbl_m)
