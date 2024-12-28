import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page configuration
st.set_page_config(
    page_title="Customer Churn Prediction Dashboard",
    page_icon="📊",
    layout="wide",
)

# Load data


@st.cache_data
def load_data(file_path):
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None


file_path = 'main_df.csv'
main_df = load_data(file_path)

# Sidebar navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", ["EDA Dashboard", "Analytics Dashboard"])

# Function to create bar plots


def create_bar_plot(data, title, x_label, y_label):
    fig, ax = plt.subplots(figsize=(6, 4))
    data.plot(kind='bar', ax=ax, color='skyblue')
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    st.pyplot(fig)
    plt.close(fig)

# Function to create pie charts


def create_pie_chart(labels, counts, title, colors):
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.pie(counts, labels=labels, colors=colors,
           autopct='%1.0f%%', shadow=False)
    ax.axis('equal')
    ax.set_title(title)
    st.pyplot(fig)
    plt.close(fig)


if options == "EDA Dashboard":
    st.header("🔍 EDA Dashboard")

    if main_df is not None:
        # Contract Types
        if 'Contract' in main_df.columns:
            st.markdown("### Types of Contracts")
            contract_counts = main_df['Contract'].value_counts()
            create_bar_plot(contract_counts, "Types of Contracts",
                            "Contract Type", "Count")

        # Monthly Charges Distribution
        if 'Monthly_Charges' in main_df.columns:
            st.markdown("### Distribution of Monthly Charges")
            fig, ax = plt.subplots(figsize=(6, 4))
            sns.histplot(main_df['Monthly_Charges'],
                         kde=True, ax=ax, color='steelblue')
            ax.set_title("Distribution of Monthly Charges")
            st.pyplot(fig)
            plt.close(fig)

        # Senior Citizens Pie Chart
        if 'Senior_Citizen' in main_df.columns:
            st.markdown("### Distribution of Senior Citizens")
            senior_counts = main_df['Senior_Citizen'].value_counts()
            labels = ['Non-Senior Citizen', 'Senior Citizen']
            counts = [senior_counts.get(0, 0), senior_counts.get(1, 0)]
            create_pie_chart(labels, counts, "Distribution of Senior Citizens", [
                             '#009ACD', '#ADD8E6'])

        # Gender Distribution
        if 'Gender' in main_df.columns:
            st.markdown("### Distribution of Gender")
            gender_counts = main_df['Gender'].value_counts()
            create_bar_plot(
                gender_counts, "Distribution of Gender", "Gender", "Count")

        # Churn by Payment Method
        if 'Churn' in main_df.columns and 'Payment_Method' in main_df.columns:
            st.markdown("### Churn Rate by Payment Method")
            churn_counts = main_df.groupby('Payment_Method')[
                'Churn'].value_counts(normalize=True).unstack()
            fig, ax = plt.subplots(figsize=(10, 6))
            churn_counts.plot(kind='bar', stacked=True,
                              color=['green', 'red'], ax=ax)
            ax.set_title("Churn Rate by Payment Method")
            ax.set_xlabel("Payment Method")
            ax.set_ylabel("Churn Rate")
            ax.legend(title='Churn')
            st.pyplot(fig)
            plt.close(fig)

        # Mean Total Charges by Tenure
        if 'Tenure_Months' in main_df.columns and 'Total_Charges' in main_df.columns:
            st.markdown("### Mean Total Charges by Tenure")
            df_grp_tenure = main_df.groupby('Tenure_Months')[
                'Total_Charges'].mean().reset_index()
            df_grp_tenure_15 = df_grp_tenure.head(15)
            fig, ax = plt.subplots(figsize=(12, 6))
            sns.pointplot(data=df_grp_tenure_15, x='Tenure_Months',
                          y='Total_Charges', color='steelblue', ax=ax)
            ax.set_title("Mean Total Charges by Tenure")
            ax.set_xlabel("Tenure")
            ax.set_ylabel("Mean Total Charges")
            st.pyplot(fig)
            plt.close(fig)

elif options == "Analytics Dashboard":
    st.header("📈 Analytics Dashboard")
    st.markdown("""
        ### Model Performance Metrics
        - **Accuracy:** 82.43%
        - **Precision (No):** 0.87
        - **Recall (No):** 0.87
        - **F1-Score (No):** 0.87
        - **Precision (Yes):** 0.74
        - **Recall (Yes):** 0.73
        - **F1-Score (Yes):** 0.73
    """)

    # Confusion Matrix Visualization
    st.markdown("### Confusion Matrix")
    conf_matrix = [[645, 95], [100, 270]]
    cm_df = pd.DataFrame(conf_matrix, index=['No', 'Yes'], columns=[
                         'Predicted No', 'Predicted Yes'])
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(cm_df, annot=True, fmt='d', cmap='Blues', ax=ax)
    ax.set_title("Confusion Matrix")
    st.pyplot(fig)
