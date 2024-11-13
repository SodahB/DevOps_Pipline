FROM python:3.10-slim

COPY requirements.txt /app/

COPY . /app/

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "fetch_weather.py"]
