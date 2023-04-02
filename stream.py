import tensorflow as tf
import numpy as np
import cv2
import streamlit as st

st.markdown('<style>body{color: White; background-color: DarkSlateGrey}</style>', unsafe_allow_html=True)

option = st.selectbox(
    'Which dataset do you like to use model?',
    ('deep weeds', 'horses or humans', 'svhn cropped'))

################################
######   for Deep weeds  #######
################################

if option == "deep weeds":
    deep = tf.saved_model.load('models/deepweeds')
    st.title('Deep weeds classifier')
    st.header(":blue[Using model]")
    img_file_buffer = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    if img_file_buffer is not None:
        file_bytes = np.asarray(bytearray(img_file_buffer.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
        img_array = np.array(img)
        st.image(cv2.resize(img_array, (512, 512)))


    if st.button('Predict'):
        img_array = cv2.resize(img_array, (224, 224)).astype(np.float32) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        val = deep(img_array)
        st.write(f'result: {np.argmax(val[0])}')
        st.bar_chart(val[0])


######################################
######   for Horses or humans  #######
######################################

elif option == "horses or humans":
    horse = tf.saved_model.load('models/horsehumans')
    st.title('Horses or humans classifier')
    st.header(":blue[Using model]")
    img_file_buffer = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    if img_file_buffer is not None:
        file_bytes = np.asarray(bytearray(img_file_buffer.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
        img_array = np.array(img)
        st.image(cv2.resize(img_array, (512, 512)))


    if st.button('Predict'):
        img_array = cv2.resize(img_array, (224, 224)).astype(np.float32) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        val = horse(img_array)
        st.write(f'result: {np.argmax(val[0])}')
        val = np.array([val[0], 1-val[0]])
        st.bar_chart(val)


##################################
######   for Svhn cropped  #######
##################################

else:
    svhn = tf.saved_model.load('models/svhn')
    st.title('Svhn cropped classifier')
    st.header(":blue[Using model]")
    img_file_buffer = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    if img_file_buffer is not None:
        file_bytes = np.asarray(bytearray(img_file_buffer.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
        img_array = np.array(img)
        st.image(cv2.resize(img_array, (512, 512)))


    if st.button('Predict'):
        img_array = cv2.resize(img_array, (32, 32)).astype(np.float32) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        val = svhn(img_array)
        st.write(f'result: {np.argmax(val[0])}')
        st.bar_chart(val[0])

