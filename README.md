# Short-Term-Project-IRIS-Kelompok-M-Deteksi-Dini-Kanker-Kulit-
Proyek Klasifikasi Lesi Kulit (HAM10000) melatih CNN (EfficientNetB0) untuk mendeteksi Melanoma dan penyakit kulit lainnya. Proses training, penanganan imbalance data, dan evaluasi dirangkum utuh dalam Jupyter Notebook. Repositori ini dilengkapi aplikasi web Flask sebagai simulasi penggunaan model.
# DermoVision AI: Klasifikasi Penyakit Kulit (HAM10000)

Proyek ini adalah implementasi *Deep Learning* untuk mendeteksi 7 jenis penyakit kulit menggunakan arsitektur **EfficientNetB0**. Proyek ini dikembangkan sebagai bagian dari *Short-Term Project* di organisasi IRIS.

## 🚀 Fitur Utama
- **Model AI Tinggi Presisi**: Menggunakan *Transfer Learning* dengan EfficientNetB0.
- **Handling Imbalance Data**: Menggunakan teknik *Class Weights* untuk menangani dominasi kelas tertentu.
- **Web App Interface**: Prototipe berbasis Flask untuk simulasi deteksi secara *real-time*.

## 📂 Struktur Repositori
- `short-term.ipynb`: Notebook utama berisi proses EDA, Training, dan Evaluasi.
- `app.py`: Backend server menggunakan Flask.
- `templates/`: UI frontend (HTML & Tailwind CSS).
- `dataset_sample.zip`: Sampel gambar (5 per kelas) untuk pengujian cepat.

## 📊 Dataset
Dataset asli menggunakan **HAM10000** yang tersedia di Kaggle.
> **Catatan**: Karena batas ukuran file di GitHub, dataset utuh (>2GB) tidak diunggah. Silakan unduh dataset resmi melalui [Link Kaggle ini](https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000). Gunakan `dataset_sample.zip` di repo ini jika ingin melakukan pengujian aplikasi secara instan.

