# main.py
import streamlit as st
import time
from generate_label import get_label


def main():

    st.set_page_config(
        page_title="Aplikasi Kategori Berita | Klasifikasi Berita Radar Jatim", page_icon="📺")

    col1, col2 = st.columns(2)

    with col1:

        st.image("assets/banner.png", use_column_width=True)

    with col2:
        st.subheader("Aplikasi Kategori untuk Berita")
        st.caption("Berita umumnya dikategorikan menjadi beberapa jenis category yaitu Ekonomi Bisnis, Hukum dan Kriminal, Pendidikan. Dengan news classification ini kita dapat menemukan jenis kategori berita yang sesuai dengan isi berita tersebut.")

    news_text = st.text_area(
        "Masukkan Isi Berita", key="input_text", height=250)

    if st.button("Cari Kategori"):
        if news_text:
            text = get_label(news_text)
            with st.expander('Tampilkan Hasil'):
                st.write('Berita yang anda masukkan termasuk dalam kategori: ')
                if text == "Ekonomi Bisnis":
                    st.info(text)
                    url = "https://www.google.com/search?q=berita+ekonomi-bisnis+radarjatim+hari+ini"
                    st.write(
                        'Baca juga berita terbaru terkait Ekonomi Bisnis [Berita Ekonomi Bisnis hari ini](%s)'  %url)
                elif text == "Hukum dan Kriminal":
                    st.info(text)
                    url = "https://www.google.com/search?q=berita+hukum-dan-kriminal+radarjatim+hari+ini"
                    st.write(
                        'Baca juga berita terbaru terkait Hukum dan Kriminal [Berita Hukum dan Kriminal hari ini](%s)'  %url)
                elif text == "Pendidikan":
                    st.info(text)
                    url = "https://www.google.com/search?q=berita+pendidikan+radarjatim+hari+ini"
                    st.write(
                        'Baca juga berita terbaru terkait pendidikan [Berita Pendidikan hari ini](%s)'  %url)
               
        else:
            time.sleep(.5)
            st.toast('Masukkan teks terlebih dahulu')


if __name__ == "__main__":
    main()