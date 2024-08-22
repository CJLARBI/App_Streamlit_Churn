import streamlit as st

# Initialize the USER_CREDENTIALS in session state if it doesn't exist
if 'USER_CREDENTIALS' not in st.session_state:
    st.session_state.USER_CREDENTIALS = {
        "user1": "password1",
        "user2": "password2",
    }

# Function to authenticate the user
def authenticate(username, password):
    username = username.lower()  # Ensure the username is in lowercase
    if username in st.session_state.USER_CREDENTIALS and st.session_state.USER_CREDENTIALS[username] == password:
        return True
    return False

# Function to create a new account
def create_account(username, password):
    username = username.lower()  # Ensure the username is stored in lowercase
    if username in st.session_state.USER_CREDENTIALS:
        return False  # Username already exists
    st.session_state.USER_CREDENTIALS[username] = password
    return True

# Display the create account button at the top right corner
st.markdown(
    """
    <style>
    .top-right-button {
        position: absolute;
        top: 0;
        right: 0;
        padding: 10px 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# Create account button
if st.button("Create Account", key="create_account", help="Create a new account", use_container_width=True):
    st.session_state.show_create_account = True

if not st.session_state.authenticated:
    st.title("Login")

    username = st.text_input("Username").lower()  # Ensure the username input is lowercase
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate(username, password):
            st.session_state.authenticated = True
            st.success("Login successful!")
            st.experimental_set_query_params(rerun="true")
        else:
            st.error("Invalid username or password")

    # Check if the user has clicked on the create account button
    if st.session_state.get("show_create_account"):
        with st.form("create_account_form", clear_on_submit=True):
            st.write("Create a New Account")
            new_username = st.text_input("New Username").lower()  # Force lowercase for new usernames
            new_password = st.text_input("New Password", type="password")

            create_account_button = st.form_submit_button("Create Account")
            if create_account_button:
                if new_username in st.session_state.USER_CREDENTIALS:
                    st.error("Username already exists. Please choose a different username.")
                else:
                    if create_account(new_username, new_password):
                        st.success("Account created successfully! You can now log in.")
                        st.session_state.show_create_account = False  # Close the popup after creation
                        st.experimental_set_query_params(rerun="true")
                    else:
                        st.error("Account creation failed.")
else:
    # Once authenticated, show a welcome message
    st.write("Welcome to the app!")
    
    # Option to log out
    if st.button("Logout"):
        st.session_state.authenticated = False
        st.experimental_set_query_params(rerun="true")

