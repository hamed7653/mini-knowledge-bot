# PROJECT_BRIEF.md

## What Was Built

**Mini Company Knowledge Bot** — a CLI-based Q&A assistant that answers questions about a fictional company (Arvan Engineering & Construction Co.) using plain-text documents as its sole knowledge source.

## MVP Definition

The MVP consists of:
1. A `docs/` folder with 3 company documents (FAQ, Leave Policy, Product Intro)
2. A single Python script (`bot.py`) that:
   - Loads all `.txt` files from `docs/` at startup
   - Accepts questions via CLI (interactive or single-shot)
   - Sends documents + question to Claude API
   - Returns a grounded answer based only on those documents
3. A built-in `--eval` mode to verify answer quality against 7 test cases

## MVP Boundaries (What Is NOT Included)

- No vector database or semantic search (all docs fit in one context window)
- No web UI or API server (CLI only)
- No persistent conversation history between sessions
- No authentication or multi-user support
- No document auto-update or file watching

## Tech Stack

| Component       | Choice              | Reason                                      |
|-----------------|---------------------|---------------------------------------------|
| Language        | Python 3.8+         | Widely available, minimal setup              |
| LLM             | Claude (Anthropic)  | High instruction-following, grounding        |
| Interface       | CLI (argparse)      | Simple, portable, no frontend needed         |
| Knowledge Store | Plain `.txt` files  | No DB required for small doc sets           |
| Eval            | Keyword matching    | Fast, transparent, no extra dependencies     |

## Project Size

~270 lines of Python, 3 knowledge documents, 5 agentic-brain files, 1 README.
