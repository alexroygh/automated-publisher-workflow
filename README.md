# Automated Publisher Workflow

## Overview
Automated Publisher is a human-in-the-loop, multi-phase book rewriting and publishing workflow powered by large language models (LLMs).

It performs the following steps:
1. Accepts raw chapter content (from a website, document, etc.)
2. Parses and cleans the content using BeautifulSoup
3. Splits the content into manageable chunks using a token-aware strategy
4. Uses LLMs for AI-assisted Writing, Reviewing, and Editing
5. Allows human feedback/edits at every phase
6. Outputs finalized, high-quality book content

## Key Features
1. AI Writer, Reviewer, and Editor using OpenAI GPT-4
2. Human feedback loop integrated at all stages
3. Multi-iteration editing until user is satisfied
4. Token-aware text chunking to fit LLM limits and avoid 429 errors
5. BeautifulSoup to remove noise like navigation, script tags, and HTML artifacts
6. Modular structure for each agent and flow
7. ChromaDB with SQLite backend for persistent versioning

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/alexroygh/automated-publisher-workflow.git
cd automated-publisher-workflow
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set your OpenAI API key
```bash
export OPENAI_API_KEY=<your-key>
```

---

## Running the Program

1. Run the script:
```bash
python -m main
```

You'll be prompted at every phase (Writer, Reviewer, Editor) to accept or revise the AI's suggestions.

---

## Running Tests and Coverage

To run all unit tests:
```bash
pytest
```

To run tests with coverage reporting:
```bash
coverage run -m pytest && coverage report -m
```

---

## Project Structure
```
.
├── ai_agents/
│   ├── ai_writer.py       # Handles AI writing
│   ├── ai_reviewer.py     # Handles grammar/style review
│   ├── agent_api.py       # Orchestrates the full chunk-by-chunk flow
│   └── ai_editor.py       # Handles final editorial polish
├── versioning/
│   └── chromadb_handler.py # Versioning layer with persistent storage
├── scraping/
│   └── fetch_chapter.py   # Scrapes raw HTML and screenshots
├── human_feedback/
│   └── feedback_loop.py   # Interactive human review step
├── main.py                # entry script
└── README.md              # This file
```

---

## Chunking Strategy
To stay within token limits of GPT-4 and avoid rate-limit errors (429), I had to:
- Use character-based chunking (default ~2500 characters)
- Split by paragraph or sentence boundaries
- Ensure each chunk is independently understandable by the model

This allows reliable, parallel processing of long chapters.

---

## HTML Cleanup with BeautifulSoup
Used BeautifulSoup to extract clean text from noisy HTML content. This removes:
- Navigation links
- Scripts, styles, footers, headers
- Unnecessary whitespace and tags

---

## Prompts Used
### Writer Prompt:
```
You are a writer helping paraphrase raw web content into a clean, well-written chapter.

The input may include web artifacts like navigation menus, page footers, disclaimers, or HTML junk. Your task is to:
- Focus only on the actual chapter or story content
- Ignore non-literary text like "Wikisource", "edit", "navigation", headers, links, or references
- Paraphrase and rewrite the chapter in clean, flowing way.

INPUT:
```

### Reviewer Prompt:
```
You are a reviewer assisting in polishing draft chapter content.

Your tasks are to:
- Improve clarity, grammar, and structure
- Ensure a consistent writing tone
- Eliminate repetition or awkward phrasing
- Remove any residual web-related language or formatting

Do not introduce new information.

Review the following draft:
```

### Editor Prompt:
```
You are an editor performing a final polish on a book chapter.

Ensure the output is:
- Clean, well-formatted, and publication-ready
- Free of spelling, grammar, or formatting errors
- Structured into paragraphs for readability
- Completely devoid of web-related junk like navigation labels or page metadata

Do not change the meaning of the text.

Finalize this text:
```

---

## Viewing Stored Records in ChromaDB

The project uses ChromaDB with a **persistent SQLite backend**. You can browse the stored content using the built-in SQLite CLI or any GUI tool.

### Option 1: With SQLite CLI
1. Navigate to the storage path:
```bash
cd chroma_store
```
2. Launch the SQLite shell:
```bash
sqlite3 chroma.sqlite3
```
3. List all tables:
```sql
.tables
```
4. View data:
```sql
SELECT * FROM collections;
SELECT * FROM segments LIMIT 5;
SELECT * FROM embeddings LIMIT 5;
```
5. Exit:
```sql
.exit
```

### Option 2: Use a GUI
You can inspect `./chroma_store/chroma.sqlite3` using:
- [DB Browser for SQLite](https://sqlitebrowser.org/)
- [DBeaver](https://dbeaver.io/)

---
