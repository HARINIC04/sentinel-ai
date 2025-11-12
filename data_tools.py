import os
import requests
from crewai.tools import tool

# --- TOOL 1: Weather Data (This one works!) ---
@tool("Weather Data Tool")
def weather_data_tool(latitude: float, longitude: float) -> str:
    """Fetches real-time weather data (temperature, rain, humidity, wind) for a specific latitude and longitude."""
    # This is the corrected line
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": ["temperature_2m", "relative_humidity_2m", "rain", "wind_speed_10m"],
        "timezone": "auto"
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status() 
        data = response.json()
        return f"Current weather at ({latitude}, {longitude}): {data['current']}"
    except requests.exceptions.RequestException as e:
        return f"Error fetching weather data: {e}"

# --- TOOL 2: Safe Routing (NEW!) ---
@tool("Safe Evacuation Route Tool")
def routing_tool(start_latitude: float, start_longitude: float, end_latitude: float, end_longitude: float) -> str:
    """Calculates a driving route between two points (latitude, longitude)."""
    
    api_key = os.getenv("ORS_API_KEY")
    if not api_key:
        return "Error: ORS_API_KEY environment variable not set."

    url = "https://api.openrouteservice.org/v2/directions/driving-car"
    
    headers = {
        'Authorization': api_key,
        'Content-Type': 'application/json'
    }
    
    body = {
        'coordinates': [
            [start_longitude, start_latitude], # ORS uses (lng, lat)
            [end_longitude, end_latitude]
        ]
    }
    
    try:
        response = requests.post(url, json=body, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        # Extract the important part: distance and duration
        route = data['routes'][0]['summary']
        distance_km = route['distance'] / 1000
        duration_min = route['duration'] / 60
        
        return f"Route calculated: Distance {distance_km:.2f} km, Duration {duration_min:.2f} minutes. Full route details: {data}"
    
    except requests.exceptions.RequestException as e:
        return f"Error calculating route: {e}"

