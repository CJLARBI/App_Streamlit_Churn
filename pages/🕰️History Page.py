import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="Prediction History",
    page_icon="🕰️",
    layout="wide",
)

# Page title
st.title("🕰️ Prediction History")

# Display history
history = st.session_state.get('history', pd.DataFrame())

if not history.empty:
    st.dataframe(
        history,
        use_container_width=True,
        height=400,
        column_config={
            "Date": "Date",
            "Time": "Time",
            "Prediction": "Prediction",
            "Model": "Model",
            "Probability": "Confidence",
            "Interpretation": "Details",
        },
    )
else:
    st.write("No predictions have been made yet.")
