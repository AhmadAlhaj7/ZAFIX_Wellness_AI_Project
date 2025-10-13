import os
import pickle
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import ollama
import os
print("Current working directory:", os.getcwd())

# === 1️⃣ Load FAISS index and metadata ===
index_path = "src/embeddings/faiss_index"
metadata_path = "src/embeddings/metadata.pkl"

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)

with open(metadata_path, "rb") as f:
    metadata = pickle.load(f)

# === 2️⃣ Retrieve relevant chunks ===
def retrieve_context(query, k=3):
    results = vectorstore.similarity_search(query, k=k)
    context = "\n\n".join([doc.page_content for doc in results])
    sources = [doc.metadata.get("source", "unknown") for doc in results]
    return context, sources

# === 3️⃣ Ask Ollama ===
def ask_tutor(query):
    context, sources = retrieve_context(query)
    prompt = f"""
You are a knowledgeable AI health tutor. Use the context below to answer the user's question clearly and accurately.
If the context doesn't provide enough information, say so honestly.

Context:
{context}

Question: {query}

Answer:
"""

    response = ollama.chat(model="gemma:2b", messages=[
        {"role": "system", "content": "You are a friendly and factual wellness tutor."},
        {"role": "user", "content": prompt}
    ])

    print("\n🧠 AI Tutor Response:\n")
    print(response["message"]["content"].strip())

    print("\n📚 Sources used:")
    for s in set(sources):
        print("-", s)

# === 4️⃣ Main loop ===
if __name__ == "__main__":
    print("🤖 AI Wellness Tutor is ready! Ask any wellness or nutrition question.\n")
    while True:
        query = input("You: ")
        if query.lower() in ["exit", "quit", "q"]:
            print("👋 Goodbye!")
            break
        ask_tutor(query)
