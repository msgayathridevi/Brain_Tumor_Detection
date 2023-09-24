import streamlit as st
import tensorflow as tf
from PIL import Image
import requests
from io import BytesIO
from tensorflow.keras.models import load_model

model = load_model('E:/mri_brain_tumor_xai_gradcam/deployment/saved_modell.h5')


image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if image:
    img = Image.open(image)
    st.image(img, caption="Uploaded Image", use_column_width=True)
    
    
