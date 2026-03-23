# Import the requests module to make HTTP requests
import requests

# Define a function to get latitude and longitude for a city
def get_location(city):
    """Fetch latitude and longitude for a given city using Open-Meteo Geocoding API"""
    
    # Create the API URL for geocoding the city name
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    
    # Make a GET request to the API and parse the response as JSON
    data = requests.get(url).json()

    # Check if the response contains results
    if "results" not in data:
        # Print message if city not found
        print("City not found!")
        # Return None for both latitude and longitude
        return None, None

    # Extract latitude from the API response
    lat = data["results"][0]["latitude"]
    
    # Extract longitude from the API response
    lon = data["results"][0]["longitude"]
    
    # Return latitude and longitude
    return lat, lon
