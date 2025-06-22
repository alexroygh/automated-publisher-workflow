from scraping.fetch_chapter import fetch_chapter_and_screenshot
from ai_agents.agent_api import agentic_flow
from human_feedback.feedback_loop import human_feedback_loop
from versioning.chromadb_handler import store_version, search_version
from rl_search.rl_search import rl_search
from bs4 import BeautifulSoup
import os

# Create the output directory if it doesn't exist
os.makedirs("output", exist_ok=True)

URL = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"

html = fetch_chapter_and_screenshot(URL)

def extract_text_from_html(raw_html):
    soup = BeautifulSoup(raw_html, "html.parser")
    for tag in soup(["script", "style"]):
        tag.decompose()
    return soup.get_text(separator=" ", strip=True)

clean_text = extract_text_from_html(html)

with open("output/chapter_cleaned.txt", "w", encoding="utf-8") as f:
    f.write(clean_text)

ai_output = agentic_flow(clean_text)

final_output = human_feedback_loop(ai_output)

store_version(final_output, {"id": "book1_chapter1", "source": URL})

with open("output/chapter_final.txt", "w", encoding="utf-8") as f:
    f.write(final_output)

print("\nSearch Result:\n", rl_search("Chapter about island and voyage", search_version))






