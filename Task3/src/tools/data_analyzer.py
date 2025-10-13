import os
import pandas as pd
from src.tools.data_reader import DataReader


class DataAnalyzer:
    def __init__(self):
        # Use the updated DataReader path
        self.reader = DataReader(data_file="src/data/user_metrics.csv")

    def analyze_data(self):
        df = self.reader.load_data()
        summary = ""

        # Define the metrics to summarize and their display formats
        metrics = {
            "sleep_hours": "{:.1f}",
            "steps": "{:.0f}",
            "calories_burned": "{:.0f}",
            "heart_rate": "{:.1f}",
            "stress_level": "{:.1f}",
            "focus_score": "{:.1f}"
        }

        # Build summary dynamically
        for column, fmt in metrics.items():
            if column in df.columns:
                summary += f"Average {column.replace('_', ' ')}: {fmt.format(df[column].mean())}\n"
            else:
                summary += f"Average {column.replace('_', ' ')}: N/A\n"

        # Detect anomalies safely
        anomaly_conditions = []
        if "sleep_hours" in df.columns:
            anomaly_conditions.append(df["sleep_hours"] < 5)
        if "stress_level" in df.columns:
            anomaly_conditions.append(df["stress_level"] > 8)
        if "heart_rate" in df.columns:
            anomaly_conditions.append(df["heart_rate"] > 100)

        if anomaly_conditions:
            anomalies = df[pd.concat(anomaly_conditions, axis=1).any(axis=1)]
        else:
            anomalies = pd.DataFrame()  # empty DataFrame if no conditions exist

        if not anomalies.empty:
            print("⚠️ Detected anomalies:")
            print(anomalies)
        else:
            print("✅ No anomalies detected.")

        return summary.strip(), anomalies
