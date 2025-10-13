import os
import pandas as pd


class DataReader:
    def __init__(self, data_file="src/data/user_metrics.csv"):
        # Base directory = project root (where Task3 folder is)
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        self.data_path = os.path.join(base_dir, data_file)

    def load_data(self):
        if not os.path.exists(self.data_path):
            raise FileNotFoundError(f"Data file not found at {self.data_path}")

        df = pd.read_csv(self.data_path)
        print(f"✅ Data loaded successfully from: {self.data_path}")
        return df
