import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="Number Plate Recognition", layout="wide")

st.title("Number Plate Recognition")

uploaded_file = st.file_uploader("Upload an image of a vehicle", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image_np = np.array(image)
    
    input_image = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Original Image")
        st.image(image, use_column_width=True)
    
    with st.spinner("Processing image..."):
        result = input_image.copy()

        
        detected_text = "ABC1234"
    
    with col2:
        st.subheader("Processed Image")
        st.image(result, use_column_width=True)
    
    st.success("Number Plate Recognition Results")
    st.markdown(f"**Detected Number Plate:** {detected_text}")
    
    st.info("Additional information can be displayed here, such as confidence scores or processing details.")
else:
    st.warning("Please upload an image to begin processing.")

st.sidebar.markdown("""
### Instructions:
1. Upload an image containing a vehicle
2. The system will process the image
3. Results will show the detected number plate

### Note:
This is a demo interface. You'll need to replace the placeholder processing code with your actual number plate recognition algorithm.
""")