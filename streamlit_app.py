import streamlit as st
import pandas as pd

st.title('🤖 Machine Learning App')

st.info("This is app builds a machine learning model!")
df=pd.read_csv("https://raw.githubusercontent.com/MohamedReda323/fp-machinelearning1/refs/heads/master/loan_data.csv")
df
