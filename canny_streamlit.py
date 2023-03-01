# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 03:01:51 2023

@author: Hamna Iftikhar
"""



import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO
import cv2
import matplotlib.pyplot as plt
import numpy as np



st.set_page_config(layout="wide")


st.sidebar.success("I have designed canny application using streamlit")


st.title("MY CANNY APP")


#number = st.slider("Pick a number", 0, 100)


    
uploaded_file = st.file_uploader("Choose a image file", type="jpg")




if uploaded_file is not None:
    # Convert the file to an opencv image.
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)

    # Now do something with the image! For example, let's display it:
    v = st.image(opencv_image, channels="BGR")
    
    if st.button(("Apply canny")):
        threshold1 = st.slider("Threshold1", min_value=0, max_value=1000, step=1, value=100)
        threshold2 = st.slider("Threshold2", min_value=0, max_value=1000, step=1, value=200)
        
        
        edges = cv2.Canny(opencv_image,threshold1,threshold2)
        st.image(edges)


if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Give Us Feedback!", st.session_state["my_input"])
submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input
    st.write("Your Comment: ", my_input)

#highThresholdRatio = 0.19
#lowThresholdRatio = 0.12
#img = cv2.imread('elephant.jpg', 0)
