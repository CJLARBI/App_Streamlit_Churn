import streamlit as st
import pandas as pd
import pyodbc
from dotenv import dotenv_values

# Set Page Configuration
st.set_page_config(
    page_title="Data Viewer",
    page_icon="🔍",
    layout="wide"
)

# App Title and Description
st.title("🕵️ Welcome to the Data Page")
st.write("Here you can view the data retrieved from the SQL database. Use this page to explore the dataset.")

# Load environment variables from .env file
env_vars = dotenv_values('.env')

# Validate environment variables
required_vars = ['DRIVER', 'SERVER', 'DATABASE', 'UID', 'PWD']
missing_vars = [var for var in required_vars if var not in env_vars]
if missing_vars:
    st.error(f"Missing required environment variables: {
             ', '.join(missing_vars)}")
else:
    try:
        # Connect to SQL Server using credentials from .env file
        conn = pyodbc.connect(
            f"DRIVER={env_vars['DRIVER']};"
            f"SERVER={env_vars['SERVER']};"
            f"DATABASE={env_vars['DATABASE']};"
            f"UID={env_vars['UID']};"
            f"PWD={env_vars['PWD']};"
        )

        # Query the data
        query = "SELECT * FROM dbo.LP2_Telco_churn_first_3000"
        df = pd.read_sql(query, conn)

        # Display data
        st.write("### Retrieved Data")
        st.dataframe(df, use_container_width=True)

        # Close the connection
        conn.close()

    except pyodbc.Error as e:
        st.error(f"Error connecting to the database: {e}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
