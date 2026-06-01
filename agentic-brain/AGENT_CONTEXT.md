# AGENT_CONTEXT.md
> **For any AI agent (Claude Code or otherwise) picking up this project:**  
> Read this file first. It tells you what exists, what decisions were made, and how to continue.

---

## What This Project Is

A minimal CLI-based company knowledge bot. The user runs `python bot.py`, types a question, and the bot answers using only the `.txt` files in `docs/`. No database, no web server, no frontend.

## Repository Layout (What Each File Does)

```
bot.py                   ← MAIN ENTRY POINT. Run this.
requirements.txt         ← Only one dependency: anthropic
docs/faq.txt             ← Company FAQ (10 Q&A pairs)
docs/leave_policy.txt    ← HR leave policy (8 sections)
docs/product_intro.txt   ← Services overview & project history
agentic-brain/           ← This folder. Project management docs only.
```

## How the Bot Works (Architecture in Plain English)

1. Load all `docs/*.txt` → concatenate into one big string
2. Build a system prompt: "You are an assistant. Answer ONLY from these documents."
3. User types question → send (system prompt + question) to Claude API
4. Print the response

That's it. No embeddings, no chunking, no retrieval. The entire knowledge base fits in one API call.

## Key Design Decisions

| Decision | Rationale |
|---|---|
| No vector DB | 3 small docs easily fit in Claude's context window |
| Plain `.txt` for docs | Easy to edit, no parsing overhead |
| Keyword-based EVAL | No extra deps; transparent pass/fail logic |
| `argparse` for CLI | Standard library, no additional install |
| Strict system prompt | Prevents hallucination; forces grounding |

## Environment Requirements

```bash
ANTHROPIC_API_KEY=sk-ant-...   # Must be set before running
```
Python 3.8+, one pip install: `pip install anthropic`

## How to Continue / Extend This Project

**To add more documents:** Drop any `.txt` file into `docs/`. Bot auto-loads it.

**To improve answer quality:** Edit the system prompt in `build_system_prompt()` inside `bot.py`.

**To add a web API:** Wrap the `ask()` function with FastAPI:
```python
from fastapi import FastAPI
app = FastAPI()
@app.get("/ask")
def query(q: str):
    return {"answer": ask(q, load_documents())}
```

**To add semantic search (future):** Use `chromadb` or `faiss` for chunked embeddings when doc count exceeds ~20 files.

**To add conversation history:** Maintain a `messages` list across turns instead of sending single-turn messages.

## Current State

- All 3 docs written and loaded correctly
- Bot runs in interactive and single-shot mode
- Eval suite passes 6/7 cases (EVAL-007 out-of-scope test occasionally triggers partial answer — see MEMORY.md)
- README is complete and accurate
