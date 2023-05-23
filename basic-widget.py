#Import Library yang digunakan
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime


st.header("WIDGET DALAM STREAMLIT")

st.subheader(
   'Text Input'
)
name = st.text_input(label='Nama Lengkap', value='')
st.write('Nama: ', name)

st.subheader(
   'Text Area'
)
text = st.text_area('Feedback')
st.write('Feedback: ', text)

st.subheader(
    'Number Input'
)
number = st.number_input(label='Umur')
st.write('Umur: ', int(number), ' tahun')

st.subheader(
    'Date Input'
)
date = st.date_input(label='Tanggal Lahir', min_value=datetime.date(1900, 1, 1))
st.write('Tanggal lahir', date)

st.subheader(
    'File Uploader'
)
uploaded_file = st.file_uploader('Choose a CSV file')

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

st.subheader(
    'Camera Input'
)    
picture = st.camera_input('Take a picture')
if picture:
    st.image(picture)

st.subheader(
    'Button'
)
if st.button('Say Hello'):
    st.write('Lah elu lagi!')    

st.subheader(
    'Checkbox'
)
agree = st.checkbox('Saya gagang pintu sebenarnya') 

if agree:
    st.write('Wadu, kamu setuju!')

st.subheader(
    'Radio Button'
)
food = st.radio(
    label="What's your favourite food?",
    options=('Pukis', 'Cenil', 'Dragon Pollen')
)    

st.subheader(
    'Select Box'
)
drink = st.selectbox(
    label="What's your favourite drink?",
    options=('Ice Tea', 'Ice Drunk', 'Shaved Ice')
)

st.subheader(
    'Multiselect'
)
drink = st.multiselect(
    label="What's your favourite drink?",
    options=('Ice Tea', 'Ice Drunk', 'Shaved Ice')
)    

st.subheader(
    'Slider'
)
perasaan = st.slider('Kemampuan dalam memahami perasaan wanita', 0, 100)
st.write("Ya sekitar", perasaan,'%') 