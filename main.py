import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Danny Bui")
    content = """
    Hi, I'm Danny! I'm a student at the University of Minnesota, College of Science and Enginnering, studying Data Science. I have a great interest in all things tech but find software enginnering and data science the most interesting! I have experience in a variety of fields including backend, frontend and blockchain development.
    """
    st.info(content) # Can also use .write

st.write("Below you can find some of the apps I have built in Python. Feel free to contact me!")

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows(): # iterates through the rows of the csv file
        st.header(row["title"]) # H1 header for each title

with col4:
    for index, row in df[10:git ].iterrows():
        st.header(row["title"])