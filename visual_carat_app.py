
import streamlit as st
import numpy as np

st.title("Emerald Cut Diamond Visual Carat Estimator")

st.markdown("""
This app estimates the **visual carat weight** of an emerald cut diamond based on:
- Length (mm)
- Width (mm)
- Actual Carat Weight (ct)
- Table %

The visual carat represents how large a diamond appears face-up.
""")

# Inputs
length = st.number_input("Length (mm)", min_value=0.0, step=0.01)
width = st.number_input("Width (mm)", min_value=0.0, step=0.01)
actual_carat = st.number_input("Actual Carat Weight (ct)", min_value=0.0, step=0.01)
table_pct = st.number_input("Table %", min_value=0.0, max_value=100.0, step=0.1)

# Calculate face-up area
face_up_area = length * width

# Coefficients from the trained model
coefs = {
    "length": -0.9013,
    "width": -1.3270,
    "actual_carat": 0.0030,
    "table": -0.0001,
    "face_up_area": 0.1925
}
intercept = 8.1173

# Prediction
if length > 0 and width > 0 and actual_carat > 0 and table_pct > 0:
    visual_carat = (
        coefs["length"] * length +
        coefs["width"] * width +
        coefs["actual_carat"] * actual_carat +
        coefs["table"] * table_pct +
        coefs["face_up_area"] * face_up_area +
        intercept
    )
    st.subheader(f"Estimated Visual Carat: {visual_carat:.2f} ct")
else:
    st.info("Please enter all required values to calculate visual carat.")
