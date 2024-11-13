# Använd en officiell Python-bild som bas
FROM python:3.10-slim

# Ange en miljövariabel för att förhindra att pyc-filer skapas
ENV PYTHONUNBUFFERED=1

# Ange en specifik arbetskatalog
WORKDIR /app

# Kopiera endast requirements.txt först, vilket hjälper till att cachelagra installationen av beroenden
COPY requirements.txt .

# Installera beroenden
RUN pip install --no-cache-dir -r requirements.txt

# Kopiera resten av applikationen
COPY . .

# Exponera port 80 för applikationen
EXPOSE 80

# Kör kommandot för att starta applikationen
CMD ["python", "fetch_weather.py"]
