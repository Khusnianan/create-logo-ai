import streamlit as st
import random
import io

st.set_page_config(page_title="🎨 Logo Ideas AI", layout="centered")
st.title("🎨 Logo Ideas AI")
st.write("Masukkan nama brand atau deskripsi untuk mendapatkan inspirasi gaya dan simbol logo.")

user_input = st.text_input("📝 Nama Brand atau Deskripsi Produk")
jumlah_ide = st.slider("🔁 Jumlah Ide Logo", 1, 5, 3)

# Ide warna, gaya, simbol, dan emoji preview
colors = ["biru laut", "hitam elegan", "emas mewah", "hijau alami", "oranye cerah", "ungu futuristik"]
styles = ["minimalis modern", "flat icon", "gaya tulisan tangan", "simbol geometris", "estetik retro", "3D emboss"]
symbols = ["daun", "bintang", "huruf inisial", "ikon rumah", "ikon teknologi", "lingkaran dinamis"]
emoji_map = {
    "daun": "🌿", "bintang": "⭐", "huruf inisial": "🔠", "ikon rumah": "🏠",
    "ikon teknologi": "💻", "lingkaran dinamis": "⭕"
}

if st.button("✨ Dapatkan Ide Logo"):
    if not user_input:
        st.warning("Silakan masukkan nama brand atau deskripsi terlebih dahulu.")
    else:
        hasil = []
        st.subheader("💡 Inspirasi Logo:")
        for i in range(jumlah_ide):
            warna = random.choice(colors)
            gaya = random.choice(styles)
            simbol = random.choice(symbols)
            emoji = emoji_map.get(simbol, "🎨")

            st.markdown(f"### 💡 Ide Logo {i+1}")
            st.markdown(f"- 🎨 Warna dominan: **{warna}**")
            st.markdown(f"- ✍️ Gaya desain: **{gaya}**")
            st.markdown(f"- 🖼️ Simbol: **{simbol}**")
            st.markdown(f"- 🔠 Preview Logo: **{emoji} {user_input}**")
            st.markdown("---")

            hasil.append(f"[Ide Logo {i+1}]\nWarna: {warna}\nGaya: {gaya}\nSimbol: {simbol}\nPreview: {emoji} {user_input}\n\n")

        # Buat file hasil
        hasil_txt = "".join(hasil)
        buffer = io.BytesIO(hasil_txt.encode("utf-8"))
        st.download_button("📥 Download Ide Logo (.txt)", data=buffer, file_name="logo_ideas.txt", mime="text/plain")

        st.info("Gunakan inspirasi ini untuk mendesain visual logo di Canva, Figma, atau ke desainer grafis.")
