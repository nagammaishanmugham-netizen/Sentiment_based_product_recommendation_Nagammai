import pandas as pd
from joblib import load

# =========================
# LOAD ARTIFACTS (ONCE)
# =========================

# Sentiment model + TF-IDF
vectorizer = load("vectorizer.joblib")
sentiment_model = load("final_sentiment_model.joblib")

# User-user recommendation matrix
recommend_matrix = load("pickle_files/user_final_rating.pkl")

# Product data
product_df = pd.read_csv("sample30.csv")

# =========================
# SENTIMENT PREDICTION
# =========================

def predict_sentiment(text_series):
    """
    text_series: pandas Series of raw review text
    returns: numpy array of predictions (0/1)
    """
    X = vectorizer.transform(text_series)
    return sentiment_model.predict(X)

# =========================
# RECOMMEND PRODUCTS
# =========================

def recommend_products(user_name):
    """
    Returns DataFrame with product name, review text, sentiment
    """

    # Top 20 products for the user
    product_list = (
        recommend_matrix.loc[user_name]
        .sort_values(ascending=False)
        .head(20)
        .index
        .tolist()
    )

    # Filter product reviews
    output_df = product_df[product_df["name"].isin(product_list)][
        ["name", "reviews_text"]
    ].copy()

    # Predict sentiment on RAW text
    output_df["predicted_sentiment"] = predict_sentiment(
        output_df["reviews_text"]
    )

    return output_df

# =========================
# TOP 5 PRODUCTS
# =========================

def top5_products(df):
    """
    df: output of recommend_products()
    returns: DataFrame with top 5 product names
    """

    sentiment_summary = (
        df.groupby(["name", "predicted_sentiment"])
        .size()
        .reset_index(name="count")
    )

    total_reviews = (
        df.groupby("name")
        .size()
        .reset_index(name="total")
    )

    merged = pd.merge(
        sentiment_summary,
        total_reviews,
        on="name"
    )

    merged["percentage"] = (
        merged["count"] / merged["total"]
    ) * 100

    top5 = (
        merged[merged["predicted_sentiment"] == 1]
        .sort_values(by="percentage", ascending=False)
        .head(5)
        [["name"]]
    )

    return top5
