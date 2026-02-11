# Endee Labs Assignment – Semantic Search

## Project Overview

This project demonstrates a simple implementation of Semantic Search using text embeddings and Endee OSS as the vector database.

Unlike traditional keyword search systems, semantic search retrieves documents based on meaning rather than exact word matching.

The objective of this project is to demonstrate how vector embeddings can be used to build a basic meaning-based search system.

---

## Problem Statement

Traditional keyword search relies on exact term matching. This often results in irrelevant results when:

- Different wording is used
- Synonyms are used
- Queries are phrased differently from stored documents

Semantic search addresses this limitation by converting text into numerical vectors (embeddings) and comparing similarity in vector space.

---

## Technical Approach / System Design

The system works in the following steps:

1. Documents are converted into embeddings using a pretrained SentenceTransformer model.
2. The embeddings are stored in a vector space.
3. A user query is converted into an embedding.
4. Cosine similarity is calculated between the query and stored embeddings.
5. The most similar documents are returned.

### Architecture Flow

User Query  
→ Generate Query Embedding  
→ Compare with Stored Embeddings  
→ Return Most Similar Results  

Endee OSS runs as the vector database engine inside Docker.

---

## How Endee is Used

Endee OSS is used as the vector database system in this project.

- It runs locally using Docker.
- It provides the vector indexing infrastructure.
- It represents the storage layer for vector-based search systems.
- The service runs on port 8080.

Although this project demonstrates a simple implementation, Endee serves as the underlying vector database engine.

---

## Project Structure

```
├── semantic-search/
│   ├── ingest.py
│   ├── search.py
│   └── README.md
│
├── docker-compose.yml
├── infra/
└── README.md
```

---

## Setup and Execution Instructions

### Prerequisites

- Docker Desktop
- Python 3.10+
- Git

---

### 1. Clone the Repository

```bash
git clone https://github.com/rharshitha19/endee-labs-assignment.git
cd endee-labs-assignment
```

---

### 2. Build and Start Endee OSS

```bash
docker build --build-arg BUILD_ARCH=avx2 -t endee-oss:latest -f infra/Dockerfile .
docker compose up
```

Wait until the server starts and runs on:

```
http://localhost:8080
```

Keep this terminal running.

---

### 3. Install Python Dependencies

Open a new terminal:

```bash
pip install sentence-transformers numpy requests
```

---

### 4. Ingest Documents

```bash
cd semantic-search
python ingest.py
```

---

### 5. Run Semantic Search

```bash
python search.py
```

---

## Limitations

- Small dataset used for demonstration
- No graphical user interface
- Basic similarity comparison only
- Not optimized for large-scale production deployment
- No advanced ranking or filtering mechanisms

---

## Conclusion

This project demonstrates a basic semantic search implementation using embeddings and a vector database system (Endee OSS). It provides a simple example of meaning-based information retrieval and showcases the fundamentals of vector search.
