# Import the time module to use sleep function
import time

# Import get_location function from location.py
from location import get_location

# Import get_weather function from weather.py
from weather import get_weather

# Import notify function from notifier.py
from notifier import notify

# Get user input for city name
city = input("Enter city name: ")

# Get user input for refresh interval in seconds and convert to integer
refresh = int(input("Enter refresh interval (seconds): "))

# Get latitude and longitude coordinates for the entered city
lat, lon = get_location(city)

# Exit program if coordinates are not found
if not lat:
    exit()

# Start an infinite loop to fetch weather and show notifications repeatedly
while True:
    # Fetch current weather data for the given latitude and longitude
    info = get_weather(lat, lon)

    # Show the weather information as a desktop notification
    notify(city, info)

    # Wait for the specified refresh interval before fetching weather again
    time.sleep(refresh)
