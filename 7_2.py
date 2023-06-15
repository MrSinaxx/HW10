import requests
import tkinter as tk

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
                humidity = data["main"]["humidity"]
                feels_like = data["main"]["feels_like"]
                return temperature, humidity, feels_like
            else:
                print(f"Error: {data['message']}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except KeyError as e:
        print("Error: Invalid API response.")
    except Exception as e:
        print(f"Error: {e}")

    return None, None, None

def fetch_weather_data():
    city = entry.get()
    temperature, humidity, feels_like = get_weather_data(city)
    if temperature is not None:
        result_label.config(text=f"Temperature: {temperature} °C\nHumidity: {humidity}%\nFeels Like: {feels_like} °C")
    else:
        result_label.config(text="Error retrieving weather data.")


window = tk.Tk()
window.title("Weather Data")
window.geometry("300x200")


entry = tk.Entry(window)
entry.pack(pady=10)

fetch_button = tk.Button(window, text="Fetch Weather Data", command=fetch_weather_data)
fetch_button.pack(pady=5)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

window.mainloop()
