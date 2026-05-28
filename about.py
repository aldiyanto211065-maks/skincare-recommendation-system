import streamlit as st

def app():

    # ===== CSS =====
    st.markdown("""
    <style>

    .info-card{
        background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);
        border-radius:15px;
        padding:2rem;
        margin-bottom:1.5rem;
        color:white;
        box-shadow:0 4px 15px rgba(0,0,0,0.1);
    }

    .white-card{
        background:white;
        border-radius:15px;
        padding:2rem;
        margin-bottom:1.5rem;
        box-shadow:0 4px 15px rgba(0,0,0,0.1);
        border:1px solid #e0e0e0;
    }

    .card-title{
        font-size:1.5rem;
        font-weight:600;
        color:#2c3e50;
        margin-bottom:1rem;
    }

    .gradient-title{
        color:white;
        margin-bottom:1rem;
    }

    .feature-item{
        background:rgba(255,255,255,0.15);
        padding:1rem;
        border-radius:10px;
        margin-bottom:10px;
    }

    .stat-box{
        background:rgba(255,255,255,0.15);
        padding:1rem;
        border-radius:12px;
        text-align:center;
    }

    .stat-number{
        font-size:2rem;
        font-weight:bold;
        display:block;
    }

    .stat-label{
        font-size:0.9rem;
    }

    .developer-section{
        background:linear-gradient(135deg,#4CAF50 0%,#45a049 100%);
        border-radius:15px;
        padding:2rem;
        color:white;
        text-align:center;
    }

    .main-header{
        text-align:center;
        padding:2rem;
        background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);
        border-radius:15px;
        color:white;
        margin-bottom:2rem;
    }

    </style>
    """, unsafe_allow_html=True)

    # ===== HEADER =====
    st.markdown("""
    <div class="main-header">
        <h1>🌟 Skincare Recommendation System</h1>
        <p>
        Sistem Rekomendasi Produk Skincare Berbasis
        Item-Based Collaborative Filtering
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ===== STATISTIK =====
    st.markdown("""
    <div class="info-card">

        <div style="display:grid;
        grid-template-columns:repeat(3,1fr);
        gap:15px;">

            <div class="stat-box">
                <span class="stat-number">8K+</span>
                <div class="stat-label">Produk Skincare</div>
            </div>

            <div class="stat-box">
                <span class="stat-number">99%</span>
                <div class="stat-label">Akurasi</div>
            </div>

            <div class="stat-box">
                <span class="stat-number">IBCF</span>
                <div class="stat-label">Metode</div>
            </div>

        </div>

    </div>
    """, unsafe_allow_html=True)

    # ===== ABOUT =====
    st.markdown("""
    <div class="white-card">

        <h2 class="card-title">
        🎯 Tentang Aplikasi
        </h2>

        <p style="color:#34495e; line-height:1.8;">

        Aplikasi ini merupakan sistem rekomendasi produk skincare
        yang membantu pengguna menemukan produk yang sesuai
        berdasarkan tingkat kemiripan antar produk.

        <br><br>

        Sistem dikembangkan menggunakan
        <strong>Streamlit</strong>,
        metode
        <strong>Item-Based Collaborative Filtering</strong>,
        <strong>Cosine Similarity</strong>,
        dan
        <strong>Weighted Sum</strong>.

        <br><br>

        Dataset mencakup lebih dari
        <strong>8.000 produk skincare</strong>
        dengan informasi lengkap seperti
        nama produk, brand, kategori,
        ingredients, dan harga.

        </p>

    </div>
    """, unsafe_allow_html=True)

    # ===== FITUR =====
    st.markdown("""
    <div class="info-card">

        <h2 class="gradient-title">
        ✨ Fitur Unggulan
        </h2>

        <div class="feature-item">
        🔍 Pencarian produk berdasarkan nama, brand, dan kategori.
        </div>

        <div class="feature-item">
        🎯 Rekomendasi personal berdasarkan kemiripan data produk.
        </div>

        <div class="feature-item">
        📊 Analisis menggunakan Cosine Similarity.
        </div>

        <div class="feature-item">
        🧮 Perhitungan Weighted Sum untuk skor rekomendasi.
        </div>

        <div class="feature-item">
        💰 Filter harga sesuai budget pengguna.
        </div>

        <div class="feature-item">
        📱 Responsive design pada berbagai perangkat.
        </div>

    </div>
    """, unsafe_allow_html=True)

    # ===== TECHNOLOGY =====
    st.markdown("""
    <div class="white-card">

        <h2 class="card-title">
        ⚙️ Teknologi yang Digunakan
        </h2>

        <p style="line-height:1.9;color:#34495e;">

        🐍 <strong>Python</strong><br>
        🌊 <strong>Streamlit</strong><br>
        🧮 <strong>Pandas & NumPy</strong><br>
        📈 <strong>Scikit-learn</strong><br>
        🎨 <strong>CSS3</strong>

        </p>

    </div>
    """, unsafe_allow_html=True)

    # ===== DEVELOPER =====
    st.markdown("""
    <div class="developer-section">

        <h2>
        👨‍💻 Mohamad Fiqih Aldiyanto
        </h2>

        <p>

        <strong>NIM:</strong> 2110651015<br>

        <strong>Program Studi:</strong>
        Teknik Informatika<br>

        <strong>Universitas:</strong>
        Universitas Muhammadiyah Jember

        <br><br>

        <em>
        Pengembangan sistem rekomendasi produk skincare
        berbasis kemiripan data.
        </em>

        </p>

    </div>
    """, unsafe_allow_html=True)

    # ===== FOOTER =====
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align:center;color:#777;">

    © 2026 Sistem Rekomendasi Produk Skincare<br>

    Dibangun menggunakan Python, Streamlit,
    Item-Based Collaborative Filtering,
    Cosine Similarity, dan Weighted Sum

    </div>
    """, unsafe_allow_html=True)
