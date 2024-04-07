import requests
from datetime import datetime, timedelta

# Coordinaten van de kantoorlocatie in Nederland
latitude = 50.930581
longitude = 5.780691

# API endpoint
url = f"https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}&formatted=0"

# GET-request naar de API
response = requests.get(url)

# Parse the JSON response
data = response.json()

# haalt zonsopkomst en zonsondergangstijden op
sunrise_str = data["results"]["sunrise"]
sunset_str = data["results"]["sunset"]

# converteer zonsopkomst en zonsondergangstijden naar datetime
sunrise = datetime.fromisoformat(sunrise_str[:-6])  # verwijder tijdzones
sunset = datetime.fromisoformat(sunset_str[:-6])    # verwijder tijdzones

# huidige tijd 
now = datetime.now()

#bepaalt wanneer het dag of nacht is
if sunrise < now < sunset:
    print("ON")
else:
    print("OFF")

