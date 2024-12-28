import streamlit as st

# Set Page Configuration
st.set_page_config(
    page_title="About App",
    page_icon="🏡",
    layout="wide"
)


def home():
    """Display the home page with app details."""
    # Set the title with a larger font and center alignment
    st.markdown(
        "<h1 style='text-align: center; color: #4CAF50;'>Customer Churn Prediction App</h1>",
        unsafe_allow_html=True
    )

    # Add a subtitle
    st.markdown(
        "<h3 style='text-align: center; color: #f39c12;'>Designed by CJL</h3>",
        unsafe_allow_html=True
    )

    # Add a banner image
    st.image(
        "Customer-churn-prediction.webp",
        use_column_width=True,
        caption="Predicting customer churn to retain valuable customers."
    )

    # Provide a brief introduction of the app
    st.write(
        """
        Welcome to the Customer Churn Prediction App! This application helps you analyze customer behavior and predict churn using advanced machine learning algorithms. 
        Navigate through the app using the sidebar to view data, explore the dashboard, or make predictions.
        """
    )


# Display the home page
home()

# Key Features Section
st.subheader("Key Features")
st.markdown(
    """
    - **Data Integration**: Connect to SQL Server to fetch and analyze customer data.
    - **Feature Selection**: Choose relevant features for classification.
    - **Model Performance Report**: Access a detailed report on model performance.
    - **Interactive Charts**: Visualize feature importance and churn probabilities with interactive charts.
    """
)

# App Navigation Section
st.subheader("App Navigation")
st.markdown(
    """
    1. **About This App**: Overview of the application's purpose and functionality.
    2. **View Data**: Explore the dataset and understand the customer attributes.
    3. **Dashboard**: Visualize key metrics and insights from the data.
    4. **Prediction**: Make individual predictions on customer churn.
    5. **History Page**: Review past predictions and their outcomes.
    """
)

# How to Run the App Section
st.subheader("Running the App")
st.code(
    """ 
    # Activate the virtual environment
    venv/Scripts/activate

    # Run the Streamlit app
    streamlit run app.py
    """,
    language='bash'
)

# Machine Learning Integration Section
st.subheader("Machine Learning Integration")
st.markdown(
    """
    - **Model Selection**: Choose from various machine learning models for prediction.
    - **Prediction**: Generate predictions for individual customers based on their data.
    - **Seamless Integration**: Easily incorporate predictions into your business workflow.
    - **Insights and Visualization**: Gain valuable insights through interactive charts and graphs.
    """
)

# Contact and GitHub Repository Section
st.subheader("Need Help or Collaboration?")
st.markdown(
    """
    For collaboration or support, please contact Clement.
    """
)
if st.button("Visit My GitHub Repository"):
    st.markdown(
        "[GitHub Repository](https://github.com/CJLARBI/App_Streamlit_Churn.git)")
