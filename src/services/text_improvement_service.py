from openai import OpenAI
from dotenv import load_dotenv
import os

class TextImprovementService:
    def __init__(self):
        load_dotenv()
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def improve_text(self, text):
        """Use OpenAI to improve the English language of the text"""
        if not text:
            return "No text was found in the clipboard."

        print("🧠 Sending text to AI for language improvement...")
        response = self.client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert English language editor. Your task is to revise the user's text to sound like it was written by a native English speaker while keeping it concise. Return ONLY the revised text without any explanations, comments, or quotes. Do not include phrases like 'Here's the revised version' or any other commentary."
                },
                {
                    "role": "user",
                    "content": f"Revise this comment to sound like it was written by a native English speaker while maintaining its concise and straightforward nature:\n\n{text}"
                }
            ],
            max_tokens=1000
        )

        return response.choices[0].message.content 