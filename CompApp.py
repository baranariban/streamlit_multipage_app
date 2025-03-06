import streamlit as st

# Dummy user credentials (Replace with a real authentication system)
USER_CREDENTIALS = {"bariban": "0v6260", "gunaydin": "0v6260", "zegeuysal": "0v6260", "sertacaltinok": "0v6260"}

st.title("CompApp: Composite Application")
st.markdown("### :red[by Ali Baran Arıban]")

def login():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password", key="password_input")
    
    if st.button("Login"):
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.session_state["authenticated"] = True
            st.session_state["username"] = username
            st.rerun()  # Updated function
        else:
            st.error("Invalid username or password")

# Initialize session state
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# Show login page if user is not authenticated
if not st.session_state["authenticated"]:
    login()
else:
    # Redirect to the Home page after login
    st.switch_page("pages/Home.py")
