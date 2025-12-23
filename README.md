# Sentiment-Based Product Recommendation System

## Project Overview
This project implements an end-to-end sentiment-based product recommendation system using machine learning and collaborative filtering techniques. The system recommends the top 5 products to a user based on both user similarity and sentiment analysis of product reviews.

## Key Components
- Data Cleaning and Preprocessing
- Text Preprocessing and Feature Extraction using TF-IDF
- Sentiment Analysis using Tuned Gradient Boosting Classifier
- User-Based Collaborative Filtering Recommendation System
- Flask Web Application Deployment

## Models Used
- Logistic Regression
- Random Forest
- XGBoost
- Gradient Boosting (Final Model)

The final model was selected based on comparative evaluation using Accuracy, Precision, Recall, F1-Score, and ROC-AUC metrics.

## Recommendation Logic
1. Generate Top 20 products using collaborative filtering
2. Predict sentiment for all reviews of these products
3. Calculate percentage of positive reviews per product
4. Recommend Top 5 products with highest positive sentiment

## Deployment
The application is deployed using **Flask** and **Docker** to ensure environment consistency and compatibility with machine learning artifacts.

Live Application URL:
👉 *(Add your Render URL here)*

## How to Run Locally
```bash
pip install -r requirements.txt
python app.py
