from geopy.geocoders import Nominatim
import math

def get_qibla_by_city(city_name: str):
    geolocator = Nominatim(user_agent="qibla_finder_app")
    location = geolocator.geocode(city_name)
    
    if not location:
        return "Location not found."
    
    # Kaaba coordinates
    kaaba_lat = math.radians(21.422487)
    kaaba_lon = math.radians(39.826206)
    
    user_lat = math.radians(location.latitude)
    user_lon = math.radians(location.longitude)
    delta_lon = kaaba_lon - user_lon
    
    y = math.sin(delta_lon)
    x = math.cos(user_lat) * math.tan(kaaba_lat) - math.sin(user_lat) * math.cos(delta_lon)
    
    bearing = (math.degrees(math.atan2(y, x)) + 360) % 360
    return f"{location.address}\nQibla Direction: {bearing:.2f}° from True North"

print(get_qibla_by_city("Lahore, Pakistan"))
