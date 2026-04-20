import streamlit as st
import numpy as np
from PIL import Image
import joblib
from tensorflow.keras.preprocessing.image import img_to_array

# App UI setup
st.set_page_config(page_title="Image Classification App", layout="centered")
st.title("🖼️ Image Classification App Using 4 Models")


# Load models
@st.cache_resource
def load_models():
    try:
        models = {
            "SVM": joblib.load("svm.joblib"),
            "Decision Tree": joblib.load("tree.joblib"),
            "Logistic Regression": joblib.load("logistic.joblib"),
            "Random Forest": joblib.load("rf.joblib")
        }
        return models
    except FileNotFoundError as e:
        st.error(f"❌ File not found: {e.filename}")
        return None

models = load_models()

# Image preprocessing function
def preprocess_image(img, target_size=(64, 64)):
    img = img.convert("L")               # ⚠️ Convert to grayscale to match 4096 features
    img = img.resize(target_size)        # resize  
    img_array = img_to_array(img) / 255.0
    return img_array.reshape(1, -1)      #(1, 4096)

# File upload interface
uploaded_file = st.file_uploader("📤 Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file and models:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="✅ Image uploaded", use_column_width=True)

    processed_image = preprocess_image(image)
    
    st.subheader(" buildings: 0, forest: 1, glacier: 2")
    st.subheader("🔍 Prediction Results:")
    for model_name, model in models.items():
        prediction = model.predict(processed_image)[0]            # prediction
        st.write(f"🔹 {model_name} predicts: **{prediction}**")   # result
