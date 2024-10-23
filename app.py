from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv
from datetime import datetime

app = Flask(__name__)

load_dotenv()
API_KEY = os.getenv("API_KEY")


def format_time(timestamp, timezone_offset):
    """Convert UTC timestamp to local time using the timezone offset"""
    return datetime.utcfromtimestamp(timestamp + timezone_offset).strftime(
        "%Y-%m-%d %H:%M:%S"
    )


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/weather", methods=["POST"])
def get_weather():
    city = request.form["city"]
    if not city:
        return render_template("index.html", error="Please enter a city name.")

    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(weather_url)

    if response.status_code == 200:
        weather_data = response.json()

        weather = {
            "city": weather_data["name"],
            "country": weather_data["sys"]["country"],
            "coordinates": f"{weather_data['coord']['lat']}, {weather_data['coord']['lon']}",
            "temperature": weather_data["main"]["temp"],
            "feels_like": weather_data["main"]["feels_like"],
            "min_temp": weather_data["main"]["temp_min"],
            "max_temp": weather_data["main"]["temp_max"],
            "pressure": weather_data["main"]["pressure"],
            "humidity": weather_data["main"]["humidity"],
            "visibility": weather_data["visibility"],
            "wind_speed": weather_data["wind"]["speed"],
            "wind_deg": weather_data["wind"]["deg"],
            "weather_description": weather_data["weather"][0]["description"],
            "weather_icon": f"http://openweathermap.org/img/wn/{weather_data['weather'][0]['icon']}@2x.png",
            "clouds": weather_data["clouds"]["all"],
            "sunrise": format_time(
                weather_data["sys"]["sunrise"], weather_data["timezone"]
            ),
            "sunset": format_time(
                weather_data["sys"]["sunset"], weather_data["timezone"]
            ),
            "sunrise_time": weather_data["sys"]["sunrise"],
            "sunset_time": weather_data["sys"]["sunset"],
        }
        return render_template("weather.html", weather=weather)
    else:
        return render_template("index.html", error="City not found.")


if __name__ == "__main__":
    app.run(debug=True)
