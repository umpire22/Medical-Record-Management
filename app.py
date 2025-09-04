import streamlit as st
import pandas as pd

st.set_page_config(page_title="Medical Record Management", layout="wide")

st.title("🏥 **Medical Record Management Agent**")
st.markdown("""
Upload patient records, search for a specific patient, and generate reports about their medical history.
""")

uploaded_file = st.file_uploader("Upload Medical Records (CSV/Excel)", type=["csv", "xlsx"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('csv') else pd.read_excel(uploaded_file)
    st.write("### 📋 **Data Preview**")
    st.dataframe(df.head())

    patient_id = st.text_input("Enter Patient ID to Search")

    if patient_id:
        patient_data = df[df["Patient_ID"] == patient_id]

        if not patient_data.empty:
            st.markdown("### 🩺 **Patient Record Found**")
            st.write(patient_data)

            # --- Simple Summary ---
            name = patient_data.iloc[0]["Name"]
            condition = patient_data.iloc[0]["Condition"]
            last_visit = patient_data.iloc[0]["Last_Visit"]

            st.markdown("### 📑 **Summary Report**")
            st.write(f"**Name:** {name}")
            st.write(f"**Condition:** {condition}")
            st.write(f"**Last Visit:** {last_visit}")
        else:
            st.warning("No record found for the given Patient ID.")
