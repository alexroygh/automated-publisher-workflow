# Automated Publisher Workflow

## Overview
Automated Publisher is a human-in-the-loop, multi-phase book rewriting and publishing workflow powered by large language models (LLMs).

It performs the following steps:
1. Accepts raw chapter content (from a website, document, etc.)
2. Splits the content into manageable chunks
3. Uses LLMs for AI-assisted Writing, Reviewing, and Editing
4. Allows human feedback/edits at every phase
5. Outputs finalized, high-quality book content

## Key Features
- AI Writer, Reviewer, and Editor using OpenAI GPT-4
- Human feedback loop integrated at all stages
- Multi-iteration editing until user is satisfied
- Token-aware text chunking to fit LLM limits
- Modular structure for each agent and flow
- ChromaDB with SQLite backend for persistent versioning

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
python -m main.py
```

You’ll be prompted at every phase (Writer, Reviewer, Editor) to accept or revise the AI’s suggestions.

---

## Project Structure
```
.
├── ai_agents/
│   ├── ai_writer.py       # Handles AI writing
│   ├── ai_reviewer.py     # Handles grammar/style review
│   ├── ai_editor.py       # Handles final editorial polish
│   └── agent_api.py       # Orchestrates the full chunk-by-chunk flow
├── main.py                # entry script
└── README.md              # This file
```


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