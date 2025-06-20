import os
import openai

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ai_writer(chapter_text):
    prompt = f"You are an AI book writer. Rewrite the following text with a creative twist while preserving its original meaning.\n\n{chapter_text}"
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful creative writing assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
            max_tokens=1000
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error generating AI writer output: {e}"