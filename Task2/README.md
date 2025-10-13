The ZAFIX AI Wellness Tutor is a small-scale, knowledge-driven chatbot that explains wellness, nutrition, and longevity concepts in simple, factual terms.
It uses local AI models (Ollama) and a retrieval-based question-answering pipeline to generate contextual, source-grounded responses from curated wellness articles.

This project demonstrates an offline-capable AI Tutor — capable of reasoning over a custom knowledge base using open-source tools.

🎯 Objectives

Build a contextual AI Tutor that can explain wellness or nutrition concepts.

Use a retrieval-based QA system with embeddings and similarity search.

Integrate with a local LLM (Ollama – e.g., gemma:2b).

Provide a simple web-based chat interface (Streamlit).

Show factual grounding by referencing the source content.

⚙️ Tech Stack
Component	Tool / Library
Programming	Python 3.10+
Embeddings	Hugging Face SentenceTransformers
Vector Store	FAISS
LLM	Ollama (gemma:2b)
Framework	LangChain
UI	Streamlit
Data	5–10 curated wellness text articles


🧰 Setup Guide
1️⃣ Environment Setup

Make sure you have Python ≥ 3.10 and Git installed. Then:

git clone <repo_url>
cd ZAFIX_Wellness_Task/Task2
python -m venv .venv
source .venv/bin/activate      # (Mac/Linux)
.venv\Scripts\activate         # (Windows)


Install dependencies:

pip install -r requirements.txt

2️⃣ Install and Run Ollama

If you don’t have Ollama:

https://ollama.ai/download


Pull your preferred local model (e.g.):

ollama pull gemma:2b


Check it works:

ollama run gemma:2b

3️⃣ Prepare Knowledge Base

Add 5–10 plain-text articles (.txt) into the data/ folder.
These can cover nutrition, fitness, health metrics, sleep, or longevity.

Example:

data/
├── article1.txt
├── article2.txt
├── article3.txt
├── article4.txt
└── article5.txt

4️⃣ Build the FAISS Embedding Index

Run this to convert your text files into vector embeddings:

python build_index.py


Expected output:

Total chunks prepared: 30
FAISS index saved to: src/embeddings/faiss_index

5️⃣ Test Console Agent

Run a terminal-based version:

python src/query_agent.py


Example:

🤖 AI Wellness Tutor is ready!
You: how much water should I drink daily?
AI: Most adults should aim for about 2–3 liters per day, though it depends on...
(Sources: hydration.txt)

6️⃣ Launch the Web Interface

Run:

streamlit run src/app.py


Your browser will open at:

http://localhost:8501


Ask questions like:

💬 “Explain how calorie intake affects metabolism”
💬 “Explain like I’m 10: what is a balanced diet?”

⚡ Stretch Features

✅ Retrieval-Augmented Generation (RAG) with FAISS

✅ Local LLM integration (Ollama)

✅ Source attribution for factual grounding

⚙️ (Optional) Add Mode Switching: “Explain Simply” vs “Scientific”

⚙️ (Optional) Add persistent chat history and multi-turn context

🧩 Troubleshooting
Problem	Fix
model 'gemma:2b' not found	Run ollama pull gemma:2b
NotImplementedError: meta tensor	Force CPU in HuggingFaceEmbeddings: model_kwargs={"device":"cpu"}
FAISS index not found	Re-run build_index.py to recreate embeddings
Streamlit doesn’t open	Run via streamlit run src/app.py, not plain Python
🧠 Example Workflow

Add health articles in data/

Run build_index.py to embed them

Launch app.py with Streamlit

Ask contextual health questions — answers come from your own data, not the web.