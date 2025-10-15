# nomogram_streamlit_app.py
import streamlit as st
import numpy as np
import os
from PIL import Image

import base64

# Encode image file to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        b64_string = base64.b64encode(img_file.read()).decode()
    return f"data:image/png;base64,{b64_string}"


# -------------------------
# Risk & point mapping table
# -------------------------
risk_table = {
    205: 0.001, 214: 0.010, 220: 0.050, 223: 0.100, 226: 0.200, 
    228: 0.300, 230: 0.400, 231: 0.500, 233: 0.600, 234: 0.700, 
    236: 0.800, 239: 0.900, 242: 0.950, 249: 0.990
}

point_table = {
    "age": {">6": 0, "≤6": 40},
    "sex": {"Male": 0, "Female": 46},
    "cancer": {"ALL": 0, "AML": 56, "Brain tumor": 5, "Lymphoma": 100,
               "Neuroblastoma": 54, "Others": 3},
    "pr": {"<122 beats/min": 0, "≥122 beats/min": 86}
}

# -------------------------
# Functions
# -------------------------
def calculate_total_points(age, sex, cancer, pr):
    """Calculate total points"""
    return (point_table["age"][age] + 
            point_table["sex"][sex] + 
            point_table["cancer"][cancer] + 
            point_table["pr"][pr])

def calculate_risk(total_points):
    """Calculate risk"""
    points_list = sorted(risk_table.keys())
    
    if total_points <= min(points_list):
        return min(risk_table.values())
    elif total_points >= max(points_list):
        return max(risk_table.values())
    else:
        # Linear interpolation
        for i in range(len(points_list) - 1):
            if points_list[i] <= total_points <= points_list[i + 1]:
                x1, x2 = points_list[i], points_list[i + 1]
                y1, y2 = risk_table[x1], risk_table[x2]
                return y1 + (y2 - y1) * (total_points - x1) / (x2 - x1)
        return 0.0

# -------------------------
# Streamlit App
# -------------------------
st.title("Nomogram Risk Calculator")

# Sidebar - Risk factors
st.sidebar.header("Risk factors")

age = st.sidebar.selectbox("Age:", options=[">6", "≤6"])
sex = st.sidebar.selectbox("Sex:", options=["Male", "Female"])
cancer = st.sidebar.selectbox("Cancer Type:", 
                              options=["ALL", "AML", "Brain tumor", "Neuroblastoma", "Lymphoma", "Others"])
pr = st.sidebar.selectbox("Pulse Rate (PR):", options=["<122 beats/min", "≥122 beats/min"])

calc_button = st.sidebar.button("Calculate", type="primary")

## Main Panel
# --- Nomogram image
# img_path = "nomogram.png"
# image = Image.open(img_path)
# st.image(image, caption="Nomogram for Bacteremia in patients with Persistent Neutropenic Fever.", use_container_width=False)

# HTML
b64_image = get_base64_image("nomogram.png")
st.markdown(
    f"""
    <div style="text-align: center;">
        <img src="{b64_image}" style="max-width: 100%; height: auto;" />
        <p style="font-size: 0.9em; color: gray;">Nomogram for Bacteremia in patients with Persistent Neutropenic Fever.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Calculate and display results
if calc_button:
    # Calculate total points
    total_points = calculate_total_points(age, sex, cancer, pr)
    
    # Calculate risk
    predicted_risk = calculate_risk(total_points)
    
    # Display results
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Total Points", f"{total_points}", border=True)
    
    with col2:
        st.metric("Predicted Risk", f"{predicted_risk:.4f}", border=True)
    
    # Risk probability visualization
    st.subheader("Risk Probability Visualization")
    st.progress(min(predicted_risk, 1.0))
    
    # Details
    with st.expander("Score Details"):
        st.write(f"**[Total] {total_points} points**")
        st.write(f"- Age ({age}): {point_table['age'][age]} points")
        st.write(f"- Sex ({sex}): {point_table['sex'][sex]} points")
        st.write(f"- Cancer Type ({cancer}): {point_table['cancer'][cancer]} points")
        st.write(f"- Pulse Rate ({pr}): {point_table['pr'][pr]} points")
        

else:
    st.info("👈 Please select variables in the sidebar and click the 'Calculate' button.")


