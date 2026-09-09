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

with st. sidebar:
  st.header("Input feature")
  #credit_score,loan_status
  Gender = st.selectbox("Gender",("male","female"))
  Education = st.selectbox("Education",("High School", "Associate", "Bachelor", "Master", "Doctorate"))
  Home_ownership = st.selectbox("Home ownership",("RENT", "MORTGAGE", "OWN", "OTHER"))
  loan_intent = st.selectbox("Loan intent",("EDUCATION", "MEDICAL", "VENTURE", "PERSONAL", "DEBTCONSOLIDATION", "HOMEIMPROVEMENT"))
  previous_loan_defaults_on_file = st.selectbox("Loan defaults",("Yes","No"))
  person_age = st.slider("Age",20,78,26,1)
  person_income = st.slider("Income",8000.00,168667.12,67045.50)
  person_emp_exp = st.slider("Years of Experience",0,58,4,1)
  loan_amnt = st.slider("Loan amount",500.00,23093.12,8000.00)
  loan_int_rate = st.slider("Interest rate",5.42,19.59,11.01)
  loan_percent_income = st.slider("Loan to income ratio",0.003,0.37,0.12)
  cb_person_cred_hist_length = st.slider("Credit history length",2,15,4)
  credit_score = st.slider("Credit score",497.50,773.50,640.00)

