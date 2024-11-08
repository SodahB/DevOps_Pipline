import requests
from datetime import datetime
import streamlit as st
#Stockholm statisk location 
def get_smhi_data():
    url = 'https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/18.071094/lat/59.325117/data.json'
    response = requests.get(url)
    return response.json()

def print_temperature_data():
    data = get_smhi_data()
    count = 0  

    st.title ("Temperatur i Stockholm")
    st.write ("Kommmande 24 timmarna")

    for entry in data.get('timeSeries', []):
        if count >= 24:  #max 24
            break
        
        valid_time = entry.get('validTime')
        temperature = None
        
        for param in entry.get('parameters', []):
            if param.get('name') == 't':  
                temperature = param.get('values', [])[0]

        if temperature is not None:
            #formaterrar valid_time till läsbarare 
            formatted_time = datetime.strptime(valid_time, "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d %H:%M")
            st.write(f"Tid: {formatted_time} Temperatur: {temperature}°C")
            count += 1  

if __name__ == "__main__":
    print_temperature_data()
