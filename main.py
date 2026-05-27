import streamlit as st
from data_utils import load_data, preprocess_data, compute_similarity

import home
import about
import preference
import recommendation
import contact

st.set_page_config(
    page_title="Skincare Recommendation System",
    page_icon="✨",
    layout="wide"
)

def main():

    try:

        with st.spinner("📂 Memuat dan memproses data..."):

            df = load_data()
            df = preprocess_data(df)
            similarity_matrix = compute_similarity(df)

        st.sidebar.title("Menu")

        page = st.sidebar.radio(
            "Pilih Halaman:",
            [
                "Home",
                "Preference",
                "Recommendation Result",
                "About",
                "Contact"
            ]
        )

        if page == "Home":
            home.app()

        elif page == "Preference":
            preference.app(df)

        elif page == "Recommendation Result":
            recommendation.app(df, similarity_matrix)

        elif page == "About":
            about.app()

        elif page == "Contact":
            contact.app()

    except Exception as e:
        st.error(f"Terjadi error: {e}")

if __name__ == "__main__":
    main()
