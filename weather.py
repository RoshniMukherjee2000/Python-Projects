# Import the requests library to make HTTP requests to APIs
import requests

# Define a function to get current weather data given latitude and longitude
def get_weather(lat, lon):
    """Fetch current weather data using Open-Meteo Weather API"""

    # Create the API URL with the given latitude and longitude
    # current_weather=true ensures only current weather is returned
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

    # Send a GET request to the API URL and convert the response to a Python dictionary
    data = requests.get(url).json()

    # Extract the 'current_weather' dictionary from the API response
    w = data.get("current_weather")
    
    # If 'current_weather' is not present in the response, return an error message
    if not w:
        return "Weather data not available"

    # Extract temperature from the 'current_weather' dictionary
    temp = w["temperature"]
    
    # Extract wind speed from the 'current_weather' dictionary
    wind = w["windspeed"]
    
    # Return a formatted string showing temperature and wind speed
    return f"Temperature: {temp}°C\nWind: {wind} km/h"
