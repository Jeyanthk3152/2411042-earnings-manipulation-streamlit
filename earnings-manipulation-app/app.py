import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Earnings Manipulation ML Models", layout="wide")

st.title("Earnings Manipulation Detection using ML Models")

with open("2411042_EARNINGS_MANIPULATION_ML_MODELS.html", "r", encoding="utf-8") as f:
    html_data = f.read()

components.html(html_data, height=1200, scrolling=True)