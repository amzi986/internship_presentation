import streamlit as st
st.markdown("# Or in other words: :sunglasses:")
st.write("")
st.write("")
st.code("""
working_at_OpenSesame = True

if working_at_OpenSesame:
    career_goals = "unlocked! 🚀"
else:
    career_goals = "Preparing for Opportunity"

""", language="python")
st.sidebar.image("assets/cat.gif")
if st.button("Go to next page"):
    st.switch_page("pages/Page_5.py")