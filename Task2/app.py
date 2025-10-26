# app.py
import os
import torch
import streamlit as st
from huggingface_hub import InferenceClient
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# === HF client & model ===
HF_TOKEN = os.getenv("HF_API_TOKEN")
if not HF_TOKEN:
    st.error("HF_API_TOKEN not found in environment. Set it as a secret in Spaces.")
    st.stop()

hf_client = InferenceClient(HF_TOKEN)
HF_MODEL_ID = "google/flan-t5-large"

def call_llm(prompt: str, max_new_tokens: int = 256) -> str:
    out = hf_client.text_generation(
        model=HF_MODEL_ID,
        inputs=prompt,
        parameters={"max_new_tokens": max_new_tokens}
    )
    if isinstance(out, list) and len(out) > 0 and "generated_text" in out[0]:
        return out[0]["generated_text"]
    return str(out)

# === Load FAISS index ===
index_path = os.path.abspath("src/embeddings/faiss_index")

# === Determine device for embeddings ===
device = "cuda" if torch.cuda.is_available() else "cpu"
st.write(f"Using device for embeddings: {device}")

# === Initialize embeddings ===
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": device}
)

# === Load FAISS vectorstore ===
vectorstore = FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)

# === Streamlit UI ===
st.set_page_config(page_title="AI Wellness Tutor", page_icon="🤖")
st.title("🤖 AI Wellness Tutor (Hugging Face Inference)")
st.markdown("Ask about health, nutrition, or wellness concepts — retrieval + HF LLM backend.")

mode = st.sidebar.selectbox(
    "Select Explanation Mode:",
    ["Normal", "Explain like I'm 10", "Explain scientifically"]
)

user_query = st.text_input("Ask your question:")

if st.button("Ask"):
    if user_query.strip() == "":
        st.warning("Please enter a question.")
    else:
        docs = vectorstore.similarity_search(user_query, k=3)
        context = "\n\n".join([d.page_content for d in docs])
        sources = [d.metadata.get("source", "unknown") for d in docs]

        mode_instruction = ""
        if mode == "Explain like I'm 10":
            mode_instruction = "Explain this in simple terms suitable for a 10-year-old."
        elif mode == "Explain scientifically":
            mode_instruction = "Provide a detailed, scientific explanation."

        prompt = f"Context:\n{context}\n\nQuestion: {user_query}\n{mode_instruction}\nAnswer:"
        answer = call_llm(prompt)

        st.subheader("💬 Tutor's Answer")
        st.write(answer)

        st.subheader("📚 Sources")
        for src in set(sources):
            st.markdown(f"- {src}")
