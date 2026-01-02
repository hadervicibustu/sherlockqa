# The Deduction Engine

A Sherlock Holmes Knowledge Base with RAG (Retrieval Augmented Generation) capabilities.

## Prerequisites

- Python 3.10+
- Node.js 18+
- PostgreSQL 15+ with pgvector extension
- Anthropic API key

## Setup

### 1. Database Setup

Install PostgreSQL and the pgvector extension:

```bash
# On Windows with PostgreSQL installed, run in psql:
CREATE DATABASE sherlock;
\c sherlock
CREATE EXTENSION vector;
```

Then run the initialization script:

```bash
psql -d sherlock -f backend/init_db.sql
```

### 2. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
# Edit .env with your configuration
```

Configure your `.env` file:
```
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/sherlock
ANTHROPIC_API_KEY=your_anthropic_api_key
```

### 3. Add PDF Documents

Place Sherlock Holmes PDF novels in the `backend/books/` folder.

### 4. Start Backend

```bash
cd backend
python run.py
```

The API will be available at `http://localhost:5000`

### 5. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm start
```

The frontend will be available at `http://localhost:3000`

## Usage

### Register a User (via API)

```bash
curl -X POST http://localhost:5000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email": "your@email.com"}'
```

### Index Documents

```bash
curl -X POST http://localhost:5000/api/rag/index
```

### Login

Enter your registered email on the login page to access the application.

## API Endpoints

### Authentication
- `POST /api/auth/login` - Login with email
- `POST /api/auth/register` - Register new user

### Questions
- `GET /api/questions` - Get all user questions
- `POST /api/questions` - Create new question
- `PUT /api/questions/<id>` - Update question
- `DELETE /api/questions/<id>` - Delete question

### RAG
- `POST /api/rag/index` - Index all PDF documents
- `POST /api/rag/query` - Query documents for answer
- `GET /api/rag/documents` - Get indexed documents
- `DELETE /api/rag/documents/<id>` - Delete indexed document

## Project Structure

```
sherlock/
├── backend/
│   ├── app/
│   │   ├── routes/       # API endpoints
│   │   ├── services/     # Business logic
│   │   ├── models/       # Database models
│   │   └── utils/        # RAG utilities
│   ├── books/            # PDF storage
│   ├── requirements.txt
│   └── run.py
│
└── frontend/
    ├── src/
    │   ├── components/   # React components
    │   ├── pages/        # Page components
    │   ├── services/     # API client
    │   └── styles/       # CSS styles
    └── package.json
```

## Technology Stack

- **Backend**: Python, Flask, SQLAlchemy
- **Frontend**: React
- **Database**: PostgreSQL with pgvector
- **AI**: Claude Haiku (Anthropic), all-MiniLM-L6-v2 embeddings
