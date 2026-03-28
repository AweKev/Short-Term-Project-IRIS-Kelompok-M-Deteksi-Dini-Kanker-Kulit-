# Multi-class Skin Lesion Classification

Ini merupakan sebuah proyek *Web App* berbasis *Deep Learning* yang dirancang untuk mengklasifikasikan 7 jenis lesi kulit secara otomatis. Proyek jangka pendek (*Short-Term Project*) ini bertujuan untuk membantu mendeteksi penyakit kanker kulit dan lesi lainnya secara cepat dan akurat, menggunakan teknik **Transfer Learning** dengan arsitektur **EfficientNetB0** guna mencapai keseimbangan antara akurasi prediksi yang tinggi dan efisiensi komputasi.

**Live Demo Tersedia:** [Coba Multi-class Skin Lesion Classification di sini!](https://bit.ly/Multi-classSkinLesionClassification)

> **⏱️ Catatan Server:** Aplikasi ini di-hosting menggunakan layanan gratis dari Hugging Face Spaces. Jika tidak ada yang mengakses web ini selama kurang lebih 1-2 hari berturut-turut, server akan otomatis "tertidur" (*paused*) untuk menghemat daya. Jika saat diakses web terasa lambat atau *loading*, mohon tunggu sekitar 1-2 menit hingga sistem terbangun dan kembali menyala sepenuhnya.

---

## 📌 Dataset: HAM10000
Dataset yang digunakan untuk melatih model ini adalah **HAM10000** (*Human Against Machine with 10,000 training images*). Proyek ini mengklasifikasikan gambar lesi kulit ke dalam 7 kategori klinis:
1. **akiec**: Actinic keratoses
2. **bcc**: Basal cell carcinoma
3. **bkl**: Benign keratosis-like lesions
4. **df**: Dermatofibroma
5. **mel**: Melanoma (Kanker Ganas)
6. **nv**: Melanocytic nevi
7. **vasc**: Vascular lesions

> **Catatan Dataset:** Dikarenakan ukuran dataset asli mencapai **~6GB** (melebihi batas GitHub 100MB), repositori ini hanya menyertakan **`dataset_sample.zip`** berisi 35 gambar (5 per kelas) untuk keperluan *testing* cepat. Dataset utuh dapat diunduh langsung di [Kaggle HAM10000](https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000).

---

## ⚙️ Detail Teknis & Alur Kerja

### 1. Model Architecture
- **Base Model**: EfficientNetB0 (Pre-trained on ImageNet).
- **Custom Layers**: 
  - Global Average Pooling 2D
  - Batch Normalization
  - Dropout (0.5) untuk mencegah *overfitting*
  - Dense Layer (512 unit, aktivasi ReLU)
  - Output Dense Layer (7 unit, aktivasi Softmax).
- **Optimization**: Adam Optimizer (Learning Rate: 0.0001) dilengkapi dengan *ReduceLROnPlateau* (penyesuaian *learning rate* otomatis saat akurasi stagnan) dan *EarlyStopping*.

### 2. Handling Data Imbalance
Dataset HAM10000 sangat tidak seimbang dan didominasi oleh kelas `nv`. Untuk mengatasi ini, proyek ini menerapkan perhitungan **Class Weights** (menggunakan *library* `sklearn`) saat proses *training*. Hal ini memberikan penalti/bobot error yang lebih tinggi pada kelas minoritas yang krusial seperti **Melanoma**, sehingga AI tidak menjadi bias dan hanya menebak kelas mayoritas.

### 3. Image Pre-processing
- *Resizing* gambar dari ukuran asli menjadi **224x224** piksel (sesuai standar input EfficientNetB0).
- Normalisasi nilai pixel (*Rescaling* 1./255).
- Augmentasi data menggunakan `ImageDataGenerator` (*Rotation*, *Zoom*, *Width/Height Shift*, dan *Horizontal Flip*) untuk memperkaya variasi data latih dan meningkatkan kemampuan generalisasi model.

---

## 📂 Struktur Repositori

```text
.
├── templates/                 # Frontend UI (HTML & Tailwind CSS)
├── app.py                     # Backend Web Server (Flask)
├── Dockerfile                 # Konfigurasi Container untuk Hugging Face
├── requirements.txt           # Daftar dependensi library Python
├── short-term.ipynb           # Notebook untuk Pipeline Training & EDA
├── skin_cancer_model.h5       # Model AI Hasil Training (HDF5)
├── dataset_sample.zip         # Sampel gambar uji coba (35 images)
├── HAM10000_metadata.csv      # Metadata dari dataset HAM10000
└── README.md                  # Dokumentasi utama proyek
