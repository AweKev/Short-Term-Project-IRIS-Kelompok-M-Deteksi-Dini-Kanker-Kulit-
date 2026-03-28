from flask import Flask, render_template, request, jsonify
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.efficientnet import preprocess_input
from PIL import Image
import numpy as np
import io
import time

app = Flask(__name__)

# 1. Load Model saat server dinyalakan
print("Memuat model EfficientNetB0... Mohon tunggu.")
try:
    model = load_model('skin_cancer_model.h5')
    print("Model berhasil dimuat!")
except Exception as e:
    print(f"Error memuat model: {e}")

# 2. Mapping Class dari LabelEncoder Kaggle (Sesuai urutan Alfabet)
CLASS_MAPPING = {
    0: {'name': 'Actinic Keratoses (akiec)', 'risk': 'Pra-Kanker'},
    1: {'name': 'Basal Cell Carcinoma (bcc)', 'risk': 'Ganas'},
    2: {'name': 'Benign Keratosis (bkl)', 'risk': 'Jinak'},
    3: {'name': 'Dermatofibroma (df)', 'risk': 'Jinak'},
    4: {'name': 'Melanoma (mel)', 'risk': 'Ganas'},
    5: {'name': 'Melanocytic Nevi (nv)', 'risk': 'Jinak'},
    6: {'name': 'Vascular Lesions (vasc)', 'risk': 'Jinak'}
}

# 3. Routing untuk Halaman Web
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analisis')
def analisis():
    return render_template('analisis.html')

# 4. API Endpoint untuk Prediksi
@app.route('/api/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'success': False, 'error': 'Tidak ada file gambar yang diunggah'})
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'success': False, 'error': 'File kosong'})

    try:
        # Mulai hitung waktu proses
        start_time = time.time()

        # Baca dan Preprocess Gambar
        image_bytes = file.read()
        img = Image.open(io.BytesIO(image_bytes)).convert('RGB')
        img = img.resize((224, 224)) # Ukuran input EfficientNetB0
        
        img_array = img_to_array(img)
        # HAPUS BARIS img_array / 255.0
        
        img_batch = np.expand_dims(img_array, axis=0)
        
        # Gunakan preprocessor bawaan EfficientNet
        img_batch = preprocess_input(img_batch)

        # Lakukan Inferensi / Prediksi
        predictions = model.predict(img_batch)[0]
        
        # Ambil 2 prediksi tertinggi
        top_2_indices = np.argsort(predictions)[-2:][::-1]
        
        top_1_idx = top_2_indices[0]
        top_2_idx = top_2_indices[1]

        # Hitung waktu selesai
        inference_time = f"{(time.time() - start_time):.2f} detik"

        # Format output (JSON) untuk dikirim ke analisis.html
        result = {
            'success': True,
            'inference_time': inference_time,
            'top_prediction': {
                'class_name': CLASS_MAPPING[top_1_idx]['name'],
                'risk_level': CLASS_MAPPING[top_1_idx]['risk'],
                'confidence': float(predictions[top_1_idx] * 100)
            },
            'second_prediction': {
                'class_name': CLASS_MAPPING[top_2_idx]['name'],
                'risk_level': CLASS_MAPPING[top_2_idx]['risk'],
                'confidence': float(predictions[top_2_idx] * 100)
            }
        }
        return jsonify(result)

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    # Jalankan server
    app.run(host="0.0.0.0", port=7860, debug=False)
