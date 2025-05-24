import streamlit as st
import joblib

# Charger le modèle avec cache Streamlit
@st.cache_resource
def load_model():
    model = joblib.load("dataworth_model.joblib")
    return model
