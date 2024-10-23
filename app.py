from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

# Initialize app
app = Flask(__name__)

# Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")


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
            "temperature": weather_data["main"]["temp"],
            "description": weather_data["weather"][0]["description"],
            "humidity": weather_data["main"]["humidity"],
            "wind_speed": weather_data["wind"]["speed"],
        }
        return render_template("weather.html", weather=weather)
    else:
        return render_template("index.html", error="City not found.")


if __name__ == "__main__":
    app.run(debug=True)
