import streamlit as st

st.header(f"The number you thought of is... {st.session_state['calculation']}!")
st.session_state.clear()
