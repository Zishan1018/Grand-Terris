 # location.py
import random

def get_location():
    """
    Simulated GPS coordinates (Hyderabad area)
    """
    lat = 17.3850 + random.uniform(-0.01, 0.01)
    lon = 78.4867 + random.uniform(-0.01, 0.01)

    return lat, lon