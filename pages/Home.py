import streamlit as st

# Prevent unauthorized access
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.error("Unauthorized access. Please log in.")
    st.stop()  # Stop execution if not logged in

st.sidebar.title(f"Welcome, {st.session_state['username']}!")
selection = st.sidebar.radio("Go to", ["Composite Grader V1", "Composite Grader V2", "Composite Grader V3", "Composite Selector"])

if selection == "Composite Grader V1":
    st.switch_page("pages/Composite Grader V1.py")
elif selection == "Composite Grader V2":
    st.switch_page("pages/Composite Grader V2.py")
elif selection == "Composite Grader V3":
    st.switch_page("pages/Composite Grader V3.py")
elif selection == "Composite Selector":
    st.switch_page("pages/Composite Selector.py")
