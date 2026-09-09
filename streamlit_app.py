import streamlit as st
import pandas as pd

st.title('🤖 Machine Learning App')

st.info("This is app builds a machine learning model!")

with st.expander("Data"):
  st.write("**Raw Data**")
  df=pd.read_csv("https://raw.githubusercontent.com/MohamedReda323/fp-machinelearning1/refs/heads/master/loan_data.csv")
  df
  
  st.write("**X**")
  X=df.drop("loan_status",axis=1)
  X

  st.write("**y**")
  y=df.loan_status
  y

with st.expander("Data visualization"):
  st.scatter_chart(data=df, x="person_age", y="person_emp_exp", color="loan_status")

with st.sidebar:
  st.header("Input feature")
