import pandas as pd
import random
import os

os.makedirs("data", exist_ok=True)

genders = ["Male", "Female"]

married = ["Yes", "No"]

education = ["Graduate", "Not Graduate"]

self_employed = ["Yes", "No"]

property_area = ["Urban", "Semiurban", "Rural"]

loan_status = ["Approved", "Rejected"]

rows = []

for i in range(5000):

    gender = random.choice(genders)

    marry = random.choice(married)

    edu = random.choice(education)

    employ = random.choice(self_employed)

    income = random.randint(1500, 20000)

    co_income = random.randint(0, 10000)

    loan = random.randint(50, 700)

    term = random.choice([180,240,300,360])

    credit = random.choice([0,1])

    area = random.choice(property_area)

    if credit == 1 and income > 5000:
        status = "Approved"
    else:
        status = "Rejected"

    rows.append([
        gender,
        marry,
        edu,
        employ,
        income,
        co_income,
        loan,
        term,
        credit,
        area,
        status
    ])

df = pd.DataFrame(rows, columns=[
    "Gender",
    "Married",
    "Education",
    "Self_Employed",
    "ApplicantIncome",
    "CoapplicantIncome",
    "LoanAmount",
    "Loan_Amount_Term",
    "Credit_History",
    "Property_Area",
    "Loan_Status"
])

df.to_csv("data/loan_dataset.csv", index=False)

print("✅ Dataset Created Successfully!")

print(df.head())