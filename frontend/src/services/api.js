const API_BASE_URL = '/api';

class ApiError extends Error {
  constructor(message, status) {
    super(message);
    this.status = status;
    this.name = 'ApiError';
  }
}

async function request(endpoint, options = {}) {
  const url = `${API_BASE_URL}${endpoint}`;

  const { headers: optionHeaders, ...restOptions } = options;
  const config = {
    ...restOptions,
    headers: {
      'Content-Type': 'application/json',
      ...optionHeaders,
    },
  };

  try {
    const response = await fetch(url, config);
    const data = await response.json();

    if (!response.ok) {
      throw new ApiError(data.error || 'An error occurred', response.status);
    }

    return data;
  } catch (error) {
    if (error instanceof ApiError) {
      throw error;
    }
    throw new ApiError('Network error. Please try again.', 0);
  }
}

// Auth API
export const authApi = {
  login: (email) => request('/auth/login', {
    method: 'POST',
    body: JSON.stringify({ email }),
  }),

  register: (email) => request('/auth/register', {
    method: 'POST',
    body: JSON.stringify({ email }),
  }),

  getUser: (userId) => request(`/auth/user/${userId}`),
};

// Questions API
export const questionsApi = {
  getAll: (userId) => request('/questions', {
    headers: { 'X-User-ID': userId },
  }),

  getOne: (userId, questionId) => request(`/questions/${questionId}`, {
    headers: { 'X-User-ID': userId },
  }),

  create: (userId, question, answer = null) => request('/questions', {
    method: 'POST',
    headers: { 'X-User-ID': userId },
    body: JSON.stringify({ question, answer }),
  }),

  update: (userId, questionId, question, answer) => request(`/questions/${questionId}`, {
    method: 'PUT',
    headers: { 'X-User-ID': userId },
    body: JSON.stringify({ question, answer }),
  }),

  delete: (userId, questionId) => request(`/questions/${questionId}`, {
    method: 'DELETE',
    headers: { 'X-User-ID': userId },
  }),
};

// RAG API
export const ragApi = {
  indexDocuments: () => request('/rag/index', {
    method: 'POST',
  }),

  query: (question) => request('/rag/query', {
    method: 'POST',
    body: JSON.stringify({ question }),
  }),

  getDocuments: () => request('/rag/documents'),

  deleteDocument: (documentId) => request(`/rag/documents/${documentId}`, {
    method: 'DELETE',
  }),

  searchChunks: (query, topK = 3) => request('/rag/search', {
    method: 'POST',
    body: JSON.stringify({ query, top_k: topK }),
  }),
};

export { ApiError };
