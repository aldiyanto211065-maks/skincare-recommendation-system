import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

@st.cache_data
def load_data():
    df = pd.read_csv("skincare_dataset_8000_clean.csv")
    return df

def preprocess_data(df):

    df = df.copy()

    df.fillna("", inplace=True)

    df['combined'] = (
        df['Product Name'].astype(str).str.lower() + ' ' +
        df['Brand'].astype(str).str.lower() + ' ' +
        df['Category'].astype(str).str.lower() + ' ' +
        df['Main Ingredients'].astype(str).str.lower()
    )

    return df

@st.cache_resource
def compute_similarity(df):

    vectorizer = TfidfVectorizer(
        stop_words='english',
        max_features=5000
    )

    tfidf_matrix = vectorizer.fit_transform(df['combined'])

    similarity_matrix = cosine_similarity(tfidf_matrix)

    return similarity_matrix

def get_recommendations(product_name, df, similarity_matrix, top_n=5):

    product_name = product_name.lower()

    matches = df[df['Product Name'].str.lower() == product_name]

    if matches.empty:
        return None, None

    idx = matches.index[0]

    sim_scores = list(enumerate(similarity_matrix[idx]))

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    sim_scores = sim_scores[1:top_n + 1]

    product_indices = [i[0] for i in sim_scores]

    scores = [i[1] for i in sim_scores]

    recommended_products = df.iloc[product_indices]

    return recommended_products, scores
