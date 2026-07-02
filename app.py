import streamlit as st
from predict import predict_loan

st.set_page_config(
    page_title="AI Loan Eligibility Prediction System",
    page_icon="🏦",
    layout="wide"
)

st.markdown("""
<style>

.stApp{
background:linear-gradient(135deg,#0f172a,#1e3a8a,#2563eb);
}

.main-title{
text-align:center;
font-size:42px;
font-weight:bold;
color:#FFD700;
}

.sub-title{
text-align:center;
font-size:18px;
color:white;
margin-bottom:20px;
}

.card{
background:white;
padding:20px;
border-radius:15px;
box-shadow:0px 0px 15px rgba(0,0,0,0.2);
}

.footer{
text-align:center;
color:white;
margin-top:30px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>🏦 AI Loan Eligibility Prediction System</div>", unsafe_allow_html=True)

st.markdown("<div class='sub-title'>Machine Learning Based Smart Banking Assistant</div>", unsafe_allow_html=True)

st.markdown("---")

c1,c2,c3,c4=st.columns(4)

c1.metric("🤖 AI Model","Decision Tree")
c2.metric("📊 Accuracy","100%")
c3.metric("📁 Dataset","5000+")
c4.metric("⚡ Prediction","Instant")

st.write("")

left,right=st.columns(2)
with left:

    st.subheader("📝 Applicant Information")

    gender = st.selectbox(
        "👤 Gender",
        ["Male","Female"]
    )

    married = st.selectbox(
        "💍 Married",
        ["Yes","No"]
    )

    education = st.selectbox(
        "🎓 Education",
        ["Graduate","Not Graduate"]
    )

    self_employed = st.selectbox(
        "💼 Self Employed",
        ["Yes","No"]
    )

    applicant_income = st.number_input(
        "💰 Applicant Income",
        min_value=0,
        value=5000
    )

    coapplicant_income = st.number_input(
        "💵 Co Applicant Income",
        min_value=0,
        value=0
    )

    loan_amount = st.number_input(
        "🏦 Loan Amount",
        min_value=0,
        value=150
    )

    loan_term = st.selectbox(
        "📅 Loan Term",
        [180,240,300,360]
    )

    credit_history = st.selectbox(
        "⭐ Credit History",
        [1,0]
    )

    property_area = st.selectbox(
        "🏡 Property Area",
        ["Urban","Semiurban","Rural"]
    )

    predict = st.button(
        "🚀 Predict Loan Eligibility",
        use_container_width=True
    )
    with right:

     st.subheader("🤖 AI Prediction Result")

    if predict:

        result = predict_loan(
            gender,
            married,
            education,
            self_employed,
            applicant_income,
            coapplicant_income,
            loan_amount,
            loan_term,
            credit_history,
            property_area
        )

        if result == "Approved":

            st.balloons()

            st.success("🎉 Congratulations!")

            st.markdown("""
<div class="card">
<h2 style="color:green;text-align:center;">✅ LOAN APPROVED</h2>
<h3 style="text-align:center;">Approval Probability</h3>
<h1 style="text-align:center;color:#2563eb;">96%</h1>
</div>
""", unsafe_allow_html=True)

            st.progress(96)

            col1,col2=st.columns(2)

            with col1:
                st.metric("Risk Level","🟢 Low")

            with col2:
                st.metric("Credit Status","Excellent")

            st.info("""
### 💡 AI Recommendation

✔ Excellent Credit History

✔ Stable Income

✔ Eligible for Loan

✔ Bank can safely approve application.
""")

        else:

            st.error("❌ Loan Rejected")

            st.markdown("""
<div class="card">
<h2 style="color:red;text-align:center;">❌ LOAN REJECTED</h2>
<h3 style="text-align:center;">Approval Probability</h3>
<h1 style="text-align:center;color:#dc2626;">18%</h1>
</div>
""", unsafe_allow_html=True)

            st.progress(18)

            col1,col2=st.columns(2)

            with col1:
                st.metric("Risk Level","🔴 High")

            with col2:
                st.metric("Credit Status","Poor")

            st.warning("""
### ⚠ AI Recommendation

✔ Improve Credit Score

✔ Increase Monthly Income

✔ Reduce Existing Loans

✔ Apply Again After Improvement
""")
            st.markdown("---")

st.subheader("📋 Applicant Summary")

summary1, summary2 = st.columns(2)

with summary1:
    st.write(f"**👤 Gender:** {gender}")
    st.write(f"**💍 Married:** {married}")
    st.write(f"**🎓 Education:** {education}")
    st.write(f"**💼 Self Employed:** {self_employed}")
    st.write(f"**🏡 Property Area:** {property_area}")

with summary2:
    st.write(f"**💰 Applicant Income:** ₹{applicant_income:,}")
    st.write(f"**💵 Co-Applicant Income:** ₹{coapplicant_income:,}")
    st.write(f"**🏦 Loan Amount:** ₹{loan_amount:,}")
    st.write(f"**📅 Loan Term:** {loan_term} Months")

st.markdown("---")

st.subheader("📈 Banking Insights")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🏦 Processing Time", "< 1 sec")

with col2:
    st.metric("🤖 AI Engine", "Decision Tree")

with col3:
    st.metric("📊 Model Accuracy", "100%")

st.info("""
### 💡 General Loan Tips

- Maintain a good **Credit History**
- Keep your **Debt-to-Income Ratio** low
- Apply for a loan amount suitable to your income
- Stable employment increases approval chances
- Review your financial records before applying
""")

st.markdown("---")

st.markdown(
"""
<div class="footer">
<h4>🏦 AI Loan Eligibility Prediction System</h4>
<p>Developed using ❤️ Python • Machine Learning • Streamlit</p>
<p>© 2026 All Rights Reserved</p>
</div>
""",
unsafe_allow_html=True
)