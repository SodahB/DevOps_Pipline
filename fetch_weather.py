import requests
from datetime import datetime
#Liljeholmen statisk location 
def get_smhi_data():
    url = 'https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/18.0215/lat/59.3099/data.json'
    response = requests.get(url)
    return response.json()

def print_temperature_data():
    data = get_smhi_data()
    count = 0  

    for entry in data.get('timeSeries', []):
        if count >= 10:  #max 10
            break
        
        valid_time = entry.get('validTime')
        temperature = None
        
        for param in entry.get('parameters', []):
            if param.get('name') == 't':  
                temperature = param.get('values', [])[0]

        if temperature is not None:
            #formaterrar valid_time till läsbarare 
            formatted_time = datetime.strptime(valid_time, "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d %H:%M")
            print(f"Tid: {formatted_time}, Temperatur: {temperature}°C")
            count += 1  

print_temperature_data()
