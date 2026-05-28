import streamlit as st

def app():

    st.markdown("""
    <style>

    .info-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        color: white;
    }

    .white-card {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }

    .feature-item {
        background: rgba(255,255,255,0.1);
        padding: 1rem;
        margin-bottom: 10px;
        border-radius: 8px;
    }

    .main-header {
        text-align: center;
        padding: 2rem;
        background: linear-gradient(135deg,#667eea,#764ba2);
        color: white;
        border-radius: 15px;
        margin-bottom: 2rem;
    }

    </style>
    """, unsafe_allow_html=True)

    # ================= HEADER =================
    st.markdown("""
    <div class="main-header">
        <h1>🌟 Skincare Recommendation System</h1>
        <p>
        Sistem Rekomendasi Produk Skincare Berbasis Item-Based Collaborative Filtering
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ================= STATISTIK =================
    st.markdown("""
    <div class="info-card">

        <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:15px;">

            <div style="text-align:center;">
                <h2>8K+</h2>
                <p>Produk Skincare</p>
            </div>

            <div style="text-align:center;">
                <h2>99%</h2>
                <p>Akurasi Rekomendasi</p>
            </div>

            <div style="text-align:center;">
                <h2>IBCF</h2>
                <p>Metode</p>
            </div>

        </div>

    </div>
    """, unsafe_allow_html=True)

    # ================= ABOUT =================
    st.markdown("""
    <div class="white-card">

        <h2>🎯 Tentang Aplikasi</h2>

        <p style="line-height:1.8;color:#333;">

        Aplikasi ini merupakan sistem rekomendasi produk skincare
        yang membantu pengguna menemukan produk berdasarkan kemiripan data.

        <br><br>

        Dibangun menggunakan Streamlit dengan metode
        Item-Based Collaborative Filtering,
        Cosine Similarity, dan Weighted Sum.

        <br><br>

        Dataset berisi lebih dari 8.000 produk skincare.

        </p>

    </div>
    """, unsafe_allow_html=True)

    # ================= FITUR (FIX UTAMA KAMU) =================
    st.markdown("""
    <div class="info-card">

        <h2>✨ Fitur Unggulan</h2>

        <div class="feature-item">
        🔍 Pencarian Produk: Berdasarkan nama, brand, kategori
        </div>

        <div class="feature-item">
        🎯 Rekomendasi Personal: Berdasarkan kemiripan data produk dan preferensi pengguna
        </div>

        <div class="feature-item">
        📊 Cosine Similarity: Mengukur kemiripan antar produk
        </div>

        <div class="feature-item">
        🧮 Weighted Sum: Menghitung skor rekomendasi
        </div>

        <div class="feature-item">
        💰 Filter Harga: Sesuai budget
        </div>

        <div class="feature-item">
        📱 Responsive Design
        </div>

    </div>
    """, unsafe_allow_html=True)

    # ================= TECHNOLOGY =================
    st.markdown("""
    <div class="white-card">

        <h2>⚙️ Teknologi</h2>

        <p>
        Python, Streamlit, Pandas, NumPy, Scikit-learn
        </p>

    </div>
    """, unsafe_allow_html=True)

    # ================= DEVELOPER =================
    st.markdown("""
    <div class="white-card">

        <h2>👨‍💻 Mohamad Fiqih Aldiyanto</h2>

        <p>
        NIM: 2110651015 <br>
        Teknik Informatika <br>
        Universitas Muhammadiyah Jember
        </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align:center;color:gray;">
    © 2025 Skincare Recommendation System
    </div>
    """, unsafe_allow_html=True)
