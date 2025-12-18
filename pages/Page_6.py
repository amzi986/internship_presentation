import streamlit as st
st.markdown("# AI is the next :rainbow[great chapter] of humanity.")
st.sidebar.image("assets/AI animation.gif", width = 1000000)
st.write("")
st.image("assets/AI 1.png")
st.write("")
st.image("assets/AI 2.png")
if st.button("Whats an example of a company that uses AI well?"):
    st.image("assets/OpenSesame_Full_Hor_Grd_Blk.pdf.jpg", width = 100000000)
if st.button("Next page"):
     st.switch_page("Page_7.py")