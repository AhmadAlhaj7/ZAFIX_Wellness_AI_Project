🎯 Objective

Develop a frontend interface and reasoning engine for an AI tutor that interacts with learners, analyzes their progress, and provides intelligent feedback.

🧠 Core Logic
Module	Function
lesson_loader.py	Loads educational content (notes, PDFs, slides).
embedding_engine.py	Transforms study material into embeddings for contextual recall.
chat_engine.py	Handles the conversational logic between user and tutor.
ollama_interface.py	Connects to local LLM (e.g., phi3:mini, gemma:2b) for reasoning.
ui/app.py	Streamlit interface for interaction.
⚙️ Workflow
User → Streamlit UI
   ↓
Chat Engine → Interprets query
   ↓
Ollama Interface → LLM reasoning and response generation
   ↓
Output → Tutor feedback / Explanation / Guidance

🧩 Key Features

Real-time chat interface (Streamlit-based).

Local model integration via Ollama for data privacy.

Contextual responses grounded in loaded materials.

🧠 Example Flow

User asks: “Explain Newton’s second law.”
→ System retrieves related content
→ AI tutor summarizes and explains with examples.