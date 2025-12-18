import streamlit as st
st.sidebar.image("assets/Sesamelogo.png", width = 900)
st.title("Hello! :wave:", text_alignment= 'left') #
st.title("Welcome to my presentation!", text_alignment= 'left')
st.write("")
st.markdown("## Made by Amzar AbidHussain")
st.write("")
if st.button("Go to next page"):

    st.switch_page("pages/Page_2.py")


