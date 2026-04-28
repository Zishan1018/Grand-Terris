# hospitals.py

import math

# 📍 Mock hospitals (Hyderabad area)
HOSPITALS = [
    {"name": "Apollo Hospital", "lat": 17.3850, "lon": 78.4867},
    {"name": "Yashoda Hospital", "lat": 17.4435, "lon": 78.3772},
    {"name": "Care Hospital", "lat": 17.4010, "lon": 78.4770},
    {"name": "KIMS Hospital", "lat": 17.4350, "lon": 78.4480},
]


# 📏 distance formula
def calculate_distance(lat1, lon1, lat2, lon2):
    return math.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)


# 🏥 find nearest hospital
def find_nearest_hospital(user_lat, user_lon):
    nearest = None
    min_distance = float('inf')

    for hospital in HOSPITALS:
        dist = calculate_distance(user_lat, user_lon, hospital["lat"], hospital["lon"])
        if dist < min_distance:
            min_distance = dist
            nearest = hospital

    return nearest