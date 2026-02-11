import requests
from sentence_transformers import SentenceTransformer

ENDEE_URL = "http://localhost:8080/api/v1/vector"

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "Endee is a high performance vector database written in C++",
    "Vector databases enable semantic search",
    "HNSW is used for fast approximate nearest neighbor search",
    "Semantic search retrieves information based on meaning"
]

for idx, text in enumerate(documents):
    embedding = model.encode(text).tolist()

    payload = {
        "id": str(idx),
        "vector": embedding,
        "metadata": {
            "text": text
        }
    }

    response = requests.put(ENDEE_URL, json=payload)
    print(f"Inserted document {idx} → Status {response.status_code}")
