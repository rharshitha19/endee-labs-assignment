from sentence_transformers import SentenceTransformer
import numpy as np

# Same model used during ingestion
model = SentenceTransformer("all-MiniLM-L6-v2")

# Documents (same as ingest.py)
documents = [
    "Endee is a high performance vector database written in C++",
    "Vector databases enable semantic search",
    "HNSW is used for fast approximate nearest neighbor search",
    "Semantic search retrieves information based on meaning"
]

# Create embeddings
doc_embeddings = model.encode(documents, normalize_embeddings=True)

# User query
query = "What is Endee used for?"
query_embedding = model.encode(query, normalize_embeddings=True)

# Cosine similarity
scores = np.dot(doc_embeddings, query_embedding)

# Rank results
top_k = 2
top_indices = np.argsort(scores)[::-1][:top_k]

print("\nSemantic Search Results:\n")
for idx in top_indices:
    print(f"- {documents[idx]} (score: {scores[idx]:.4f})")
