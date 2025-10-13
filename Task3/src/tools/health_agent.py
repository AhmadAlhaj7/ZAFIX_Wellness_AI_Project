import os
import json
import sys
from datetime import datetime



import ollama  # Using your local Ollama model
from src.tools.data_reader import DataReader
from src.tools.data_analyzer import DataAnalyzer


current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
if project_root not in sys.path:
    sys.path.append(project_root)
class HealthCompanionAgent:
    def __init__(self, memory_file="data/memory.json", model="gemma:2b"):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        self.memory_path = os.path.join(base_dir, memory_file)
        self.model = model

        # Initialize tools
        self.reader = DataReader()
        self.analyzer = DataAnalyzer()

        # Load or initialize memory
        if os.path.exists(self.memory_path):
            with open(self.memory_path, "r") as f:
                self.memory = json.load(f)
        else:
            self.memory = {"history": []}

    def generate_recommendation(self, summary):
        """Use Ollama model to generate recommendations"""
        prompt = (
            "You are a personalized health AI assistant. Based on the following user data summary, "
            "provide actionable insights to improve well-being. "
            "Focus on nutrition, recovery, and mental balance.\n\n"
            f"{summary}\n\n"
            "Format your answer clearly in bullet points."
        )

        try:
            response = ollama.chat(model=self.model, messages=[
                {"role": "user", "content": prompt}
            ])
            return response["message"]["content"]
        except Exception as e:
            return f"⚠️ Model error: {str(e)}"

    def update_memory(self, recommendations):
        """Append today's recommendations to memory"""
        self.memory["history"].append({
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "recommendations": recommendations
        })

        # Save updated memory
        with open(self.memory_path, "w") as f:
            json.dump(self.memory, f, indent=4)

    def run_daily_report(self):
        """Generate daily summary, detect anomalies, and make recommendations"""
        df = self.reader.load_data()
        summary, anomalies = self.analyzer.analyze_data()

        recommendations = self.generate_recommendation(summary)
        self.update_memory(recommendations)

        print("\n📅 DAILY HEALTH REPORT")
        print("-" * 40)
        print(recommendations)
        print("\n🧠 Memory updated successfully.")


if __name__ == "__main__":
    agent = HealthCompanionAgent()
    agent.run_daily_report()
