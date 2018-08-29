# Breast Cancer Screening using a Deep Learning Architecture

A final year project in the making. We employ a Resnet34 model using the Fast AI library to distinguish between benign and malignant tumors. The model was trained using Google's Colaboratory

# Contents

  - check.ipynb : Used to experiment and research with different procedures and functions.
  - create_dataset.py : Used to create the dataset and store it as an HDF5 file.
  - plan.txt : A list of observations and strategies taken up in the making of this project.
  - main_woMM.csv : A CSV file containing metadata on all cases (except Malignant Mass tumors).
  - model.ipynb : Notebook that loads the dataset and trains/tests the model. Inference is also done. Has to be run on Google Colaboratory.
  - utility.py : Contains helpful functions.
  - extract_data.ipynb (not entirely functional) : Notebook to extract the image from the DDSM directory on drive and separate it into separate folders.
  - data/images.1227.hfd5 : The dataset in a HDF5 file that contains about 1227 ROI images of calcification tumor cases.

# License
----

AGPL - 3.0
