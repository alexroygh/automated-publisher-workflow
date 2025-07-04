import os
import openai

def ai_editor(reviewed_text):
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    prompt = f"""You are an editor performing a final polish on a book chapter.
    Ensure the output is:
    - Clean, well-formatted, and publication-ready
    - Free of spelling, grammar, or formatting errors
    - Structured into paragraphs for readability
    - Completely devoid of web-related junk like navigation labels or page metadata

    Do not change the meaning of the text.

    Finalize this text:

    {reviewed_text}"""

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a meticulous editor for final publication."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4,
            max_tokens=1000
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error generating AI editor output: {e}"