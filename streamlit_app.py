import streamlit as st
import pandas as pd
import joblib
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
  person_gender = st.selectbox("Gender",("male","female"))
  person_education = st.selectbox("Education",("High School", "Associate", "Bachelor", "Master", "Doctorate"))
  person_home_ownership = st.selectbox("Home ownership",("RENT", "MORTGAGE", "OWN", "OTHER"))
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
  data = {
      "person_age": [person_age],
      "person_gender": [1 if person_gender == "male" else 0],
      "person_education": [
          1 if person_education == "High School" else
          2 if person_education == "Associate" else
          3 if person_education == "Bachelor" else
          4 if person_education == "Master" else 5
      ],
      "person_income": [person_income],
      "person_emp_exp": [person_emp_exp],
      "loan_amnt": [loan_amnt],
      "loan_int_rate": [loan_int_rate],
      "loan_percent_income": [loan_percent_income],
      "cb_person_cred_hist_length": [cb_person_cred_hist_length],
      "credit_score": [credit_score],
      "previous_loan_defaults_on_file": [1 if previous_loan_defaults_on_file == "Yes" else 0],
      "person_home_ownership_OTHER": [1 if person_home_ownership == "OTHER" else 0],
      "person_home_ownership_OWN": [1 if person_home_ownership == "OWN" else 0],
      "person_home_ownership_RENT": [1 if person_home_ownership == "RENT" else 0],
      "loan_intent_EDUCATION": [1 if loan_intent == "EDUCATION" else 0],
      "loan_intent_HOMEIMPROVEMENT": [1 if loan_intent == "HOMEIMPROVEMENT" else 0],
      "loan_intent_MEDICAL": [1 if loan_intent == "MEDICAL" else 0],
      "loan_intent_PERSONAL": [1 if loan_intent == "PERSONAL" else 0],
      "loan_intent_VENTURE": [1 if loan_intent == "VENTURE" else 0]  
  }
  input_df = pd.DataFrame(data)
with st.expander("Input features"):
  st.write("**Input Data**")
  input_df
  
xgb_model = joblib.load("xgb_model.pkl")
scaler = joblib.load("scaler.pkl")

numeric_col = ['person_age', 'person_income', 'person_emp_exp', 'loan_amnt',
       'loan_int_rate', 'loan_percent_income', 'cb_person_cred_hist_length',
       'credit_score']
input_df[numeric_col] = scaler.transform(input_df[numeric_col])


if hasattr(xgb_model, "feature_names_in_"):
  input_df = input_df.reindex(columns=xgb_model.feature_names_in_, fill_value=0)

st.subheader("Prediction")
if st.button("Predict Loan Status"):
    prediction = xgb_model.predict(input_df)
    prediction
    if prediction[0] == 0:
        st.error("Loan Rejected")
    else:
        st.success("Loan Approved!")
