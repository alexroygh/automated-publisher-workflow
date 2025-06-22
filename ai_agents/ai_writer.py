import os
import openai

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ai_writer(chapter_text):
    prompt = f"""You are a writer helping paraphrase raw web content into a clean, well-written chapter.

    The input may include web artifacts like navigation menus, page footers, disclaimers, or HTML junk. Your task is to:
    - Focus only on the actual chapter or story content
    - Ignore non-literary text like "Wikisource", "edit", "navigation", headers, links, or references
    - Paraphrase and rewrite the chapter in clean, flowing way.
    
    INPUT:
    {chapter_text}"""

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