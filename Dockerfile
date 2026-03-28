# Gunakan image Python yang ringan
FROM python:3.9-slim

# Set folder kerja di dalam server
WORKDIR /app

# Copy semua file dari laptopmu ke dalam server
COPY . .

# Install semua library yang ada di requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Beri tahu port mana yang dipakai Flask (default: 5000)
EXPOSE 7860

# Jalankan aplikasi Flask
# Hugging Face butuh aplikasi jalan di port 7860 dan host 0.0.0.0
CMD ["python", "app.py"]