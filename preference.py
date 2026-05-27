import streamlit as st

def app(df):

    st.title("🧴 Pilih Produk Skincare")

    product_list = sorted(df['Product Name'].dropna().unique())

    selected_product = st.selectbox(
        "Pilih Produk:",
        product_list
    )

    top_n = st.slider(
        "Jumlah rekomendasi",
        1,
        10,
        5
    )

    if st.button("🔍 Cari Rekomendasi"):

        st.session_state['selected_product'] = selected_product
        st.session_state['top_n'] = top_n

        st.success(
            "Preferensi berhasil disimpan. "
            "Silakan buka halaman Recommendation Result."
        )
