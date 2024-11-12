from fetch_weather import get_smhi_data

def test_integration_with_real_api():
    data = get_smhi_data() 

    assert "timeSeries" in data, "Expected 'timeSeries' key in API response"
    assert len(data["timeSeries"]) > 0, "Expected 'timeSeries' to contain entries"

    first_entry = data["timeSeries"][0]
    assert "validTime" in first_entry, "Expected 'validTime' in entry"
    assert "parameters" in first_entry, "Expected 'parameters' in entry"

    temperature_params = [param for param in first_entry["parameters"] if param["name"] == "t"]
    assert temperature_params, "Temperature data ('t') not found in parameters"
    assert "values" in temperature_params[0], "Expected 'values' key in temperature parameter"
