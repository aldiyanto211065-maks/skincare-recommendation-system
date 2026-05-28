import streamlit as st

def app():

    # ================= CSS =================
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
        margin-bottom:1rem;
        color:#2c3e50;
    }

    .gradient-title{
        color:white;
        text-shadow:2px 2px 4px rgba(0,0,0,0.3);
    }

    .feature-item{
        background:rgba(255,255,255,0.1);
        padding:1rem;
        margin-bottom:0.8rem;
        border-radius:8px;
        border-left:4px solid #ffd700;
    }

    .stat-box{
        background:rgba(255,255,255,0.1);
        border-radius:10px;
        padding:1.5rem;
        text-align:center;
        margin-bottom:1rem;
    }

    .stat-number{
        font-size:2rem;
        font-weight:bold;
        color:white;
        display:block;
    }

    .stat-label{
        color:rgba(255,255,255,0.85);
        font-size:0.9rem;
        margin-top:0.5rem;
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

    # ================= HEADER =================
    st.markdown("""
    <div class="main-header">

        <h1 style="font-size:2.5rem;margin-bottom:0.5rem;">
        🌟 Skincare Recommendation System
        </h1>

        <p style="font-size:1.2rem;opacity:0.9;">
        Sistem Rekomendasi Produk Skincare Berbasis Item-Based Collaborative Filtering
        </p>

    </div>
    """, unsafe_allow_html=True)

    # ================= STATISTICS =================
    st.markdown("""
    <div class="info-card">

        <div style="
        display:grid;
        grid-template-columns:repeat(auto-fit,minmax(150px,1fr));
        gap:1rem;">

            <div class="stat-box">
                <span class="stat-number">8K+</span>
                <div class="stat-label">
                Produk Skincare
                </div>
            </div>

            <div class="stat-box">
                <span class="stat-number">99%</span>
                <div class="stat-label">
                Akurasi Rekomendasi
                </div>
            </div>

            <div class="stat-box">
                <span class="stat-number">IBCF</span>
                <div class="stat-label">
                Metode Rekomendasi
                </div>
            </div>

        </div>

    </div>
    """, unsafe_allow_html=True)

    # ================= ABOUT =================
    st.markdown("""
    <div class="white-card">

        <h2 class="card-title">
        🎯 Tentang Aplikasi
        </h2>

        <p style="
        font-size:1rem;
        line-height:1.8;
        color:#34495e;">

        Aplikasi ini merupakan sistem rekomendasi produk skincare yang
        dirancang untuk membantu pengguna menemukan produk yang sesuai
        berdasarkan tingkat kemiripan antar produk.

        <br><br>

        Sistem dibangun menggunakan
        <strong>Streamlit</strong> sebagai framework aplikasi web
        dengan menerapkan metode
        <strong>Item-Based Collaborative Filtering</strong>,
        <strong>Cosine Similarity</strong>,
        serta pendekatan
        <strong>Weighted Sum</strong>
        untuk menghasilkan rekomendasi yang relevan dan personal.

        <br><br>

        Dataset yang digunakan mencakup lebih dari
        <strong>8.000 produk skincare</strong>
        dari berbagai merek dengan atribut lengkap seperti:

        nama produk, brand, kategori,
        kandungan utama, dan rentang harga.

        </p>

    </div>
    """, unsafe_allow_html=True)

    # ================= FITUR =================
    st.markdown("""
    <div class="info-card">

        <h2 class="gradient-title">
        ✨ Fitur Unggulan
        </h2>

        <div class="feature-item">
        <strong>🔍 Pencarian Produk:</strong>
        Temukan produk skincare berdasarkan
        nama produk, brand, maupun kategori.
        </div>

        <div class="feature-item">
        <strong>🎯 Rekomendasi Personal:</strong>
        Sistem memberikan rekomendasi berdasarkan
        tingkat kemiripan data produk
        dan preferensi pengguna.
        </div>

        <div class="feature-item">
        <strong>📊 Analisis Similarity:</strong>
        Menggunakan metode Cosine Similarity
        untuk mengukur hubungan kemiripan
        antar produk skincare.
        </div>

        <div class="feature-item">
        <strong>🧮 Perhitungan Weighted Sum:</strong>
        Digunakan untuk menghasilkan skor akhir
        rekomendasi produk yang lebih optimal.
        </div>

        <div class="feature-item">
        <strong>💰 Filter Harga:</strong>
        Membantu pengguna menemukan produk
        sesuai kebutuhan dan budget.
        </div>

        <div class="feature-item">
        <strong>📱 Responsive Design:</strong>
        Tampilan aplikasi dapat digunakan
        dengan baik pada berbagai perangkat.
        </div>

    </div>
    """, unsafe_allow_html=True)

    # ================= TECHNOLOGY =================
    st.markdown("""
    <div class="white-card">

        <h2 class="card-title">
        ⚙️ Teknologi yang Digunakan
        </h2>

        <p style="
        font-size:1rem;
        line-height:1.8;
        color:#34495e;">

        Aplikasi dikembangkan menggunakan
        beberapa teknologi pendukung berikut:

        <br><br>

        <strong>🐍 Python</strong><br>
        Bahasa pemrograman utama untuk
        pengolahan data dan implementasi metode.

        <br><br>

        <strong>🌊 Streamlit</strong><br>
        Framework untuk membangun aplikasi web interaktif.

        <br><br>

        <strong>🧮 Pandas & NumPy</strong><br>
        Digunakan untuk manipulasi,
        transformasi, dan analisis dataset.

        <br><br>

        <strong>📈 Scikit-learn</strong><br>
        Mendukung implementasi metode
        Cosine Similarity serta pemrosesan data.

        <br><br>

        <strong>🎨 CSS3</strong><br>
        Digunakan untuk styling dan tampilan antarmuka.

        </p>

    </div>
    """, unsafe_allow_html=True)

    # ================= DEVELOPER =================
    st.markdown("""
    <div class="developer-section">

        <h2 style="font-size:1.8rem;margin-bottom:1rem;">
        👨‍💻 Mohamad Fiqih Aldiyanto
        </h2>

        <div style="font-size:1.1rem;line-height:1.8;">

            <strong>NIM :</strong> 2110651015<br>

            <strong>Program Studi :</strong>
            Teknik Informatika<br>

            <strong>Universitas :</strong>
            Universitas Muhammadiyah Jember

            <br><br>

            <em>
            "Pengembangan sistem rekomendasi produk skincare
            berbasis kemiripan data untuk membantu pengguna
            menemukan produk yang sesuai."
            </em>

        </div>

    </div>
    """, unsafe_allow_html=True)

    # ================= FOOTER =================
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="
    text-align:center;
    color:#666;
    font-size:0.9rem;
    padding:1rem;">

    © 2026 Sistem Rekomendasi Produk Skincare<br>

    Dibangun menggunakan Python, Streamlit,
    Item-Based Collaborative Filtering,
    Cosine Similarity, dan Weighted Sum

    </div>
    """, unsafe_allow_html=True)
