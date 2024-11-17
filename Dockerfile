# Use a base image with Python 3.10
FROM python:3.10-slim

# Set environment variables to ensure python outputs everything to the console and to prevent writing .pyc files
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set a working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Expose port 8501 for Streamlit (if you're using Streamlit to serve the app)
EXPOSE 8501

# Run the application
CMD ["streamlit", "run", "fetch_weather.py"]