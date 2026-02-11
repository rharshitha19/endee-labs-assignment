Semantic Search using Endee OSS
Project Overview

This project demonstrates a simple semantic search system using text embeddings and Endee OSS as the vector database.

Instead of matching exact words, semantic search compares the meaning of text using vector similarity.

Problem Statement

Keyword search depends on exact word matching.
If different wording or synonyms are used, results may not be relevant.

Semantic search solves this by:

Converting text into numerical vectors (embeddings)

Comparing vectors using similarity

Returning the most similar documents

Technical Approach

The system works in the following steps:

Documents are converted into embeddings using a pretrained SentenceTransformer model.

The embeddings are stored in memory.

A user query is converted into an embedding.

Cosine similarity is calculated between the query and stored embeddings.

The most similar documents are returned.

How Endee is Used

Endee OSS is used as the vector database engine and runs locally inside Docker.

It represents the vector database layer.

It runs on port 8080.

It provides the vector indexing infrastructure.

Project Structure
semantic-search/
├── ingest.py
├── search.py
├── README.md

Setup Instructions
1. Start Endee

From the project root:

docker build --build-arg BUILD_ARCH=avx2 -t endee-oss:latest -f infra/Dockerfile .
docker compose up


Keep this running.

2. Install Dependencies

In a new terminal:

pip install sentence-transformers numpy requests

3. Run Ingestion
python ingest.py

4. Run Search
python search.py

Limitations

Small dataset

No user interface

Basic similarity comparison only

Not designed for production use

Conclusion

This project demonstrates a basic implementation of semantic search using embeddings and a vector database system (Endee OSS).