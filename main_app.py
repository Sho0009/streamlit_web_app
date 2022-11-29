import streamlit as st
from PIL import Image

st.title('Shoのアプリ')
st.caption('これはアプリ開発の学習です。')

image = Image.open('./data/image_1.jpg')
st.image(image, width=200)