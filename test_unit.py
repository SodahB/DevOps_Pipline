from fetch_weather import get_smhi_data, extract_temperature_and_time

def test_extract_temperature_with_real_data():
    data = get_smhi_data()  
    first_entry = data.get("timeSeries", [])[0] 

    assert first_entry is not None, "No data retrieved from the API"

    valid_time, temperature = extract_temperature_and_time(first_entry)
    
    assert valid_time is not None, "Expected 'validTime' to be extracted"
    assert isinstance(temperature, (int, float)), "Expected temperature to be an integer or float"
