import streamlit as st
from PIL import Image

st.write("heyy")

st.header("Check for Brain Tumor with XAi (GradCam) using MRI scans")

# Upload image
image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Handle image classification
if image:
    img = Image.open(image)
    st.image(img, caption="Uploaded Image").resize((250,250))

col1, col2 = st.columns(2)

if st.button("Check for tumor"):
    with col1:
        st.header("Tumor is Present")
        st.image(  Image.open('E:\mri_brain_tumor_xai_gradcam\yes.jpg').resize((250,250)),
                use_column_width=False,
                caption="Tumor Present (Given Image)")

    with col2:
        st.header("GradCam XAi")
        st.image( Image.open('E:\mri_brain_tumor_xai_gradcam\gradcam.jpg').resize((250,250)),
                use_column_width=False,
                caption="GradCam XAi")

