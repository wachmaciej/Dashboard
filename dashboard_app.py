import streamlit as st

st.write('Hello World')


col1, col2 = st.columns([3, 1])
with col1:
    st.title("YOY Dashboard")
with col2:
    st.image("logo.png", width=300)
