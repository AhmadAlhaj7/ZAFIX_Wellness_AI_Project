import streamlit as st
import os
import torch
import ollama
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# === Load FAISS index ===
index_path = os.path.abspath("src/embeddings/faiss_index")

# === Determine device ===
device = "cuda" if torch.cuda.is_available() else "cpu"
st.write(f"Using device: {device}")

# === Initialize embeddings correctly ===
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": device}  # Forces CPU or GPU
)

# === Load the FAISS vectorstore ===
vectorstore = FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)

# === Streamlit app configuration ===
st.set_page_config(page_title="AI Wellness Tutor", page_icon="🤖")
st.title("🤖 AI Wellness Tutor")
st.markdown(
    "Ask about health, nutrition, or wellness concepts — powered by local AI (Ollama + FAISS)."
)

# === Sidebar mode selection ===
mode = st.sidebar.selectbox(
    "Select Explanation Mode:",
    ["Normal", "Explain like I'm 10", "Explain scientifically"]
)

# === Input field ===
user_query = st.text_input("Ask your question:")

if st.button("Ask"):
    if user_query.strip() == "":
        st.warning("Please enter a question.")
    else:
        # 1️⃣ Retrieve relevant chunks
        docs = vectorstore.similarity_search(user_query, k=3)
        context = "\n\n".join([d.page_content for d in docs])
        sources = [d.metadata.get("source", "unknown") for d in docs]

        # 2️⃣ Mode prompt
        mode_instruction = ""
        if mode == "Explain like I'm 10":
            mode_instruction = "Explain this in simple terms suitable for a 10-year-old."
        elif mode == "Explain scientifically":
            mode_instruction = "Provide a detailed, scientific explanation."

        # 3️⃣ Query Ollama model
        prompt = f"Context:\n{context}\n\nQuestion: {user_query}\n{mode_instruction}\nAnswer:"
        response = ollama.chat(
            model="gemma:2b",
            messages=[{"role": "user", "content": prompt}]
        )

        # 4️⃣ Display results
        st.subheader("💬 Tutor's Answer")
        st.write(response['message']['content'])

        st.subheader("📚 Sources")
        for src in set(sources):
            st.markdown(f"- {src}")
