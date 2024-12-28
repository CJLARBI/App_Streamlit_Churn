import streamlit as st
import hashlib
import json
import os

# Function to hash passwords


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to load user data


def load_user_data():
    if os.path.exists("users.json"):
        with open("users.json", "r") as file:
            return json.load(file)
    return {"users": []}

# Function to save user data


def save_user_data(user_data):
    with open("users.json", "w") as file:
        json.dump(user_data, file, indent=4)

# Function to create a new user


def create_user(username, password):
    user_data = load_user_data()
    if any(user["username"] == username for user in user_data["users"]):
        st.warning("Username already exists.")
        return False

    user_data["users"].append({
        "username": username,
        "password": hash_password(password)
    })
    save_user_data(user_data)
    st.success("Account created successfully.")
    return True

# Function to authenticate user


def authenticate_user(username, password):
    user_data = load_user_data()
    hashed_password = hash_password(password)
    return any(
        user["username"] == username and user["password"] == hashed_password
        for user in user_data["users"]
    )

# Main application


def main():
    st.set_page_config(page_title="Authentication App", layout="centered")
    st.title("Authentication System")

    # Menu options
    menu = ["Home", "Login", "SignUp"]
    choice = st.sidebar.selectbox("Menu", menu)

    # Home Page
    if choice == "Home":
        st.subheader("Home")
        st.write("Welcome to the app! Use the sidebar to navigate.")

    # Login Page
    elif choice == "Login":
        st.subheader("Login")

        if "logged_in" not in st.session_state:
            st.session_state.logged_in = False

        if not st.session_state.logged_in:
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")

            if st.button("Login"):
                if authenticate_user(username, password):
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.success(f"Welcome, {username}!")
                else:
                    st.error("Invalid username or password.")
        else:
            st.write(
                f"Hello, {st.session_state.username}! You are already logged in.")
            if st.button("Logout"):
                st.session_state.logged_in = False
                st.session_state.pop("username", None)
                st.success("You have successfully logged out.")

    # SignUp Page
    elif choice == "SignUp":
        st.subheader("Sign Up")

        new_user = st.text_input("Choose a Username")
        new_password = st.text_input("Choose a Password", type="password")

        if st.button("SignUp"):
            if create_user(new_user, new_password):
                st.info("You can now log in using your credentials.")

    # Access control for logged-in users
    if "logged_in" in st.session_state and st.session_state.logged_in:
        st.sidebar.success(f"Logged in as: {st.session_state.username}")


if __name__ == "__main__":
    main()
