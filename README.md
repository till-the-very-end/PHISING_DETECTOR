# 🛡️ AI-Powered Phishing Email Detector

A machine learning-based security tool that classifies emails as **Safe** or **Phishing** using Natural Language Processing (NLP). This project was developed to demonstrate the application of AI in cybersecurity threats detection.

## 🚀 Live Demo
[Insert your Streamlit Cloud Link Here, e.g., https://prachi-phishing-detector.streamlit.app]

## 📌 Project Overview
Phishing remains one of the most common cyber-attack vectors. This project implements a supervised machine learning model to analyze the text content of emails and predict the probability of a phishing attempt.

### Key Features:
* **Machine Learning Pipeline:** Utilizes `Scikit-Learn` for model training and inference.
* **NLP Techniques:** Implements **TF-IDF Vectorization** (Term Frequency-Inverse Document Frequency) to convert raw text into numerical features.
* **User Interface:** A clean, interactive web dashboard built with **Streamlit**.
* **Real-time Prediction:** Provides a classification label and a confidence percentage for every input.

## 🛠️ Tech Stack
* **Language:** Python 3.9+
* **Libraries:** Pandas, Scikit-Learn, Joblib
* **Frontend:** Streamlit
* **Model:** Logistic Regression (optimized for binary classification)

## 🏗️ Architecture
The system follows a standard ML pipeline:
1. **Data Preprocessing:** Cleaning text and removing stop words.
2. **Feature Extraction:** Using `TfidfVectorizer` to capture word importance and context (unigrams/bigrams).
3. **Classification:** A Logistic Regression model trained on real-world phishing datasets.
4. **Serialization:** Model persistence using `joblib` for fast loading in production.



## 💻 Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/Phishing-Detector.git](https://github.com/your-username/Phishing-Detector.git)
   cd Phishing-Detector
