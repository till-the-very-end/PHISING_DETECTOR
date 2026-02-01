import streamlit as st
import joblib
import os

# This helper function ensures we find the file in the current folder
def load_model():
    # Get the directory where THIS script (app_streamlit.py) is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(current_dir, "phishing_model.joblib")
    
    if not os.path.exists(model_path):
        st.error(f"Model file not found! I looked here: {model_path}")
        return None
    return joblib.load(model_path)

st.title("🛡️ AI Phishing Detector")
model = load_model()

if model is not None:
    text = st.text_area("Paste email text here to scan for threats:")
    if st.button("Analyze Email"):
        if not text.strip():
            st.warning("Please enter some text first.")
        else:
            # Predict
            pred = model.predict([text])[0]
            # Get the confidence score (probabilities)
            probs = model.predict_proba([text])[0]
            
            if pred == 1:
                st.error(f"🚨 PREDICTION: PHISHING (Confidence: {probs[1]*100:.2f}%)")
            else:
                st.success(f"✅ PREDICTION: SAFE (Confidence: {probs[0]*100:.2f}%)")