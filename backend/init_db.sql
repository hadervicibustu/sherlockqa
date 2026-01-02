-- Sherlock Holmes Knowledge Base Database Initialization
-- Run this script to set up the database

-- Create database
CREATE DATABASE sherlock;

-- Connect to the sherlock database
\c sherlock

-- Enable pgvector extension
CREATE EXTENSION IF NOT EXISTS vector;

-- Users table
CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);

-- Documents table (tracks ingested PDFs)
CREATE TABLE IF NOT EXISTS documents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    filename VARCHAR(255) NOT NULL,
    title VARCHAR(500),
    file_hash VARCHAR(64) UNIQUE NOT NULL,
    indexed_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    chunk_count INTEGER DEFAULT 0
);

CREATE INDEX IF NOT EXISTS idx_documents_filename ON documents(filename);

-- Document chunks table (stores vectorized text segments)
CREATE TABLE IF NOT EXISTS document_chunks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    document_id UUID NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
    chunk_text TEXT NOT NULL,
    chunk_index INTEGER NOT NULL,
    embedding vector(384),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_chunks_document ON document_chunks(document_id);

-- Create IVFFlat index for vector similarity search
-- Note: This requires at least 100 rows to be effective
-- For smaller datasets, the index will still work but may not provide speedup
CREATE INDEX IF NOT EXISTS idx_chunks_embedding ON document_chunks
    USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);

-- Questions table (user Q&A storage)
CREATE TABLE IF NOT EXISTS questions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    question TEXT NOT NULL,
    answer TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_questions_user ON questions(user_id);
CREATE INDEX IF NOT EXISTS idx_questions_created ON questions(created_at DESC);

-- Insert default user
INSERT INTO users (email) VALUES ('hamida.dervic@outlook.com')
ON CONFLICT (email) DO NOTHING;

COMMENT ON TABLE users IS 'Registered users for the knowledge base application';
COMMENT ON TABLE documents IS 'Metadata for ingested PDF documents';
COMMENT ON TABLE document_chunks IS 'Text chunks with vector embeddings for RAG';
COMMENT ON TABLE questions IS 'User questions and answers';
