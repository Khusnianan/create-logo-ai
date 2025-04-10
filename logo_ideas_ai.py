import streamlit as st
import random

st.set_page_config(page_title="🎨 Logo Ideas AI", layout="centered")
st.title("🎨 Logo Ideas AI")
st.write("Masukkan nama brand atau deskripsi untuk mendapatkan inspirasi nama dan gaya logo.")

user_input = st.text_input("📝 Nama Brand atau Deskripsi Produk")

# Ide warna dan gaya
colors = ["biru laut", "hitam elegan", "emas mewah", "hijau alami", "oranye cerah", "ungu futuristik"]
styles = ["minimalis modern", "flat icon", "gaya tulisan tangan", "simbol geometris", "estetik retro", "3D emboss"]
symbols = ["daun", "bintang", "huruf inisial", "ikon rumah", "ikon teknologi", "lingkaran dinamis"]

if st.button("✨ Dapatkan Ide Logo"):
    if not user_input:
        st.warning("Silakan masukkan nama brand atau deskripsi terlebih dahulu.")
    else:
        st.subheader("💡 Inspirasi Logo:")

        st.markdown(f"**Nama Brand**: `{user_input}`")
        st.markdown(f"- 🎨 Warna dominan: **{random.choice(colors)}**")
        st.markdown(f"- ✍️ Gaya desain: **{random.choice(styles)}**")
        st.markdown(f"- 🖼️ Simbol yang cocok: **{random.choice(symbols)}**")
        st.markdown("\n")
        st.info("Gunakan ide ini untuk membuat draft visual atau disampaikan ke desainer grafis!")
