import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, accuracy_score
import joblib

# --- STEP 1: LOAD DATA ---
# This is your small sample to start with
data = [
    ("Your account has been compromised. Click here to reset: http://evil.example", 1),
    ("Please verify your account immediately by clicking the link below", 1),
    ("Meeting notes for today's scrum attached.", 0),
    ("Invoice for your recent purchase attached.", 0),
    ("Urgent: Your mailbox is full. Update now http://phish.example", 1),
    ("Lunch tomorrow? 1 PM works for me.", 0),
    ("You received a secure message from Bank. Sign in: http://bank.example", 1),
    ("Weekly report attached. Great job everyone!", 0)
]

# TIP: Once you download a Kaggle CSV, you can replace the lines above with:
# df = pd.read_csv("your_kaggle_file.csv")
df = pd.DataFrame(data, columns=["text", "label"])

# --- STEP 2: SPLIT DATA ---
X_train, X_test, y_train, y_test = train_test_split(df["text"], df["label"], test_size=0.2, random_state=42)

# --- STEP 3: BUILD THE PIPELINE ---
# TF-IDF turns text into numbers; LogisticRegression decides 0 or 1
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1,2), max_features=5000)),
    ("clf", LogisticRegression(max_iter=1000))
])

# --- STEP 4: TRAIN ---
print("Training the AI model...")
pipeline.fit(X_train, y_train)

# --- STEP 5: EVALUATE ---
preds = pipeline.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, preds) * 100:.2f}%")

# --- STEP 6: SAVE ---
joblib.dump(pipeline, "phishing_model.joblib")
print("Model saved successfully as 'phishing_model.joblib'")