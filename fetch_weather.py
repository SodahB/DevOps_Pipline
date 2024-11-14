import requests
from datetime import datetime
import streamlit as st
import os


def get_smhi_data():
    url = 'https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/18.071094/lat/59.325117/data.json'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def extract_temperature_and_time(entry):
    valid_time = entry.get("validTime")
    temperature = None
    
    for param in entry.get("parameters", []):
        if param.get("name") == "t":
            temperature = param.get("values", [None])[0]
            break
            
    return valid_time, temperature

# Streamlit display function
def print_temperature_data():
    data = get_smhi_data()
    count = 0

    st.title("Temperatur i Stockholm")
    st.write("Kommande 24 timmar")

    for entry in data.get("timeSeries", []):
        if count >= 24: 
            break

        valid_time, temperature = extract_temperature_and_time(entry)
        if temperature is not None:
            formatted_time = datetime.strptime(valid_time, "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d %H:%M")
            st.write(f"Tid: {formatted_time} Temperatur: {temperature}°C")
            count += 1

if __name__ == "__main__":
    os.system("streamlit run fetch_weather.py --server.port=80 --server.address=0.0.0.0")
    print_temperature_data()
    
