import streamlit as st

# Prevent unauthorized access
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.error("Unauthorized access. Please log in.")
    st.stop()

st.title("Option 1 Page")
st.write("Content for Option 1")
