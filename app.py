import streamlit as st
import pickle
import pandas as pd

# Load trained model
model = pickle.load(open("random_forest_model.pkl", "rb"))

# Define selected features
selected_features = [
    "odor",
    "gill-size",
    "gill-color",
    "bruises",
    "spore-print-color",
    "ring-type",
    "population",
    "gill-spacing",
]

# ⚠️ Hardcode categories for each feature
categories = {
    "odor": ["a", "l", "c", "y", "f", "m", "n", "p", "s"],
    "gill-size": ["b", "n"],
    "gill-color": ["k", "n", "b", "h", "g", "r", "o", "p", "u", "w", "y"],
    "bruises": ["t", "f"],
    "spore-print-color": ["k", "n", "b", "h", "r", "o", "u", "w", "y"],
    "ring-type": ["c", "e", "f", "l", "n", "p", "s", "z"],
    "population": ["a", "c", "n", "s", "v", "y"],
    "gill-spacing": ["c", "w"],
    
}

st.title("🍄 Mushroom Classification App")
st.write("This app predicts whether a mushroom is **Edible** or **Poisonous** based on selected features.")

# Collect user inputs
user_input = {}
for feature in selected_features:
    user_input[feature] = st.selectbox(f"Select {feature}", categories[feature])

if st.button("Predict"):
    # Convert input to DataFrame
    input_df = pd.DataFrame([user_input])

    # Load encoder (single object) and transform
    label_encoders = pickle.load(open("label_encoders.pkl", "rb"))

    for col in selected_features:
        input_df[col] = label_encoders.fit_transform(input_df[col])

    prediction = model.predict(input_df)[0]

    if prediction == "e":
        st.success("✅ The mushroom is **Edible**")
    else:
        st.error("⚠️ The mushroom is **Poisonous**")
