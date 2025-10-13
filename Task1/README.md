Smart Wellness Data Automation (Task 1)
Project Overview

This project demonstrates a lightweight automation pipeline for collecting, cleaning, and visualizing wellness-related data. It simulates part of ZAFIX’s data workflow for the ARC system, which combines multiple health and wellness inputs to generate insights for personal optimization.

Key Features:

Automated fetching of data from two public APIs:

Open-Meteo API — hourly weather and environmental metrics (temperature, humidity, apparent temperature).

Open Food Facts API — nutrition information for a selected food product.

Data cleaning and normalization for consistent analysis.

Visualizations to provide basic insights from the datasets.

Fully reproducible workflow with minimal setup.

Project Structure
Task1/
│
├── data/
│   ├── weather_data.csv          # Raw weather data fetched from Open-Meteo
│   ├── food_data.csv             # Raw food data fetched from Open Food Facts
│   ├── weather_data_clean.csv    # Cleaned and normalized weather data
│   ├── food_data_clean.csv       # Cleaned and simplified food nutrition data
│
├── src/
│   ├── main.py                   # Script to fetch data from APIs
│   ├── clean_data.py             # Script to clean and normalize datasets
│   ├── visualize_data.py         # Script to generate visual insights
│
├── README.md                     # Project documentation
└── requirements.txt              # Python dependencies for the project

Tech Stack

Language: Python 3.10+

Libraries: requests, pandas, matplotlib, seaborn, os

IDE/Environment: PyCharm with .venv virtual environment

Data Storage: CSV files for raw and cleaned data

Visualization: Line charts, heatmaps, bar charts

Installation & Setup

Clone or download the project

Create a virtual environment and activate it:

python -m venv .venv
# Windows
.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate


Install dependencies:

pip install -r requirements.txt


If requirements.txt is missing, you can install manually:

pip install pandas requests matplotlib seaborn

Usage
1️⃣ Fetch Data
python src/main.py


Fetches weather and food data from the APIs.

Saves raw data to data/weather_data.csv and data/food_data.csv.

2️⃣ Clean & Normalize Data
python src/clean_data.py


Cleans missing values, normalizes column names, and formats time fields.

Saves cleaned files as weather_data_clean.csv and food_data_clean.csv.

3️⃣ Visualize Insights
python src/visualize_data.py


Generates plots for:

Hourly temperature vs. “feels-like” temperature

Correlation heatmap of weather metrics

Nutritional composition bar chart for the food item

Insights & Examples

Weather Data: Shows hourly trends for temperature and apparent temperature, helping identify patterns in environmental conditions.

Correlation: Reveals relationships between temperature, humidity, and apparent temperature.

Nutrition Data: Highlights key nutrients for the selected food, e.g., calories, sugar, protein, fat, and carbohydrates.

This demonstrates a small-scale automated wellness data pipeline capable of being extended to more datasets and integrated into intelligent health systems.