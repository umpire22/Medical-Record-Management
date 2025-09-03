import streamlit as st
import pandas as pd

# --- PAGE CONFIG ---
st.set_page_config(page_title="Medical Record Management", layout="wide", initial_sidebar_state="expanded")

# --- TITLE & DESCRIPTION ---
st.title("🏥 **Medical Record Management Agent**")
st.markdown("""
This agent helps organize and manage medical records. Users can upload patient data, retrieve medical histories, and generate reports for patient follow-ups.
""", unsafe_allow_html=True)

# --- FILE UPLOADER ---
st.subheader("🔼 **Upload Medical Records (CSV/Excel)**")
uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('csv') else pd.read_excel(uploaded_file)
    st.write("### **Patient Data Preview**")
    st.write(df.head())

    # --- SEARCH PATIENT ---
    patient_id = st.text_input("Enter Patient ID to Search")
    if patient_id:
        patient_data = df[df["Patient_ID"] == patient_id]
        if not patient_data.empty:
            st.write("### 🩺 **Patient Record**")
            st.write(patient_data)
        else:
            st.write("No record found for the given Patient ID.")
            
    # --- DOWNLOAD BUTTON ---
    st.download_button(
        label="Download Medical Records",
        data=df.to_csv(index=False),
        file_name="medical_records.csv",
        mime="text/csv"
    )

# --- STYLING ---
st.markdown("""
    <style>
    body {
        background-color: #1e1e1e;
        color: white;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
    }
    .stTextInput, .stFileUploader {
        background-color: #333;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)
