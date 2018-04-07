print("Initialise modules...\n")
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import dicom as pdicom
import os
import scipy.ndimage
import matplotlib.pyplot as plt
import glob
import cv2
import mahotas as mh
from skimage import measure, morphology
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

print("Reading Images...\n")
data_dir='DOI'
labels_df= pd.read_csv('calc_case_description_test_set.csv',index_col=0)

#
# inp=labels_df[['left or right breast','image view','pathology','ROI mask file path']][labels_df['pathology']!='BENIGN_WITHOUT_CALLBACK']
# inp.head()
# img=pdicom.read_file(imgpt)
#
# imgpx=((img.pixel_array/65535)*255).astype(np.uint8)
# print("Computing Haralick features...\n")
# print(mh.features.haralick(imgpx).mean(0))
# #plt.imshow(imgpx,cmap=plt.cm.bone)





inp=labels_df[['left or right breast','image view','pathology','ROI mask file path']][labels_df['pathology']!='BENIGN_WITHOUT_CALLBACK']
def ff(x):
    loc=data_dir+'/'+x
    img=pdicom.read_file(loc)
    imgpx=((img.pixel_array/65535)*255).astype(np.uint8)
    return(mh.features.haralick(imgpx).mean(0))

res=inp
print("Computing Haralick features...\n")
res['hr'] = res['ROI mask file path'].map(ff)
res.to_csv('some.csv')
#plt.imshow(imgpx,cmap=plt.cm.bone)
