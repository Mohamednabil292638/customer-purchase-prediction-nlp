import streamlit as st
import pandas as pd
from textblob import TextBlob

# Load your product dataset
def load_data():
    return pd.read_csv("1429_1.csv")


# Sentiment analysis function
def analyze_sentiment(review):
    blob = TextBlob(review)
    return blob.sentiment.polarity  # Returns value between -1 (negative) and 1 (positive)

# Main app
def main():
    st.title("🛍️ Product Review Analyzer & Recommendation")
    st.write("Analyze your product review sentiment and get smart recommendations!")

    # Load data
    df = load_data()

    # User input
    review_text = st.text_area("✍️ Enter your product review here:")
    rating = st.slider("⭐ Rate the product (1 to 5):", 1, 5, 3)

    if st.button("Analyze"):
        if not review_text.strip():
            st.warning("Please enter a review to analyze.")
            return

        # Analyze sentiment
        sentiment_score = analyze_sentiment(review_text)
        st.write(f"**Sentiment Score:** {round(sentiment_score, 2)}")

        # Classify customer intention
        if sentiment_score > 0.2 and rating >= 3:
            st.success("✅ Customer is likely to buy.")
        elif sentiment_score < -0.2 and rating <= 2:
            st.error("❌ Customer is not likely to buy.")
        else:
            st.info("🤔 Customer is neutral or undecided.")

        # Filter best products based on existing data
        best_products = df[df['reviews.rating'].between(1, 5, inclusive='both')]
        best_products['sentiment_score'] = best_products['reviews.text'].fillna("").apply(analyze_sentiment)

        # Recommend top 3 similar products from the dataset
        st.subheader("🔍 Matching Product Recommendations")
        similar_products = best_products[
            (best_products['sentiment_score'] > sentiment_score - 0.1) &
            (best_products['sentiment_score'] < sentiment_score + 0.1) &
            (best_products['reviews.rating'] == rating)
        ]

        if not similar_products.empty:
            top_recommendations = similar_products['name'].value_counts().head(3).index.tolist()
            for i, prod in enumerate(top_recommendations, 1):
                st.write(f"{i}. {prod}")
        else:
            st.write("No exact matches found, but try adjusting the rating or review text.")

# Run the app
if __name__ == "__main__":
    main()
