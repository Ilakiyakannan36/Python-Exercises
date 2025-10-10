import streamlit as st

st.title("Hello Streamlit")
st.write("This is a simple interactive app.")

# Corrected input function
name = st.text_input("Enter your name")

if st.button("Greet"):
    st.success(f"Hello, {name}")
