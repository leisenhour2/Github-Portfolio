"""
📍 Weather Report CLI Application
---------------------------------
Get current weather and a 3-day forecast for any location using OpenWeatherMap and Geopy.

Author: Larry Isenhour II
GitHub: https://github.com/leisenhour2
License: MIT
"""

import requests
import os
import time
from geopy.geocoders import Nominatim


# ================================
# 🔐 Load OpenWeatherMap API Key
# ================================
def load_api_key():
    """Reads the OpenWeatherMap API key from the local 'appid' file."""
    try:
        with open(f"{os.path.dirname(__file__)}/appid", "r") as file:
            return file.readline().strip()
    except Exception as e:
        print(f"[ERROR] Could not read API key: {e}")
        exit(1)


API_KEY = load_api_key()


# ==========================
# 🌦️ Weather Report Class
# ==========================
class WeatherReport:
    def __init__(self, name, lat, lon):
        self.city = name.title()
        self.lat = lat
        self.lon = lon
        self.current_url = (
            f"https://api.openweathermap.org/data/2.5/weather?units=metric"
            f"&lat={self.lat}&lon={self.lon}&appid={API_KEY}"
        )
        self.forecast_url = (
            f"https://api.openweathermap.org/data/2.5/onecall?units=metric"
            f"&lat={self.lat}&lon={self.lon}&exclude=minutely,hourly,alerts&appid={API_KEY}"
        )

    @staticmethod
    def c_to_f(celsius):
        """Convert Celsius to a formatted Celsius/Fahrenheit string."""
        try:
            c = float(celsius)
            f = (c * 9 / 5) + 32
            return f"{c:.1f}°C / {f:.1f}°F"
        except Exception:
            return "Invalid"

    @staticmethod
    def get_icon(condition):
        """Return an emoji icon for a given weather condition."""
        icons = {
            "Clear": "☀️", "Clouds": "☁️", "Rain": "🌧️", "Drizzle": "🌦️",
            "Thunderstorm": "⛈️", "Snow": "❄️", "Mist": "🌫️", "Smoke": "🚬",
            "Haze": "🌫️", "Dust": "🌪️", "Fog": "🌁", "Sand": "🏜️",
            "Ash": "🌋", "Squall": "💨", "Tornado": "🌪️"
        }
        return icons.get(condition, "")

    def get_current_weather(self):
        """Fetch and return the current weather data as a dictionary."""
        try:
            response = requests.get(self.current_url)
            time.sleep(1)
            data = response.json()

            condition = data["weather"][0]["main"]
            return {
                "City": self.city,
                "Latitude": self.lat,
                "Longitude": self.lon,
                "Temperature": self.c_to_f(data["main"]["temp"]),
                "Max Temp": self.c_to_f(data["main"]["temp_max"]),
                "Min Temp": self.c_to_f(data["main"]["temp_min"]),
                "Sky": f"{condition} {self.get_icon(condition)}",
                "Description": data["weather"][0]["description"].capitalize(),
                "Humidity": f"{data['main']['humidity']}%",
                "Visibility": f"{data['visibility'] / 1000:.1f} km",
                "Wind Speed": f"{data['wind']['speed']} m/s"
            }

        except Exception as e:
            return {"Error": f"Could not fetch weather: {e}"}

    def get_forecast(self, days=3):
        """Fetch and return daily forecast for the next 'days'."""
        try:
            response = requests.get(self.forecast_url)
            time.sleep(1)
            data = response.json()
            return data.get("daily", [])[:days]
        except Exception as e:
            print(f"[Forecast Error] {e}")
            return []

    def display_weather(self):
        """Print the current weather and a 3-day forecast."""
        print("\n" + "=" * 60)
        print("🌍 Current Weather:")
        weather = self.get_current_weather()
        for key, value in weather.items():
            print(f"{key:<18}: {value}")
        print("=" * 60)

        print("📅 3-Day Forecast:")
        for day in self.get_forecast():
            date = time.strftime('%Y-%m-%d', time.gmtime(day["dt"]))
            condition = day["weather"][0]["main"]
            icon = self.get_icon(condition)
            day_temp = self.c_to_f(day["temp"]["day"])
            night_temp = self.c_to_f(day["temp"]["night"])
            print(f"{date} → {condition:<10} {icon} | Day: {day_temp}, Night: {night_temp}")
        print("=" * 60)


# ================================
# 📌 Main Program Entry Point
# ================================
def main():
    geolocator = Nominatim(user_agent="weather_cli_app")

    while True:
        address = input("\n📍 Enter a location (or type 'exit' to quit): ").strip()
        if address.lower() == "exit":
            print("👋 Goodbye!")
            break

        try:
            location = geolocator.geocode(address)
            if location:
                print(f"\n🔎 Found: {location.address}")
                report = WeatherReport(address, location.latitude, location.longitude)
                report.display_weather()
            else:
                print(f"❌ Location not found: {address}")
        except Exception as e:
            print(f"[Error] {e}")

        time.sleep(2)


if __name__ == "__main__":
    main()
