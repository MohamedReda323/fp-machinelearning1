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
  #person_age,person_income,person_emp_exp,loan_amnt,loan_int_rate,loan_percent_income,
  #cb_person_cred_hist_length,credit_score,loan_status
  Gender = st.selectbox("Gender",("male","female"))
  Education = st.selectbox("Education",("High School", "Associate", "Bachelor", "Master", "Doctorate"))
  Home_ownership = st.selectbox("Home ownership",("RENT", "MORTGAGE", "OWN", "OTHER"))
  loan_intent = st.selectbox("Loan intent",("EDUCATION", "MEDICAL", "VENTURE", "PERSONAL", "DEBTCONSOLIDATION", "HOMEIMPROVEMENT"))
  previous_loan_defaults_on_file = st.selectbox("Loan defaults",("Yes","No"))
  person_age = st.slider("Age",20.00,78.00,26.00,1.00)


