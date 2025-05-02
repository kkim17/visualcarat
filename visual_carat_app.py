import numpy as np
from sklearn.linear_model import LinearRegression
import streamlit as st

# === MODEL TRAINING SECTION ===
# Example data: [length (mm), width (mm), actual_carat], target: visual_carat
X_raw = np.array([
    [13.31, 9.36, 8.01],
    [13.23, 9.49, 7.82],
])

y = np.array([7.7, 7.79])  # visual carat values

# Derived feature: face-up area
face_up_area = X_raw[:, 0] * X_raw[:, 1]
X_features = np.column_stack((X_raw, face_up_area))

# Train linear regression model
model = LinearRegression().fit(X_features, y)

# === STREAMLIT APP SECTION ===
st.title("Emerald Cut Diamond Visual Carat Calculator")

st.markdown("""
Enter the measurements of your emerald cut diamond to estimate the **Visual Carat**, which is how large the stone appears when viewed from the top.
""")

# Input fields
length = st.number_input("Length (mm)", min_value=0.0, step=0.01, format="%.2f")
width = st.number_input("Width (mm)", min_value=0.0, step=0.01, format="%.2f")
actual_carat = st.number_input("Actual Carat Weight", min_value=0.0, step=0.01, format="%.2f")

if st.button("Calculate Visual Carat"):
    face_up_area_input = length * width
    features = np.array([[length, width, actual_carat, face_up_area_input]])
    visual_carat = model.predict(features)[0]
    st.success(f"Estimated Visual Carat: {visual_carat:.2f} ct")