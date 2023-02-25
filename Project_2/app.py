import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os 

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# st.write(__file__)

# PARENT_DIR = os.path.join(FILE_DIR,os.pardir)
# st.write(os.pardir)

MAIN_FILE = os.path.join(FILE_DIR,"files")

IMAGE_PATH = os.path.join(MAIN_FILE,"images","heart.jpg")
# st.write(IMAGE_PATH)
# st.write(MAIN_FILE)

DATA_PATH = os.path.join(MAIN_FILE,"data","heart.csv" )

st.title("Dashboard - Heart disease")

img = image.imread(IMAGE_PATH)
# st.image(img)

df = pd.read_csv(DATA_PATH)

sex = st.selectbox("select sex:", df["Sex"].unique())
col1 , col2 = st.columns(2)

# st.write(sex)
fig_1 = px.histogram(df[df["Sex"]== sex], x = "Age", color_discrete_sequence = ['green'], title="Histogram Distribution of Age")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.bar(df[df["Sex"]== sex],x = "ChestPainType", color = "ChestPainType", title = "Types of ChestPain")
col2.plotly_chart(fig_2, use_container_width=True)

