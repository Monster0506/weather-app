# Weather App

A simple web application built using Python and Flask that provides real-time weather updates by city name. The app fetches data from the OpenWeather API to display current weather conditions in an easy-to-use interface.

## Features

- **Search by city name**: Users can input a city name to retrieve the current weather.
- **Weather details**: Displays key data, including temperature, weather condition, humidity, and wind speed.
- **Minimal UI**: Clean, straightforward interface for a smooth user experience.
- **Error handling**: Graceful handling of invalid city names or API errors.

### Available Weather Data

The application provides comprehensive weather information including:
- **Location**: City name, country code, and geographical coordinates
- **Temperature**: Current, feels like, minimum, and maximum temperatures (in Celsius)
- **Atmospheric Conditions**: Pressure, humidity percentage, visibility, and cloud coverage
- **Wind**: Speed and direction
- **Weather Description**: Text description and weather icon
- **Sun Timings**: Sunrise and sunset times for the location

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS (Optionally use a CSS framework like Bootstrap for improved styling)
- **API**: OpenWeather API for fetching weather data
- **Hosting**: (Optional) Deploy on platforms like Heroku, PythonAnywhere, or Vercel for public access

## Getting Started

### Prerequisites

Ensure the following are installed on your system:

- Python 3.x
- `pip` (Python package manager)
- Flask (install via pip)
- An OpenWeather API key (get it [here](https://openweathermap.org/api))

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/monster0506/weather-app.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd weather-app
   ```

3. **Create and activate a virtual environment (recommended)**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install the required dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

5. **Add your OpenWeather API key**:

   - Create a `.env` file in the project directory and add your API key:

     ```bash
     API_KEY=your_openweather_api_key
     ```

### Running the App

1. **Start the Flask development server**:

   ```bash
   flask run
   ```

   Or if you have a `run.py` file:

   ```bash
   python run.py
   ```

2. **Access the app in your browser** at:

   ```
   http://localhost:5000
   ```

## Usage

1. Enter a city name in the input field.
2. Click the "Get Weather" button.
3. View the displayed weather data (temperature, conditions, etc.).

## Example Screenshots

- **Homepage**:
  ![Home Page](/assets/HomePage.png)

- **Weather Results**:
  ![City Page](/assets/CityPage.png)

## To Do

- Add support for multiple cities and/or countries.
- Display a 5-day weather forecast.
- Enhance the UI with better styling or animations.

## Contributing

Contributions, issues, and feature requests are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.
