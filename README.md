# 🛒 Customer Purchase Prediction Based on Product Reviews

This project is a simple yet powerful AI/ML-based web app that predicts whether a customer will purchase a product or not, based on the sentiment of their written review. It uses Natural Language Processing (NLP) techniques and a classification model to provide real-time predictions.

---

## 📌 Demo
🚀 Try it live: [Add your Streamlit link here]

---

## 🔍 Problem Statement

Customer reviews are a vital part of the e-commerce decision-making process. Analyzing these reviews can help businesses predict customer behavior and make data-driven decisions.

This app aims to:
- Classify reviews as Positive or Negative
- Predict whether a customer is likely to purchase a product based on sentiment

---

## 💻 Technologies Used

| Tool           | Description                      |
|----------------|----------------------------------|
| Python         | Core programming language        |
| Streamlit      | Web app framework for deployment |
| NLP            | Text processing and analysis     |
| TF-IDF Vectorizer | Feature extraction             |
| Logistic Regression | Classification algorithm     |
| Jupyter/Colab  | Model development                |

---

## 📁 Project Structure

```bash
customer-purchase-prediction-nlp/
│
├── app.py                    # Main Streamlit app
├── model.pkl                # Trained ML model
├── tfidf.pkl                # TF-IDF vectorizer
├── sample_reviews.csv       # Sample input data
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
