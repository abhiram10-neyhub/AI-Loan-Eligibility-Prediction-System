import streamlit as st
from predict import predict_loan

st.set_page_config(
    page_title="AI Loan Eligibility Prediction",
    page_icon="🏦",
    layout="wide"
)

st.markdown("""
<style>

.stApp{
background:linear-gradient(135deg,#0f2027,#203a43,#2c5364);
}

.main-title{
text-align:center;
font-size:45px;
color:#FFD700;
font-weight:bold;
}

.sub{
text-align:center;
font-size:18px;
color:white;
margin-bottom:30px;
}

.result{
font-size:28px;
font-weight:bold;
text-align:center;
}

</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>🏦 AI Loan Eligibility Prediction System</div>", unsafe_allow_html=True)
st.markdown("<div class='sub'>AI Powered Loan Approval Prediction</div>", unsafe_allow_html=True)

left,right = st.columns(2)

with left:

    gender = st.selectbox("👤 Gender",["Male","Female"])

    married = st.selectbox("💍 Married",["Yes","No"])

    education = st.selectbox("🎓 Education",
    ["Graduate","Not Graduate"])

    self_employed = st.selectbox("💼 Self Employed",
    ["Yes","No"])

    property_area = st.selectbox("🏡 Property Area",
    ["Urban","Semiurban","Rural"])

with right:

    income = st.number_input("💰 Applicant Income",0,200000,5000)

    co_income = st.number_input("💵 Co-applicant Income",0,100000,0)

    loan_amount = st.number_input("🏦 Loan Amount",0,1000,150)

    loan_term = st.selectbox("📅 Loan Term",[180,240,300,360])

    credit_history = st.selectbox("⭐ Credit History",[1,0])

st.markdown("---")

if st.button("🚀 Predict Loan Status",use_container_width=True):

    result = predict_loan(
        gender,
        married,
        education,
        self_employed,
        income,
        co_income,
        loan_amount,
        loan_term,
        credit_history,
        property_area
    )

    if result=="Approved":
        st.balloons()
        st.success("🎉 Congratulations! Loan Approved")
    else:
        st.error("❌ Sorry! Loan Rejected")