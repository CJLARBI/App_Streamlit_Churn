import streamlit as st 
st.set_page_config(
    page_title="About App",
    page_icon="🏡",
    layout="wide"
)
# Main Content
st.title("Customer Churn Prediction App")
st.markdown("""
This application leverages machine learning models to predict customer churn. It helps businesses identify potential churn risks and take proactive measures to retain valuable customers.
""")

# Key Features
st.subheader("Key Features")
st.markdown("""
- **Data Integration**: Connect to SQL Server to fetch and analyze customer data.
- **Feature Selection**: Choose relevant features for classification.
- **Model Performance Report**: Access a detailed report on model performance.
- **Interactive Charts**: Visualize feature importance and churn probabilities with interactive charts.
""")

# App Features
st.subheader("App Navigation")
st.markdown("""
1. **About This App**: Overview of the application's purpose and functionality.
2. **View Data**: Explore the dataset and understand the customer attributes.
3. **Dashboard**: Visualize key metrics and insights from the data.
4. **Prediction**: Make individual predictions on customer churn.
5. **History Page**: Review past predictions and their outcomes.
""")

# How to Run the App
st.subheader("Running the App")
st.code(""" 
# Activate the virtual environment
venv/Scripts/activate

# Run the Streamlit app
streamlit run app.py
""", language='python')

# Machine Learning Integration
st.subheader("Machine Learning Integration")
st.markdown("""
- **Model Selection**: Choose from various machine learning models for prediction.
- **Prediction**: Generate predictions for individual customers based on their data.
- **Seamless Integration**: Easily incorporate predictions into your business workflow.
- **Insights and Visualization**: Gain valuable insights through interactive charts and graphs.
""")

# Contact and Github Repository
st.subheader("Need Help or Collaboration?")
st.markdown("""
For collaboration or support, please contact Team Fiji.
""")
if st.button("Visit Our GitHub Repository"):
    st.markdown("[GitHub Repository](https://github.com/your-repo-link)")
