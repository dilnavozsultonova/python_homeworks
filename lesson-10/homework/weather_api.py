
import requests

API_KEY = "b25328466b974da2515a56eb525deadb"
lat = 41.2995
lon = 69.2401
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"]
    print(f"Current temperature at lat:{lat}, lon:{lon}: {temp}°C, {weather}")
else:
    print("Error:", data.get("message", "Unknown error occurred"))