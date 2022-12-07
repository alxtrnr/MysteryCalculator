import streamlit as st
import time

st.header(f"The number you thought of is...")
x = len("The number you thought of is...")
time.sleep(2)
st.title(st.session_state.calculation)
st.session_state.clear()
