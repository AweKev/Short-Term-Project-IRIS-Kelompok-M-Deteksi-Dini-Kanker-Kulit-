# 👁️ DermoVision AI: Multi-class Skin Lesion Classification

🚀 **Live Demo Tersedia:** [Coba DermoVision AI di sini!](https://bit.ly/Multi-classSkinLesionClassification)

---

## 📑 Daftar Isi
1. [Tentang Proyek & Latar Belakang](#1-tentang-proyek--latar-belakang)
2. [Fitur Utama](#2-fitur-utama)
3. [Panduan Penggunaan (User Guide)](#3-panduan-penggunaan-user-guide)
4. [Kelas Klasifikasi (Dataset)](#4-kelas-klasifikasi-dataset)
5. [Teknologi & Detail Model](#5-teknologi--detail-model)
6. [Alur Preprocessing Gambar](#6-alur-preprocessing-gambar)
7. [Struktur Repositori](#7-struktur-repositori)
8. [API Endpoint & Respons](#8-api-endpoint--respons)
9. [Menjalankan Secara Lokal](#9-menjalankan-secara-lokal)
10. [Panduan Deployment Docker](#10-panduan-deployment-docker)
11. [Troubleshooting Server](#11-troubleshooting-server)

---

## 1. Tentang Proyek & Latar Belakang
**DermoVision AI** adalah sebuah *Web App* berbasis *Deep Learning* yang dikembangkan sebagai *Short-Term Project* untuk mendeteksi dan mengklasifikasikan jenis penyakit kulit/lesi secara otomatis. Proyek ini dilatarbelakangi oleh urgensi deteksi dini pada kasus kanker kulit (seperti Melanoma), di mana diagnosis yang cepat dan akurat sangat krusial untuk penanganan medis lanjutan.

## 2. Fitur Utama
* **Klasifikasi Instan:** Mampu membedakan 7 jenis lesi kulit dalam hitungan detik.
* **Tingkat Risiko:** Memberikan indikator level risiko klinis (Jinak, Pra-Kanker, Ganas) pada antarmuka web.
* **Top-2 Predictions:** Menampilkan dua probabilitas prediksi tertinggi untuk memberikan konteks diagnosis yang lebih luas.
* **Serverless Deployment:** Di-hosting penuh menggunakan kontainer Docker di ekosistem Hugging Face Spaces.

## 3. Panduan Penggunaan (User Guide)
Untuk mencoba simulasi prediksi melalui *Live Demo*:
1. Buka tautan web DermoVision AI.
2. Siapkan gambar lesi kulit atau gunakan sampel dari file `dataset_sample.zip` yang ada di repositori ini.
3. Klik area **Upload** pada web dan pilih gambar yang ingin dianalisis.
4. Klik tombol **Analisis**.
5. Sistem akan memproses gambar dan langsung menampilkan dua prediksi penyakit paling memungkinkan beserta persentase keyakinan AI (*Confidence Score*).

## 4. Kelas Klasifikasi (Dataset)
Model ini dilatih menggunakan dataset standar medis **HAM10000** (*Human Against Machine with 10,000 training images*). Kategori klinis yang didukung meliputi:
1. **akiec**: Actinic keratoses (Pra-Kanker)
2. **bcc**: Basal cell carcinoma (Ganas)
3. **bkl**: Benign keratosis-like lesions (Jinak)
4. **df**: Dermatofibroma (Jinak)
5. **mel**: Melanoma (Ganas)
6. **nv**: Melanocytic nevi (Jinak)
7. **vasc**: Vascular lesions (Jinak)

## 5. Teknologi & Detail Model
### Stack Teknologi
* **Backend:** Python, Flask, Gunicorn/Werkzeug
* **AI & Machine Learning:** TensorFlow 2.x, Keras, NumPy, Pillow
* **Frontend:** HTML5, Tailwind CSS
* **Deployment:** Docker, Hugging Face Spaces

### Arsitektur Sistem (Model)
* **Base Model:** EfficientNetB0 (Pre-trained pada ImageNet).
* **Top Layers Customization:** `GlobalAveragePooling2D` -> `BatchNormalization` -> `Dropout(0.5)` -> `Dense(512, ReLU)` -> `Dense(7, Softmax)`.
* **Handling Imbalance:** Menggunakan *Class Weights* saat *training* untuk memberikan penalti tinggi jika AI salah menebak kelas minoritas yang berbahaya (seperti Melanoma).

## 6. Alur Preprocessing Gambar
Untuk memastikan akurasi saat inferensi di web, gambar yang diunggah pengguna akan melewati *pipeline* prapemrosesan yang ketat sebelum masuk ke model:
1. **Format & Konversi:** Gambar dibaca via *byte stream* (`io.BytesIO`) dan dikonversi secara paksa ke format `RGB` menggunakan `PIL`.
2. **Resizing:** Disesuaikan menjadi matriks **224x224 piksel** (syarat mutlak input EfficientNetB0).
3. **Array Expansion:** Penambahan dimensi semu (`np.expand_dims`) dari `(224, 224, 3)` menjadi format *batch* `(1, 224, 224, 3)`.
4. **Native Preprocessing:** Melewati fungsi `preprocess_input` bawaan Keras untuk EfficientNet agar distribusi nilai piksel identik dengan saat proses *training*.

## 7. Struktur Repositori
```text
.
├── templates/                 # Frontend UI (index.html, analisis.html)
├── app.py                     # Backend API & Web Server (Flask)
├── Dockerfile                 # Konfigurasi env dan port (7860)
├── requirements.txt           # Dependensi library
├── short-term.ipynb           # Notebook Pipeline Training & EDA
├── skin_cancer_model.h5       # Model Neural Network Hasil Training
├── HAM10000_metadata.csv      # Metadata asli dataset HAM10000
└── dataset_sample.zip         # Sampel gambar HAM10000 untuk testing
```

## 8. API Endpoint & Respons
Backend Flask menyediakan endpoint REST API untuk memproses inferensi gambar secara *asynchronous* (digunakan oleh halaman UI `analisis.html` untuk memuat hasil tanpa *refresh* halaman).

* **URL:** `/api/predict`
* **Method:** `POST`
* **Payload:** `multipart/form-data` (Key: `file`)

**Success Response (JSON):**
```json
{
  "success": true,
  "inference_time": "0.45 detik",
  "top_prediction": {
    "class_name": "Melanoma (mel)",
    "risk_level": "Ganas",
    "confidence": 92.45
  },
  "second_prediction": {
    "class_name": "Melanocytic Nevi (nv)",
    "risk_level": "Jinak",
    "confidence": 5.12
  }
}
```

## 9. Menjalankan Secara Lokal
Jika Anda ingin mengembangkan atau menguji aplikasi ini secara lokal di komputer Anda tanpa menggunakan Docker:
1. Lakukan *clone* pada repositori ini.
2. Buka terminal/CMD dan arahkan ke dalam direktori proyek.
3. Instal semua pustaka yang dibutuhkan dengan menjalankan perintah:
   `pip install -r requirements.txt`
4. Jalankan server Flask:
   `python app.py`
5. Buka browser dan akses alamat lokal: `http://localhost:7860` atau `http://127.0.0.1:7860`

## 10. Panduan Deployment Docker
Proyek ini dikonfigurasi secara khusus untuk dijalankan di dalam kontainer. Untuk menjalankan/mendeploy ulang di platform cloud lain:
1. Pastikan memiliki `Dockerfile` dengan instruksi mengekspos port `7860`.
2. Pastikan file `app.py` berjalan pada *host* `0.0.0.0` dan *port* `7860`.
3. Unggah seluruh direktori ke platform cloud (misal: *Hugging Face Spaces*) dan pilih SDK: **Docker**.
4. Sistem akan otomatis melakukan proses *build* kontainer.

## 11. Troubleshooting Server
Web app ini berjalan di *tier* gratis platform cloud. Jika tidak ada trafik yang mengakses web selama 48 jam berturut-turut, server akan dialihkan ke mode tidur (*Paused/Sleeping*) secara otomatis. 
* **Solusi:** Buka URL utama web app. Sistem akan membutuhkan waktu tunggu ekstra (sekitar 1-2 menit) saat *loading* awal untuk "membangunkan" kontainer kembali hingga statusnya *Running*.
