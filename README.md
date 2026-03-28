Multi-class Skin Lesion Classification

Merupakan proyek riset *Deep Learning* yang dirancang untuk mengklasifikasikan 7 jenis lesi kulit secara otomatis. Proyek ini menggunakan teknik **Transfer Learning** dengan arsitektur **EfficientNetB0** untuk mencapai keseimbangan antara akurasi tinggi dan efisiensi komputasi pada perangkat lokal.

---

## 📌 Dataset: HAM10000
Dataset yang digunakan adalah **HAM10000** ("Human Against Machine with 10,000 training images"). Proyek ini mengklasifikasikan gambar ke dalam 7 kategori klinis:
1. **akiec**: Actinic keratoses
2. **bcc**: Basal cell carcinoma
3. **bkl**: Benign keratosis-like lesions
4. **df**: Dermatofibroma
5. **mel**: Melanoma (Kanker Ganas)
6. **nv**: Melanocytic nevi
7. **vasc**: Vascular lesions

> **⚠️ Catatan Dataset:** Dikarenakan ukuran dataset asli mencapai **~6GB** (melebihi batas GitHub 100MB), repositori ini hanya menyertakan **`dataset_sample.zip`** berisi 35 gambar (5 per kelas) untuk keperluan *testing* cepat. Dataset utuh dapat diunduh di [Kaggle HAM10000](https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000).

---

## ⚙️ Detail Teknis & Alur Kerja
### 1. Model Architecture
- **Base Model**: EfficientNetB0 (Pre-trained on ImageNet).
- **Custom Layers**: Global Average Pooling, Dropout (0.3), dan Dense Layer dengan aktivasi Softmax.
- **Optimization**: Adam Optimizer dengan *Learning Rate Reduction* otomatis saat akurasi stagnan.

### 2. Handling Data Imbalance
Dataset ini sangat tidak seimbang (didominasi oleh kelas `nv`). Proyek ini menerapkan **Class Weights** saat proses *training* untuk memberikan bobot lebih tinggi pada kelas minoritas yang krusial seperti **Melanoma**, sehingga model tidak hanya pintar menebak kelas mayoritas.

### 3. Image Pre-processing
- Resizing gambar menjadi **224x224** piksel.
- Normalisasi nilai pixel (Scaling).
- Augmentasi data (Rotation, Zoom, Flip) untuk meningkatkan generalisasi model.

---

## 📂 Struktur Repositori
```text
.
├── templates/               # Frontend (HTML & Tailwind CSS)
├── app.py                   # Backend Flask Server
├── short-term.ipynb         # Pipeline Training & EDA
├── skin_cancer_model.h5     # Model Hasil Training
├── dataset_sample.zip       # Sampel gambar untuk testing
├── HAM10000_metadata.csv    # Metadata dataset
└── README.md                # Dokumentasi proyek
