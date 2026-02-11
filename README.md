# Endee Labs Assignment – Semantic Search

## Project Overview

This project demonstrates a simple implementation of Semantic Search using text embeddings and Endee OSS as the vector database.

Unlike traditional keyword search systems, semantic search retrieves documents based on meaning rather than exact word matching.

---

## Problem Statement

Keyword-based search relies on exact word matching. This can produce irrelevant results when:

- Different wording is used
- Synonyms are used
- Queries are phrased differently from stored documents

Semantic search solves this by converting text into numerical vectors (embeddings) and comparing similarity in vector space.

---

## Technical Approach / System Design

The system works as follows:

1. Documents are converted into embeddings using a pretrained SentenceTransformer model.
2. Embeddings are stored in a vector space.
3. A user query is converted into an embedding.
4. Cosine similarity is computed between the query and stored embeddings.
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

- Docker Desktop installed and running
- Python 3.10+
- Git

---

### Step 1: Clone the Repository

```bash
git clone https://github.com/rharshitha19/endee-labs-assignment.git
cd endee-labs-assignment
```

---

### Step 2: Build and Start Endee OSS

```bash
docker build --build-arg BUILD_ARCH=avx2 -t endee-oss:latest -f infra/Dockerfile .
docker compose up
```

Wait until the server starts at:

```
http://localhost:8080
```

Keep this terminal running.

---

### Step 3: Install Python Dependencies

Open a new terminal and run:

```bash
pip install sentence-transformers numpy requests
```

---

### Step 4: Ingest Documents

Navigate to the semantic-search folder:

```bash
cd semantic-search
```

Run:

```bash
python ingest.py
```

This generates embeddings for the sample documents.

---

### Step 5: Run Semantic Search

After ingestion is complete, run:

```bash
python search.py
```

This performs similarity search on the embedded documents.

---

## Limitations

- Small dataset used for demonstration
- No graphical user interface
- Basic similarity comparison only
- Not optimized for large-scale production deployment

---

## Conclusion

This project demonstrates a basic semantic search system using embeddings and Endee OSS as the vector database. It provides a simple example of meaning-based information retrieval.
