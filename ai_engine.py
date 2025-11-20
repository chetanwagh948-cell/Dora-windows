import os
import openai

# 1) Put your API key here OR set environment variable OPENAI_API_KEY
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "YOUR_API_KEY_HERE")

client = openai.OpenAI(api_key=OPENAI_API_KEY)


def ask_dora(prompt: str) -> str:
    """
    Send a prompt to Dora's AI brain and return the reply text.
    """
    if not OPENAI_API_KEY or OPENAI_API_KEY == "YOUR_API_KEY_HERE":
        return "⚠️ OpenAI API key not set. Please add your key in ai_engine.py."

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are Dora, an intelligent coding and desktop assistant."},
                {"role": "user", "content": prompt},
            ],
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"⚠️ Error talking to Dora AI: {e}"
