import requests

def get_weather_data(city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    api_key = "60be8f85c6c83c4402a1439456f9647c"  

    try:
        params = {
            "q": city,
            "appid": api_key,
            "units": "metric"  
        }
        with requests.get(url, params=params) as response:
            data = response.json()
            if response.status_code == 200:
                temperature = data["main"]["temp"]
                return temperature
            else:
                print(f"Error: {data['message']}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except KeyError as e:
        print("Error: Invalid API response.")
    except Exception as e:
        print(f"Error: {e}")

    return None


temperature = get_weather_data("Kish")
print(temperature)
