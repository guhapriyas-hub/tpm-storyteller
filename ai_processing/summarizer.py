import os
import openai

def summarize_text(text):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":f"Summarize this project data for executives:\n{text}"}],
        temperature=0.2,
        max_tokens=300
    )
    return response.choice[0].message.content