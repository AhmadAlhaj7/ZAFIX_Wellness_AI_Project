import requests
import pandas as pd
import os

os.makedirs("data", exist_ok=True)

# === 1. Fetch data from Open-Meteo ===
weather_url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 40.7,      # New York City
    "longitude": -74.0,
    "hourly": "temperature_2m,relative_humidity_2m,apparent_temperature",
    "timezone": "America/New_York"
}

response = requests.get(weather_url, params=params)

if response.status_code == 200:
    data = response.json()
    print("✅ Open-Meteo data fetched successfully!")
else:
    print("❌ Failed to fetch weather data:", response.status_code)

# === 2. Fetch data from Open Food Facts ===
food_url = "https://world.openfoodfacts.org/api/v0/product/737628064502.json"  # Example: Nutella

food_response = requests.get(food_url)

if food_response.status_code == 200:
    food_data = food_response.json()
    print("✅ Open Food Facts data fetched successfully!")
    # Extract nutrition info
    nutriments = food_data['product']['nutriments']
    print("Calories (kcal):", nutriments.get('energy-kcal_100g'))
    print("Protein (g):", nutriments.get('proteins_100g'))
    print("Sugar (g):", nutriments.get('sugars_100g'))
else:
    print("❌ Failed to fetch food data:", food_response.status_code)

# Convert weather data to DataFrame
df_weather = pd.DataFrame({
    "time": data["hourly"]["time"],
    "temperature": data["hourly"]["temperature_2m"],
    "humidity": data["hourly"]["relative_humidity_2m"],
    "apparent_temp": data["hourly"]["apparent_temperature"]
})
df_weather.to_csv("data/weather_data.csv", index=False)
print("✅ Weather data saved to data/weather_data.csv")

# Convert food data to DataFrame
df_food = pd.DataFrame([nutriments])
df_food.to_csv("data/food_data.csv", index=False)
print("✅ Food data saved to data/food_data.csv")
