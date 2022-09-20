# -*- coding: utf-8 -*-
"""testPunto5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VLvS3kGpAiZiGhBFeXXEC8UWFcHHlqot
"""

from google.colab import drive
drive.mount('/content/drive')

cd '/content/drive/MyDrive/Taller_2'

import tensorflow as tf
from tensorflow import keras
from PIL import Image
import numpy as np
import os

with open('model_config.json') as json_file:
  json_config = json_file.read()
model = keras.models.model_from_json(json_config)
model.load_weights('pets_vgg19_transferlearning.h5')

data_path ='/content/drive/MyDrive/Taller_2/cats_vs_dogs_small'

set_ = 'test'
file_ = 'dog.6946.jpg'
file_path = os.path.join(data_path,set_,file_)
print(file_path)

image = tf.keras.preprocessing.image.load_img(file_path,target_size =
(150,150,3))
input_arr = tf.keras.preprocessing.image.img_to_array(image)
input_arr = np.array([input_arr]) # Convert single image to a batch.

pred = tf.keras.activations.sigmoid(model.predict(input_arr))
if pred < 0.5:
  label = 'cat'
  prob = 1-pred
else:
  label = 'dog'
  prob = pred
print(f'The pet is a {label} with probability {prob}')