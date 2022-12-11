import streamlit as st
import time

time.sleep(2)
st.title(f'-------------- {st.session_state.calculation} --------------')
st.session_state.clear()
