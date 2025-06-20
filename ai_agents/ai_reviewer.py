import os
import openai

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ai_reviewer(spun_text):
    prompt = f"You are an AI reviewer. Please improve the grammar, style, and coherence of the following rewritten book chapter.\n\n{spun_text}"
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a grammar and prose reviewer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=1000
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error generating AI reviewer output: {e}"