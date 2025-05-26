import random

# Geolocation data for cities within 100 km of Kelowna
locations = [
    { "name": "Kelowna", "lat": 49.888, "lon": -119.496 },
    { "name": "West Kelowna", "lat": 49.829, "lon": -119.621 },
    { "name": "Vernon", "lat": 50.034, "lon": -119.403 },
    { "name": "Peachland", "lat": 49.758, "lon": -119.738 },
    { "name": "Summerland", "lat": 49.6, "lon": -119.682 }
]

def get_random_location():
    """Return a random location from the list."""
    return random.choice(locations)
