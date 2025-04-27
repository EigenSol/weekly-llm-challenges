import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../'))

from groq import Groq
from traceback import format_exc

# Constants
GROQ_API_KEY = "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"
MODEL = "llama-3.3-70b-versatile"

# Big context
CONTEXT = """
You are an agent. you will help extract emails from html.
1. First of all, you will ask user for url.
2. then you will ask for the html on that url.
3. then you will extract all emails in that url. and you will provide a csv of all emails with # and email columns only.
"""

class SimpleGroqChat:
  def __init__(self, api_key, model, context):
    self.api_key = api_key
    self.model = model
    self.context = context
    self.client = Groq(api_key=self.api_key)

  def chat(self):
    while True:
      user_input = input("You: ")
      if user_input.lower() in ["exit", "quit"]:
        break

      try:
        response = self.client.chat.completions.create(
          model=self.model,
          messages=[
            {"role": "system", "content": self.context},
            {"role": "user", "content": user_input}
          ],
          temperature=0.7,
          max_tokens=100
        )
        reply = response.choices[0].message.content
        print(f"Bot: {reply}\n")

      except Exception as e:
        print(f"Error: {str(e)}\n{format_exc()}")

if __name__ == "__main__":
  bot = SimpleGroqChat(GROQ_API_KEY, MODEL, CONTEXT)
  bot.chat()
