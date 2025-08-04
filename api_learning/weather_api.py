import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def get_weather_simple(city):
    # Get API key from .env file
    api_key = os.getenv('OPENWEATHERMAP_API_KEY')
    print(f"API Key loaded: {'Valid key found' if api_key and len(api_key) > 10 else 'Key missing or invalid'}")

    # API Endpoint
    base_url = 'https://api.openweathermap.org/data/2.5/weather'

    # Parameters for the request
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Get temperature in Celsius
    }

    try:
        # Send GET request to the API
        response = requests.get(base_url, params=params)

        # Print raw response for debugging
        print("Response Status Code:", response.status_code)

        # Check if the request was successful
        response.raise_for_status()

        # Parse the JSON response
        weather_data = response.json()

        # Extract relevant information
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']

        # Print the results
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {description}")

    except requests.RequestException as e:
        print(f"Error: {e}")

    # Example usage
    # get_weather_simple('London')


if __name__ == "__main__":
    get_weather_simple('London')  # Or any city you want to check
