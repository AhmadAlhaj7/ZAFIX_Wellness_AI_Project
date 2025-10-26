# query_agent.py
import os
import pickle
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from huggingface_hub import InferenceClient

print("Current working directory:", os.getcwd())

# === Hugging Face client (token via env / Spaces secret) ===
HF_TOKEN = os.getenv("HF_API_TOKEN")
if not HF_TOKEN:
    raise RuntimeError("HF_API_TOKEN not set in environment")
hf_client = InferenceClient(HF_TOKEN)

# Choose a hosted model for text generation (pick one ava ilable on HF)
HF_MODEL_ID = "google/flan-t5-large"  # change if you prefer a different HF model

def call_llm(prompt: str, max_new_tokens: int = 256) -> str:
    """Call HF Inference text-generation and return generated text."""
    out = hf_client.text_generation(
        model=HF_MODEL_ID,
        inputs=prompt,
        parameters={"max_new_tokens": max_new_tokens}
    )
    # Typical output: a list with a dict containing "generated_text"
    if isinstance(out, list) and len(out) > 0 and "generated_text" in out[0]:
        return out[0]["generated_text"]
    # Fallback: convert to string
    return str(out)

# === 1️⃣ Load FAISS index and metadata ===
index_path = "src/embeddings/faiss_index"
metadata_path = "src/embeddings/metadata.pkl"

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2",
                                   model_kwargs={"device": "cpu"})
vectorstore = FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)

with open(metadata_path, "rb") as f:
    metadata = pickle.load(f)

# === 2️⃣ Retrieve relevant chunks ===
def retrieve_context(query, k=3):
    results = vectorstore.similarity_search(query, k=k)
    context = "\n\n".join([doc.page_content for doc in results])
    sources = [doc.metadata.get("source", "unknown") for doc in results]
    return context, sources

# === 3️⃣ Ask the HF-backed tutor ===
def ask_tutor(query):
    context, sources = retrieve_context(query)
    prompt = f"""You are a knowledgeable AI health tutor. Use the context below to answer the user's question clearly and accurately.
If the context doesn't provide enough information, say so honestly.

Context:
{context}

Question: {query}

Answer:"""

    # Call HF Inference
    answer = call_llm(prompt)

    print("\n🧠 AI Tutor Response:\n")
    print(answer.strip())

    print("\n📚 Sources used:")
    for s in set(sources):
        print("-", s)

# === 4️⃣ Main loop ===
if __name__ == "__main__":
    print("🤖 AI Wellness Tutor (HF-backed) is ready! Ask any wellness or nutrition question.\n")
    while True:
        query = input("You: ")
        if query.lower() in ["exit", "quit", "q"]:
            print("👋 Goodbye!")
            break
        ask_tutor(query)
