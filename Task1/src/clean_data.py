import requests
import pandas as pd
import os



# === Step 2: Load the saved data ===
df_weather = pd.read_csv("data/weather_data.csv")
df_food = pd.read_csv("data/food_data.csv")

print("Weather data shape:", df_weather.shape)
print("Food data shape:", df_food.shape)


# Check for missing data
print(df_weather.isnull().sum())

# Fill or drop missing values
df_weather = df_weather.fillna(method="ffill")   # forward fill
# or you can use df_weather.dropna() if preferred

df_food = df_food.fillna(0)

# === Save Cleaned Weather Data ===

df_weather.rename(columns={
    "temperature": "temp_celsius",
    "humidity": "humidity_percent",
    "apparent_temp": "feels_like"
}, inplace=True)

df_weather.to_csv("data/weather_data_clean.csv", index=False)

print("✅ Cleaned weather data saved to data/weather_data_clean.csv")

# === Clean and Save Food Data ===
# Keep only key nutrition fields
nutrition_cols = [
    'energy-kcal_100g',
    'proteins_100g',
    'carbohydrates_100g',
    'sugars_100g',
    'fat_100g'
]

# Filter columns that exist in the DataFrame
nutrition_cols = [col for col in nutrition_cols if col in df_food.columns] # Only keep columns from our list that actually exist in the DataFrame.
df_food_clean = df_food[nutrition_cols].copy()

# Rename columns for clarity
df_food_clean.rename(columns={
    'energy-kcal_100g': 'calories',
    'proteins_100g': 'protein_g',
    'carbohydrates_100g': 'carbs_g',
    'sugars_100g': 'sugar_g',
    'fat_100g': 'fat_g'
}, inplace=True)

# Fill missing values with zero
df_food_clean = df_food_clean.fillna(0)

# Save cleaned food data
df_food_clean.to_csv("data/food_data_clean.csv", index=False)
print("✅ Cleaned food data saved to data/food_data_clean.csv")

