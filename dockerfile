FROM python:3.9

COPY requirements.txt /app/

COPY . /app/

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "fetch_weather.py"]
