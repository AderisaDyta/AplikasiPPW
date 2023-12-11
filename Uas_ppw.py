import streamlit as st
import numpy as np
import pandas as pd
import re
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
nltk.download('punkt')
# Download kamus stop words
nltk.download('stopwords')
from sklearn.feature_extraction.text import TfidfVectorizer
# Inisialisasi TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.shortest_paths import weighted
import gdown


st.markdown("<h2 style='text-align: center;'>PTA Universitas Trunojoyo Madura</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>200411100013_Aderisa Dyta Okvianti</h4>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;'>UAS / PPW B</h6>", unsafe_allow_html=True)
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Data Berita Satu", "Data Preprocessing", "Summary" ,"Modelling", "Implementasi"])

with tab1:
        df = pd.read_csv('https://raw.githubusercontent.com/AderisaDyta/ppw/main/Crawling-DataBerita%20(2).csv')
        df1 = df[['Kategori', 'Judul', 'Tanggal', 'Link', 'Konten']]
        st.subheader('Data Berita Satu')
        st.write(df1)
with tab2:
        # Menampilkan judul di atas jumlah data
        st.markdown("<h4 style='text-align: center;'>Jumlah Data setiap Kategori</h4>", unsafe_allow_html=True)
        # Menampilkan jumlah data untuk kategori tertentu
        jumlah_sport = len(df[df['Kategori'] == 'Sport'])
        jumlah_pemilu = len(df[df['Kategori'] == 'Pemilu'])
        jumlah_lifestyle = len(df[df['Kategori'] == 'Lifestyle'])

      
        # Menampilkan hasil di Streamlit
        st.write(f"Jumlah data untuk Sport: {jumlah_sport}")
        st.write(f"Jumlah data untuk Pemilu: {jumlah_pemilu}")
        st.write(f"Jumlah data untuk Lifestyle: {jumlah_lifestyle}")

        #missing value
        df.isnull().sum()
        #hapus
        df = df.dropna()
        #duplikat
        df.duplicated().sum()
        #hapus
        df = df.drop_duplicates()
        # Menampilkan judul di atas jumlah data
        st.markdown("<h4 style='text-align: center;'>Setelah proses missing value dan Duplikat</h4>", unsafe_allow_html=True)
        df
        # Menampilkan judul di atas jumlah data
        st.markdown("<h4 style='text-align: center;'>Jumlah Data setiap Kategori setelah drop</h4>", unsafe_allow_html=True)
        # Menampilkan jumlah data untuk kategori tertentu
        jumlah_sport = len(df[df['Kategori'] == 'Sport'])
        jumlah_pemilu = len(df[df['Kategori'] == 'Pemilu'])
        jumlah_lifestyle = len(df[df['Kategori'] == 'Lifestyle'])

      
        # Menampilkan hasil di Streamlit
        st.write(f"Jumlah data untuk Sport: {jumlah_sport}")
        st.write(f"Jumlah data untuk Pemilu: {jumlah_pemilu}")
        st.write(f"Jumlah data untuk Lifestyle: {jumlah_lifestyle}")


        st.markdown("<h4 style='text-align: center;'>Cleaning Regex</h4>", unsafe_allow_html=True)
        # Membuat kolom baru untuk teks artikel yang sudah dibersihkan
        df['data_bersih'] = df['Konten'].apply(lambda x: re.sub(r'[^\w\s,.?!]', '', str(x).lower()))
        df

        st.markdown("<h4 style='text-align: center;'>Tokenizing</h4>", unsafe_allow_html=True)
        # Membuat kolom baru untuk tokenisasi teks artikel
        df['tokenizing'] = df['data_bersih'].apply(lambda x: sent_tokenize(str(x)))
        # Menampilkan DataFrame dengan kolom baru
        df

        df.reset_index(drop=True, inplace=True) #reset dari 0

