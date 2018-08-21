# Important functions
import pydicom
import os
import cv2

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
