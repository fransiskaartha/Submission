# Clustering Penyewaan Sepeda Berdasarkan Jam

## Deskripsi Proyek
Proyek ini bertujuan untuk melakukan clustering pada data penyewaan sepeda berdasarkan jam menggunakan algoritma K-Means. Dengan analisis ini, kita dapat mengelompokkan pola penyewaan sepeda berdasarkan waktu untuk mendapatkan wawasan yang lebih baik terkait tren penyewaan.

## Struktur Direktori
```
submission/
├───dashboard/
│   ├───dashboard.py   # Script utama untuk menampilkan dashboard
│   ├───main_data.csv  # Dataset utama yang digunakan dalam dashboard
├───data/
│   ├───day.csv     # Dataset tambahan 1
│   ├───hour.csv     # Dataset tambahan 2
├───notebook.ipynb     # Notebook untuk eksplorasi dan analisis data
├───README.md          # Dokumentasi proyek
├───requirements.txt   # File dependensi yang diperlukan
├───url.txt            # File berisi sumber dataset atau referensi tambahan
```

## Persyaratan Instalasi
Sebelum menjalankan proyek ini, pastikan telah menginstal semua dependensi dengan perintah berikut:

```bash
pip install -r requirements.txt
pip install numpy
pip install pandas
pip install scipy
pip install streamlit 
pip install matplotlib.pyplot 
pip install seaborn
```

## Cara Menjalankan Dashboard
Jalankan perintah berikut di terminal:

```bash
streamlit run dashboard/dashboard.py
```

Jika terjadi error `streamlit: command not found`, coba jalankan:

```bash
python -m streamlit run dashboard/dashboard.py
```

## Troubleshooting
1. **ImportError: ModuleNotFoundError**
   - Pastikan semua dependensi telah terinstal dengan perintah:
   
   ```bash
   pip install -r requirements.txt
   ```

2. **NameError: name 'KMeans' is not defined**
   - Pastikan menambahkan impor berikut ke dalam kode:
   
   ```python
   from sklearn.cluster import KMeans
   ```

## Penjelasan Notebook
File `notebook.ipynb` berisi eksplorasi data dan analisis clustering menggunakan K-Means. Notebook ini digunakan untuk:
- Memeriksa distribusi data
- Melakukan preprocessing data
- Menentukan jumlah cluster optimal menggunakan metode elbow
- Menganalisis hasil clustering

## Informasi `url.txt`
File `url.txt` berisi link localhost dari dashboard pemyewaan sepeda