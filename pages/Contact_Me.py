import streamlit as st
from send_email import send_email
import pandas

st.header("Contact Me")

# ONLY WORKS WITH GMAIL
with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message") # Allows multi-line text
    message = f"""Subject: From {user_email}
    \n
    From: {user_email} 
    \n
    {raw_message}
    """
    button = st.form_submit_button("Submit") # Used just for forms
    if button:
        send_email(message)
        st.info("Your email was sent successfully.")