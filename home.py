from components.ui import hide_streamlit_elt, render_navbar
import streamlit as st

st.set_page_config(initial_sidebar_state="collapsed")
hide_streamlit_elt()
render_navbar()