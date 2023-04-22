import streamlit as st
import pandas as pd
import numpy as np
import os

#Page Heading

st.header("🥂Pubs Information")

#Reading data
FILE_DIR1 = os.path.dirname(os.path.abspath(__file__))
FILE_DIR = os.path.join(FILE_DIR1,os.pardir)
dir_of_interest = os.path.join(FILE_DIR, "resourses")
DATA_PATH1 = os.path.join(dir_of_interest, "open_pubs_clean.csv")
df = pd.read_csv(DATA_PATH1)
with st.expander(label='Click Here to see the dataset overview',expanded=False):
    st.dataframe(df)

#Unique Bars and Local Authorities
unique=['Number of Pubs', 'Number of Local Authorities','Number of Postal Code']

option=st.radio(label="Select below options to see total count",
                options=unique,label_visibility="visible", horizontal=True)

if option=='Number of Pubs':
    st.subheader(f"Total no of Pubs in UK: :blue[{df['name'].nunique()}]")
elif option=='Number of Postal Code':
    st.subheader(f"Total no of Postal Codes in UK: :blue[{df['postcode'].nunique()}]")
else:
    st.subheader(f"Total no of Local Authorities in UK :blue[{df['local_authority'].nunique()}]")

st.markdown('<h3 style="color: #FFB6C1">🥂Cheers to a great night out! We hope our guide to the best pubs in the UK has helped you find the perfect spot to enjoy a drink and unwind🥂</h3>', unsafe_allow_html=True)
