📥 Installation & Setup
1️⃣ Clone or create the project
git clone https://github.com/yourusername/zafix_health_agent.git
cd zafix_health_agent

2️⃣ Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate   # Mac/Linux

3️⃣ Install dependencies
pip install -r requirements.txt


If requirements.txt is missing, install manually:

pip install pandas matplotlib

📊 Usage
1️⃣ Run the agent
python -m src.health_agent


(or use PyCharm’s green “Run” button after fixing imports)

2️⃣ Output Example
📥 Loaded 30 user entries from data/user_metrics.json
📈 Average Sleep: 6.2h | Avg Stress: 7.8 | Activity Level: 3.4
⚠️ Anomaly Detected: High stress with low recovery.
💡 Recommendation: Take a light walk or meditate for 15 minutes before bed.

3️⃣ Key Features

Reads structured health data

Detects correlation between stress, sleep, and recovery

Suggests daily improvement actions

Can be extended with Ollama or GPT model for natural language reasoning

🧠 Modules Breakdown
Module	Description
data_reader.py	Handles JSON or CSV input, validates schema, returns pandas DataFrame
data_analyzer.py	Performs data aggregation, computes averages, and detects abnormal readings
recommender.py	Translates analysis results into human-readable suggestions
health_agent.py	Core orchestrator — integrates tools, produces summarized reports
🧩 Example Workflow

User’s device uploads daily wellness metrics.

The DataReader parses and validates them.

The DataAnalyzer identifies trends (e.g., poor sleep + high stress).

The Recommender generates adaptive advice.

The Agent compiles and prints a report or sends it to a dashboard.

💡 Stretch Goals

🧠 Integrate Ollama LLM (gemma:2b) for natural language recommendations

💾 Store daily summaries in SQLite for long-term tracking

📈 Add Streamlit dashboard for visualization

🗣️ Enable multi-modal input (voice/text)

📄 Example Report Output
🧠 ARC Daily Vitality Summary
──────────────────────────────
Sleep Duration: 5.8 hrs (Low)
Stress Level: 8.1 / 10 (High)
Activity Score: 3.5 / 10

⚠️ Pattern: Chronic stress + insufficient recovery detected
💡 Tip: Reduce caffeine intake after 4PM, schedule 10min breathing sessions