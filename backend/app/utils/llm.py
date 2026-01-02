import anthropic
from ..config import Config


class LLMClient:
    """Client for interacting with Claude Haiku API."""

    def __init__(self):
        self.client = anthropic.Anthropic(api_key=Config.ANTHROPIC_API_KEY)
        self.model = "claude-3-haiku-20240307"

    def generate_answer(self, question: str, context_chunks: list[str]) -> str:
        """Generate an answer using retrieved context chunks."""
        # Format context
        context = "\n\n---\n\n".join(context_chunks)

        system_prompt = """You are an expert on Sherlock Holmes novels and stories by Sir Arthur Conan Doyle.
Your task is to answer questions about Sherlock Holmes based on the provided context from the novels.

Guidelines:
- Answer based ONLY on the provided context
- If the context doesn't contain enough information to answer the question, say so clearly
- Be concise but thorough in your answers
- Reference specific details from the context when relevant
- Maintain the Victorian-era atmosphere in your responses when appropriate"""

        user_prompt = f"""Context from Sherlock Holmes novels:

{context}

---

Question: {question}

Please provide a detailed answer based on the context above."""

        message = self.client.messages.create(
            model=self.model,
            max_tokens=1024,
            system=system_prompt,
            messages=[
                {"role": "user", "content": user_prompt}
            ]
        )

        return message.content[0].text
