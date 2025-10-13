import os
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
import pickle


# 1️⃣ Folder containing articles
docs_folder = "data"
index_folder = "src/embeddings"

os.makedirs(index_folder, exist_ok=True)

# 2️⃣ Read all articles
all_texts = []
all_sources = []

for filename in os.listdir(docs_folder):
    if filename.endswith(".txt"):
        with open(os.path.join(docs_folder, filename), "r", encoding="utf-8") as f:
            text = f.read()
            all_texts.append(text)
            all_sources.append(filename)

# 3️⃣ Split text into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    separators=["\n\n", ".", "!", "?", " ", ""]
)

chunks = []
metadata = []

for i, text in enumerate(all_texts):
    for chunk in text_splitter.split_text(text):
        chunks.append(chunk)
        metadata.append({"source": all_sources[i]})

print(f"Total chunks prepared: {len(chunks)}")

# 4️⃣ Create embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.from_texts(chunks, embeddings, metadatas=metadata)

# 5️⃣ Save FAISS index
# 5️⃣ Save FAISS index correctly
index_path = os.path.join(index_folder, "faiss_index")

vectorstore.save_local(index_path)
print(f"✅ FAISS index saved at: {index_path}")

# Optionally save metadata separately
with open(os.path.join(index_folder, "metadata.pkl"), "wb") as f:
    pickle.dump(metadata, f)
