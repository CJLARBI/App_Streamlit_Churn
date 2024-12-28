import streamlit as st
import numpy as np
import joblib
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Set page configuration
st.set_page_config(
    page_title="Predictive Analytics Dashboard",
    page_icon="🔮",
    layout="wide",
)

# Page title and subheader
st.title("🔮 Predictive Analytics Dashboard")
st.subheader("Empowering your decisions with data-driven insights")

# Load model and preprocessing components
components = joblib.load('models/churn_model_components.pkl')
preprocessor = components['preprocessing']['preprocessor']
models = components['tuned_models']

# Define default input columns
expected_columns = {
    'Gender': 'Male', 'Senior_Citizen': 'No', 'Partner': 'No', 'Dependents': 'No',
    'tenure': 0, 'Phone_Service': 'No', 'Multiple_Lines': 'No phone service',
    'Internet_Service': 'DSL', 'Online_Security': 'No internet service',
    'Online_Backup': 'No internet service', 'Device_Protection': 'No internet service',
    'Tech_Support': 'No internet service', 'Streaming_TV': 'No internet service',
    'Streaming_Movies': 'No internet service', 'Contract': 'Month-to-month',
    'Paperless_Billing': 'No', 'Payment_Method': 'Electronic check',
    'Monthly_Charges': 0.0, 'Total_Charges': 0.0
}

# Prediction function


def predict(attributes, model_name='random_forest'):
    user_data = {**expected_columns, **attributes}
    df = pd.DataFrame([user_data], columns=expected_columns.keys())
    processed_df = preprocessor.transform(df)
    pred = models[model_name].predict(processed_df)
    prob = models[model_name].predict_proba(processed_df)
    return pred[0], np.max(prob)


# Initialize session state for prediction history
if 'history' not in st.session_state:
    st.session_state.history = pd.DataFrame(
        columns=['Date', 'Time', 'Prediction', 'Model', 'Probability', 'Interpretation'])

# Input form for customer details
st.markdown("### Enter Customer Details to Predict Churn")
with st.form(key='user_input_form'):
    inputs = {
        'Gender': st.selectbox('Gender', ['Male', 'Female']),
        'Senior_Citizen': st.selectbox('Senior Citizen', ['Yes', 'No']),
        'Partner': st.selectbox('Partner', ['Yes', 'No']),
        'Dependents': st.selectbox('Dependents', ['Yes', 'No']),
        'tenure': st.slider('Tenure (in months)', 0, 100, 1),
        'Phone_Service': st.selectbox('Phone Service', ['Yes', 'No']),
        'Multiple_Lines': st.selectbox('Multiple Lines', ['Yes', 'No', 'No phone service']),
        'Internet_Service': st.selectbox('Internet Service', ['DSL', 'Fiber optic', 'No']),
        'Online_Security': st.selectbox('Online Security', ['Yes', 'No', 'No internet service']),
        'Online_Backup': st.selectbox('Online Backup', ['Yes', 'No', 'No internet service']),
        'Device_Protection': st.selectbox('Device Protection', ['Yes', 'No', 'No internet service']),
        'Tech_Support': st.selectbox('Tech Support', ['Yes', 'No', 'No internet service']),
        'Streaming_TV': st.selectbox('Streaming TV', ['Yes', 'No', 'No internet service']),
        'Streaming_Movies': st.selectbox('Streaming Movies', ['Yes', 'No', 'No internet service']),
        'Contract': st.selectbox('Contract', ['Month-to-month', 'One year', 'Two year']),
        'Paperless_Billing': st.selectbox('Paperless Billing', ['Yes', 'No']),
        'Payment_Method': st.selectbox('Payment Method', ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)']),
        'Monthly_Charges': st.number_input('Monthly Charges', 0.0, 200.0, 70.0),
        'Total_Charges': st.number_input('Total Charges', 0.0, 10000.0, 150.0)
    }

    model_choice = st.selectbox('Choose Model', list(models.keys()))
    submit_button = st.form_submit_button(label='Predict Churn')

# Handle form submission
if submit_button:
    prediction, probability = predict(inputs, model_choice)
    prediction_text = 'Churn' if prediction == 1 else 'No Churn'

    st.markdown(f"### Prediction: {prediction_text}")
    st.markdown(f"**Probability:** {probability:.2f}")

    # Probability bar chart
    fig, ax = plt.subplots()
    ax.barh(['No Churn', 'Churn'], [1 - probability,
            probability], color=['green', 'red'])
    ax.set_xlim(0, 1)
    st.pyplot(fig)

    interpretation = f"The model predicts that the customer is {
        'likely' if prediction == 1 else 'not likely'} to churn with a confidence level of {probability:.2%}."
    st.markdown("#### Interpretation")
    st.write(interpretation)

    # Log prediction to history
    current_time = datetime.now()
    new_record = pd.DataFrame({
        'Date': [current_time.strftime('%Y-%m-%d')],
        'Time': [current_time.strftime('%H:%M:%S')],
        'Prediction': [prediction_text],
        'Model': [model_choice],
        'Probability': [probability],
        'Interpretation': [interpretation],
    })
    st.session_state.history = pd.concat(
        [st.session_state.history, new_record], ignore_index=True)
