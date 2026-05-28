import streamlit as st

def app():
    st.title("📬 Kontak Kami")

    st.markdown("""
    Halaman ini disediakan untuk pengguna yang ingin menyampaikan pertanyaan, masukan, atau kerja sama terkait sistem rekomendasi produk skincare.
    Silakan isi formulir di bawah ini.
    """)

    with st.form(key='contact_form'):
        name = st.text_input("Nama")
        email = st.text_input("Email")
        message = st.text_area("Pesan")

        submit_button = st.form_submit_button(label='Kirim')

    if submit_button:
        if not name or not email or not message:
            st.error("Mohon isi semua kolom dengan lengkap.")
        else:
            st.success("Pesan Anda telah berhasil dikirim. Terima kasih atas partisipasinya.")
