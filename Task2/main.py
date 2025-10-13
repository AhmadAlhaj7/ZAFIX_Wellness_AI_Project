import os

def split_text(text, chunk_size=300):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append(chunk)
    return chunks

# Load all articles from docs/
docs_folder = "data"
all_chunks = []

for filename in os.listdir(docs_folder):
    if filename.endswith(".txt"):
        with open(os.path.join(docs_folder, filename), "r", encoding="utf-8") as f:
            text = f.read()
            chunks = split_text(text)
            # Store chunk text + source for grounding
            chunks = [{"text": c, "source": filename} for c in chunks]
            all_chunks.extend(chunks)

print(f"Total chunks prepared: {len(all_chunks)}")
