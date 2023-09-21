import streamlit as st
import numpy as np
import pandas as pd
import numpy as np
import tensorflow as tf
import keras
from PIL import Image
import os
from streamlit_image_select import image_select

    

model = keras.models.load_model('model13classes.h5')

class_names =['Ants',
 'Chubby Chernobyl ',
 'Humpy',
 'Prince Nymph',
 'Rubber Legs',
 'San Juan worm',
 'Stimulator',
 'Woolly bugger ',
 'elk hair caddis',
 'madam x',
 'parachute Adams',
 'pheasant tail nymph',
 'royal Wulff']



imageViewNames = []
for image in os.listdir('ExtraTest'): 
   
    image_path = os.path.join('ExtraTest', image)
    print(image_path)
    imageViewNames.append(Image.open(image_path))
   
        

img = image_select(
    label="Select an image",
    images=imageViewNames,
    captions = ['Wooly Bugger', 'Pheasant Tail Nymph','Parachute Adams', 'San Juan Worm', 'Madam X', 'Wooly Bugger','Ant',
                'Elk Hair Caddis','Parachute Adams','Ant', 'Prince Nymph', 'Rubber Legs', 'San Juan Worm', 'Madam X',
                'Elk Hair Caddis', 'Stimulator', 'Chubby Chernobyl' , 'Humpy' ]

)



img = img.resize((256, 256))
img_rgb = img.convert('RGB')
img_array = np.array(img_rgb)
img_array = np.expand_dims(img_array,0)

pred = model.predict(img_array)

st.header("Prediction: " + class_names[np.argmax(pred)])



