import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import os

# === Load the cleaned data ===
df_weather = pd.read_csv("data/weather_data_clean.csv")
df_food = pd.read_csv("data/food_data_clean.csv")

# Ensure datetime type
df_weather["time"] = pd.to_datetime(df_weather["time"])

plt.figure(figsize=(10,5))
plt.plot(df_weather["time"], df_weather["temp_celsius"], label="Temperature (°C)")
plt.plot(df_weather["time"], df_weather["feels_like"], label="Feels Like (°C)", alpha=0.7)
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.title("Temperature and Feels-Like Temperature Over Time")
plt.legend()
plt.tight_layout() # Spacing
plt.show()

corr = df_weather[["temp_celsius", "humidity_percent", "feels_like"]].corr()
print("Correlation matrix:\n", corr)

plt.figure(figsize=(6,4))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Between Weather Variables")
plt.tight_layout()
plt.show()


plt.figure(figsize=(6,4))
df_food.T.plot(kind="bar", legend=False)
plt.title("Nutritional Composition per 100g")
plt.ylabel("Amount (grams or kcal)")
plt.tight_layout()
plt.show()