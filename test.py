import streamlit as st
from PIL import Image, ImageOps

st.image(Image.open("images/3-4.png").rotate(180))
st.image(ImageOps.mirror(Image.open("images/3-4.png")))
