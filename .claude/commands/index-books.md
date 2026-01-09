# Index Books for RAG

Index all PDF books from the `backend/books` folder into the RAG system.

## Instructions

Make a POST request to the `/api/rag/index` endpoint to index all books in the backend/books folder.

1. First, check if the backend server is running by making a simple request
2. Call the index endpoint using curl or a similar tool:
   ```
   curl -X POST http://localhost:5000/api/rag/index
   ```
3. Report the results to the user, including:
   - Number of documents indexed
   - Any errors that occurred
   - List of indexed document titles if available

If the server is not running, inform the user they need to start the backend server first with:
```
cd backend && python run.py
```

The endpoint will:
- Scan the `backend/books/` folder for PDF files
- Extract text and create semantic chunks
- Generate embeddings using the all-MiniLM-L6-v2 model
- Store chunks and embeddings in PostgreSQL with pgvector
