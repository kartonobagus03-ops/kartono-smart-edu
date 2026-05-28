import streamlit as st
import google.generativeai as genai

# Konfigurasi API
st.set_page_config(page_title="Kartono Smart Edu", layout="wide")
st.title("🎓 KARTONO FOR SMART EDU")

# Ambil API Key dari Secrets
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

# Inisialisasi Model dengan Persona
model = genai.GenerativeModel(
    model_name='gemini-1.5-pro',
    system_instruction="""
    Anda adalah asisten pribadi Kepala Sekolah yang ahli dalam pedagogi, kurikulum Merdeka, dan manajemen sekolah. 
    Gaya bahasa Anda: Profesional, empatik, praktis, dan berwibawa.
    Tugas utama Anda:
    1. Hindari bahasa yang kaku. Gunakan bahasa yang mudah dipahami guru.
    2. Fokus pada efisiensi waktu.
    3. Selalu sertakan 'Sentuhan Manusia': Ingatkan bahwa teknologi adalah alat, dan koneksi guru-murid adalah inti pendidikan.
    4. Kualitas RPP: Pastikan RPP memiliki alur berpikir (Deep Learning).
    """
)

# Antarmuka Aplikasi
tujuan = st.text_area("Masukkan Tujuan Pembelajaran:")
if st.button("Generate Modul Ajar"):
    with st.spinner("Sedang merancang modul..."):
        response = model.generate_content(tujuan)
        st.markdown(response.text)
