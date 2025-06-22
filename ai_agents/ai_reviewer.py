import os
import openai

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ai_reviewer(spun_text):
    prompt = f"""You are a reviewer assisting in polishing draft chapter content.
    Your tasks are to:
    - Improve clarity, grammar, and structure
    - Ensure a consistent writing tone
    - Eliminate repetition or awkward phrasing
    - Remove any residual web-related language or formatting

    Do not introduce new information.

    Review the following draft:

    {spun_text}"""

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