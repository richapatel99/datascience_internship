import streamlit as st
import os

st.set_page_config(layout="centered")

title = "<h1 style='color: white;'>Explore the Great Pubs in UK</h1>"
st.markdown(title, unsafe_allow_html=True)
subtitle = "<h2 style='color: white;'>By: Richa Patel</h2>"
st.markdown(subtitle, unsafe_allow_html=True)

# st.write("By: **Richa Patel**")


#Background Image
page_bg_img = '''
<style>
.stApp {
background-image: url("https://theoxfordmagazine.com/wp-content/uploads/angels-cocktail-bar-oxford-02.jpg");
background-size: cover;
background-position: top center;
background-repeat: no-repeat;
background-attachment: local;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)