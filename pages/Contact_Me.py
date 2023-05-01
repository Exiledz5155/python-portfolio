import streamlit as st

st.header("Contact Me")


# ONLY WORKS WITH GMAIL
with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message") # Allows multi-line text
    button = st.form_submit_button("Submit") # Used just for forms
    if button:
        print("I was pressed!")