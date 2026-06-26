import os

from google import genai
from google.genai import types

from app.config import GOOGLE_API_KEY


class GeminiLLM:

    def __init__(self):

        self.client = genai.Client(
            api_key=GOOGLE_API_KEY
        )

    def generate_answer(self, question, retrieved_chunks, conversation):

        context = ""

        for chunk in retrieved_chunks:

            context += f"""
        Source File: {chunk['filename']}
        Page Number: {chunk['page']}

        Content:
    {chunk['content']}

-----------------------------------------
"""

        prompt = f"""
You are an expert AI assistant.

use ONLY from the provided context.

If the answer can not be found, reply:

"I could not find the answer in the uploaded documents."

For every answer:

1. Give us clear explanation.
2. Use bullet points if needed.
3. At teh end mention the source file(s) and page number(s) used.

Conversation History:
{conversation}

Context:

{context}

Question:

{question}

Answer:
"""

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.2
            )
        )

        return response.text