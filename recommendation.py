import streamlit as st
from data_utils import get_recommendations

def app(df, similarity_matrix):

    st.title("🎯 Hasil Rekomendasi")

    if 'selected_product' not in st.session_state:
        st.warning("Silakan pilih produk terlebih dahulu di halaman Preference.")
        return

    selected_product = st.session_state['selected_product']
    top_n = st.session_state['top_n']

    rekomendasi, skor = get_recommendations(
        selected_product,
        df,
        similarity_matrix,
        top_n
    )

    if rekomendasi is None:
        st.error("Produk tidak ditemukan.")
        return

    st.subheader(f"Produk mirip dengan: {selected_product}")

    for i, row in rekomendasi.iterrows():

        st.markdown("---")

        st.write(f"### {row['Product Name']}")

        st.write(f"**Brand:** {row['Brand']}")
        st.write(f"**Category:** {row['Category']}")
        st.write(f"**Ingredients:** {row['Main Ingredients']}")
        st.write(f"**Price:** ${row['Price ($)']}")
        st.write(f"**Rating:** {row['Rating']}")

        similarity = skor[i] * 100

        st.write(f"**Similarity Score:** {similarity:.2f}%")
