import streamlit as st
st.sidebar.image("Sesamelogo.png")
st.title("Hello! :wave:", text_alignment= 'left') #
st.title("Welcome to my presentation!", text_alignment= 'left')
if st.button("Go to next page"):
    st.switch_page("pages/Page_2.py")