import requests


class WeatherAPI:
    def __init__(self, api_key):
        self.base_url = 'https://api.openweathermap.org/data/2.5/weather'
        self.api_key = api_key

    def get_weather(self, city):
        """Fetch and display weather for a given city."""
        try:
            response = requests.get(self.base_url, params={
                'q': city,
                'appid': self.api_key,
                'units': 'metric'
            })

            response.raise_for_status()  # Raise an exception for bad responses

            weather_data = response.json()
            return {
                'city': city,
                'temperature': weather_data['main']['temp'],
                'description': weather_data['weather'][0]['description']
            }

        except requests.RequestException as e:
            print(f"API request failed: {e}")
            return None


# Usage
weather_service = WeatherAPI('your_api_key_here')
weather_info = weather_service.get_weather('London')
if weather_info:
    print(f"Weather in {weather_info['city']}:")
    print(f"Temperature: {weather_info['temperature']}°C")
    print(f"Description: {weather_info['description']}")
