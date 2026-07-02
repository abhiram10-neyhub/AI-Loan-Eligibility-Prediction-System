import joblib
import pandas as pd

model = joblib.load("models/loan_model.pkl")
encoders = joblib.load("models/label_encoders.pkl")


def predict_loan(
    gender,
    married,
    education,
    self_employed,
    applicant_income,
    coapplicant_income,
    loan_amount,
    loan_term,
    credit_history,
    property_area,
):

    gender = encoders["Gender"].transform([gender])[0]
    married = encoders["Married"].transform([married])[0]
    education = encoders["Education"].transform([education])[0]
    self_employed = encoders["Self_Employed"].transform([self_employed])[0]
    property_area = encoders["Property_Area"].transform([property_area])[0]

    sample = pd.DataFrame(
        [[
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
        ]],
        columns=[
            "Gender",
            "Married",
            "Education",
            "Self_Employed",
            "ApplicantIncome",
            "CoapplicantIncome",
            "LoanAmount",
            "Loan_Amount_Term",
            "Credit_History",
            "Property_Area"
        ]
    )

    prediction = model.predict(sample)[0]

    return encoders["Loan_Status"].inverse_transform([prediction])[0]