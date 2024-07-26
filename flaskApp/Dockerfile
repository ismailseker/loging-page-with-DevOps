# # Flask için Python tabanlı bir Docker imajı oluşturuyoruz
# FROM python:3.11-slim

# WORKDIR /app

# # Gereksinimlerinizi yükleyin
# COPY flaskApp/requirements.txt /app/
# RUN pip install --no-cache-dir -r requirements.txt

# # Flask uygulama kodunuzu kopyalayın
# COPY flaskApp /app/

# # Flask uygulamanızı başlatın
# CMD ["python", "app.py"]
# Flask için Python tabanlı bir Docker imajı oluşturuyoruz
FROM python:3.11-slim

WORKDIR /app

# Gereksinimlerinizi yükleyin
COPY flaskApp/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Flask uygulama kodunuzu kopyalayın
COPY flaskApp /app/

# Flask uygulamanızı başlatın
CMD ["python", "app.py"]
