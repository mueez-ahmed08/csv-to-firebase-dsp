import streamlit as st
import pandas as pd
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate("firebase-key.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

st.title("CSV Upload to Firebase 🚀")

# Upload file
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.write("Preview of Data:")
    st.dataframe(df)

    if st.button("Upload to Firebase"):
        for i, row in df.iterrows():
            db.collection("csv_data").add(row.to_dict())
        
        st.success("Data uploaded successfully! 🎉")