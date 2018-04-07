#%matplotlib inline
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import dicom as pdicom
import os
import scipy.ndimage
import matplotlib.pyplot as plt
import glob
import mahotas as mh

from skimage import measure, morphology
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

data_dir='DOI'

labels_df= pd.read_csv('calc_case_description_test_set.csv',index_col=0)

x=labels_df.groupby('patient_id')['image file path'].unique()[0]
redf=pdicom.read_file(data_dir+'/'+x[0])



x=labels_df.groupby('patient_id')['image file path'].unique()[5]
redf=pdicom.read_file(data_dir+'/'+x[0])
img=redf.pixel_array
print(mh.features.haralick(img).mean(0))
