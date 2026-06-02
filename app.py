# Churn : 1 = Yes, 0 = No
# Selected Features: Tenure, TotalCharges, ContractType, TechSupport

import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📊",
    layout="centered"
)

# -------------------------
# Models
# -------------------------
MODELS = {
    "Best Model": "best_classifier.pkl",
    "Logistic Regression": "logistic_model.pkl",
    "Random Forest": "randomforest_classifier.pkl",
    "Ridge Classifier": "ridge_Classifier.pkl",
    "XGBoost Classifier": "xgb_classifier.pkl"
}

# -------------------------
# Title
# -------------------------
st.title("📊 Customer Churn Prediction")

# -------------------------
# Model Selection
# -------------------------
selected_model = st.selectbox(
    "Select Model",
    list(MODELS.keys())
)

# Load selected model
try:
    model = joblib.load(MODELS[selected_model])
except Exception as e:
    st.error(f"Error loading model:\n{e}")
    st.stop()

# -------------------------
# Inputs
# -------------------------
st.subheader("Customer Information")

tenure = st.number_input(
    "Tenure (Months)",
    min_value=0,
    max_value=120,
    value=12
)

total_charges = st.number_input(
    "Total Charges",
    min_value=0.0,
    value=500.0
)

contract_type = st.selectbox(
    "Contract Type",
    ["Month-to-Month", "One Year", "Two Year"]
)

tech_support = st.selectbox(
    "Tech Support",
    ["Yes", "No"]
)

# Optional fields
with st.expander("Additional Information (Not Used For Prediction)"):

    customer_id = st.text_input("Customer ID", "CUST001")

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=30
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=50.0
    )

    internet_service = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber Optic", "No"]
    )

# -------------------------
# Predict
# -------------------------
if st.button("Predict Churn"):

    input_df = pd.DataFrame({
        "CustomerID": [""],
        "Age": [0],
        "Gender": ["Missing"],
        "Tenure": [tenure],
        "MonthlyCharges": [0],
        "ContractType": [contract_type],
        "InternetService": ["Missing"],
        "TotalCharges": [total_charges],
        "TechSupport": [tech_support]
    })

    try:
        prediction = model.predict(input_df)[0]

        st.markdown("---")

        if prediction == 1:
            st.error("⚠️ Customer is likely to Churn")
        else:
            st.success("✅ Customer is likely to Stay")

        # Probability (if supported)
        if hasattr(model, "predict_proba"):
            prob = model.predict_proba(input_df)[0][1]
            st.metric("Churn Probability", f"{prob:.2%}")

        st.subheader("Model Used")
        st.info(selected_model)

        st.subheader("Prediction Features")

        st.write({
            "Tenure": tenure,
            "TotalCharges": total_charges,
            "ContractType": contract_type,
            "TechSupport": tech_support
        })

    except Exception as e:
        st.error(f"Prediction Error:\n{e}")