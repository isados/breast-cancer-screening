from flask import Flask,request
from sklearn.linear_model import LogisticRegression
#import pickle
import numpy as np
from keras import layers
from keras.layers import Input,Dense,BatchNormalization,Flatten,Dropout,GlobalAveragePooling2D
from keras.models import Model,load_model
#from keras.utils import layer_utils
from keras.optimizers import Adam
#from keras.callbacks import ModelCheckpoint
#from keras.callbacks import EarlyStopping
#import keras.backend as K
#from keras.applications.inception_v3 import InceptionV3
#import matplotlib.pyplot as plt
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import dicom as pdicom #Read mammogram images stored in DICOM files
import cv2

def preprocess_image(path):
    img=pdicom.read_file(path,force=True)
    imgpix=img.pixel_array

    # Scaling 16-bit pixel to 8-bits
    imgpix=((imgpix/65535)*255).astype(np.uint8)

    # Contrast enhancement
    imgpix = cv2.equalizeHist(imgpix)

    #dilation
    k1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (4, 5))
    k4 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 7))
    imgpix= cv2.dilate(imgpix,k1,iterations = 1)

    # Resizing image to (224,224)
    imgpix=cv2.resize(imgpix,(224,224))

    return imgpix
m= load_model("modelfrom11th.h5")

def add_channels(img):
    import skimage.color as color
    img=color.gray2rgb(img)
    img =img.astype('float32')
    img/=255          #  Pixel normalization (important)          #
    return img

app = Flask(__name__)

@app.route('/predict/')
def predict(path):
    img=preprocess_image(path)
    img=add_channels(img)
    pred = m.predict(img[np.newaxis])
    if pred>=0.5:
        return "Malignant"
    else:
        return "Benign"

if __name__ == '__main__':
    app.run()