with tab3:
        st.markdown("<h4 style='text-align: center;'>Data Summary</h4>", unsafe_allow_html=True)
        csv_path = 'https://raw.githubusercontent.com/AderisaDyta/AplikasiPPW/main/DataSummary'
        df = pd.read_csv(csv_path)
        df


        # Ganti 'YOUR_FILE_ID' dengan ID file Google Drive Anda
        file_id = '15Cc0wnWEXp0sKzX6CS0zVzCwUbNMdaC_'
        url = f'https://drive.google.com/uc?id=15Cc0wnWEXp0sKzX6CS0zVzCwUbNMdaC_'

        # Ganti 'output.csv' dengan nama file yang diinginkan
        output_file = 'TF-IDFSummary.csv'

        # Mengunduh file dari Google Drive
        gdown.download(url, output_file, quiet=False)


        st.markdown("<h4 style='text-align: center;'>TF-IDF Summary</h4>", unsafe_allow_html=True)

        # Baca file CSV yang telah diunduh
        df = pd.read_csv(output_file)

        # Menampilkan dataframe
        st.write(df)

with tab4:
        st.markdown("<h4 style='text-align: center;'>Hasil Modelling Menggunakan Random Forest</h4>", unsafe_allow_html=True)
        csv_path = 'https://raw.githubusercontent.com/AderisaDyta/AplikasiPPW/main/classification_results.csv'
        df = pd.read_csv(csv_path)
        df
        # Menampilkan gambar
        image_path = 'https://raw.githubusercontent.com/AderisaDyta/AplikasiPPW/main/Confusion-matrix%20RF.PNG'
        st.image(image_path, caption='Confusion Matrix - Random Forest', width=200)

        st.markdown("<h4 style='text-align: center;'>Hasil Modelling Menggunakan SVM</h4>", unsafe_allow_html=True)
        csv_path = 'https://raw.githubusercontent.com/AderisaDyta/AplikasiPPW/main/classification_results_svm.csv'
        df = pd.read_csv(csv_path)
        df
        # Menampilkan gambar
        image_path = 'https://raw.githubusercontent.com/AderisaDyta/AplikasiPPW/main/Confusion-matrix%20SVM.PNG'
        st.image(image_path, caption='Confusion Matrix - SVM', width=200)

        st.write(f"Dari hasil akurasi dari 2 metode diatas yaitu metode Random Forest dan SVM didapatkan akurasi yaitu 95% untuk Random Forest dan 90% untuk SVM, Jadi hasil akurasi yang paling baik ialah menggunakan metode Random Forest")


with tab5:

        import streamlit as st
        import time
        from generate_label import get_label


        def main():

            st.set_page_config(
                page_title="Aplikasi Kategori Berita | Klasifikasi Berita Berita Satu", page_icon="📺")

            col1, col2 = st.columns(2)

            with col1:

                st.image("assets/banner.png", use_column_width=True)

            with col2:
                st.subheader("Aplikasi Prediksi Kategori Berita")
                st.caption("Nama : ADERISA DYTA OKVIANTI")
                st.caption("NIM : 200411100013")
            news_text = st.text_area(
                "Masukkan Isi Berita", key="input_text", height=250)

            if st.button("Cari Kategori"):
                if news_text:
                    text = get_label(news_text)
                    with st.expander('Tampilkan Hasil'):
                        st.write('Berita yang anda masukkan termasuk dalam kategori: ')
                        if text == "sport":
                            st.info(text)
                            url = "https://www.google.com/search?q=berita+sport+beritasatu+hari+ini"
                            st.write(
                                'Baca juga berita terbaru terkait Sport [Berita Sport hari ini](%s)'  %url)
                        elif text == "lifestyle":
                            st.info(text)
                            url = "https://www.google.com/search?q=berita+lifestyle+beritasatu+hari+ini"
                            st.write(
                                'Baca juga berita terbaru terkait Lifestyle [Berita Lifestyle hari ini](%s)'  %url)
                        elif text == "pemilu":
                            st.info(text)
                            url = "https://www.google.com/search?q=berita+pemilu+radarjatim+hari+ini"
                            st.write(
                                'Baca juga berita terbaru terkait pemilu [Berita Pemilu hari ini](%s)'  %url)
                    
                else:
                    time.sleep(.5)
                    st.toast('Input Teks')


        if __name__ == "__main__":
            main()
