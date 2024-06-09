# Weather Application

The Django Weather Application is a web-based weather forecasting tool that provides users with current weather conditions and forecasts for locations around the world. It leverages Django and integrates with a weather API to fetch real-time weather data.

## Features

- Current weather: Display current weather conditions including temperature, humidity, wind speed, and weather description.
- Forecast: Provide a weather forecast for the next few days, including temperature trends and expected conditions.
- Location search: Allow users to search for weather information by entering the name of a city or location.

## Installation

1. Clone the repository:

```
git clone https://github.com/tanujgupta18/weather-application.git
```

2. Set up API keys:

   - Obtain an API key from a weather data provider (e.g., OpenWeatherMap, Weatherstack).
   - Create a `.env` file in the project root directory.
   - Add your API key to the `.env` file:

3. Run the development server:

```
python manage.py runserver
```

The application will be accessible at `http://localhost:8000`.

## Usage

- Visit `http://localhost:8000` to access the weather application.
- Enter the name of a city or location in the search bar to retrieve weather information.
- View current weather conditions and forecasts for the selected location.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.
