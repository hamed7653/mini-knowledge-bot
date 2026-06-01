# 🤖 Mini Company Knowledge Bot
**Arvan Engineering & Construction Co. — Internal Q&A Assistant**

A lightweight CLI-based knowledge bot that answers employee and stakeholder questions using company documents as its knowledge base. Built with Python and the Anthropic Claude API.

---

## 📁 Project Structure

```
mini-knowledge-bot/
├── bot.py                   # Main application (CLI bot)
├── requirements.txt         # Python dependencies
├── README.md                # This file
├── docs/                    # Company knowledge base (plain text)
│   ├── faq.txt              # Frequently Asked Questions
│   ├── leave_policy.txt     # Employee Leave Policy (HR-POL-002)
│   └── product_intro.txt    # Services & Product Overview
└── agentic-brain/           # Project context & management docs
    ├── PROJECT_BRIEF.md
    ├── AGENT_CONTEXT.md
    ├── MEMORY.md
    ├── TASKS.md
    └── EVALS.md
```

---

## ⚡ Quick Start

### 1. Install dependencies
```bash
pip install anthropic
```

### 2. Set your API key
```bash
export ANTHROPIC_API_KEY=your_api_key_here
```

### 3. Run the bot

**Interactive mode (recommended for demo):**
```bash
python bot.py
```

**Single question mode:**
```bash
python bot.py "How many days of annual leave do I get?"
```

**Run the evaluation suite:**
```bash
python bot.py --eval
```

---

## 💬 Example Questions

```
What certifications does Arvan hold?
How do I request leave?
What sectors does the company work in?
How are variation orders handled?
What is the maternity leave policy?
How can I contact IT support?
```

---

## 🏗️ How It Works

1. **Load**: All `.txt` files in `docs/` are loaded into memory at startup
2. **Context**: Documents are combined into a single context block
3. **Prompt**: A strict system prompt instructs the model to only answer from provided documents
4. **Answer**: Claude returns a grounded, document-based response
5. **Eval**: The `--eval` flag runs 7 test cases with keyword-based pass/fail scoring

---

## 🧪 Evaluation

Run `python bot.py --eval` to execute the full EVALS suite.  
Results show per-question pass/fail and an overall score.  
See `agentic-brain/EVALS.md` for detailed test cases and expected answers.

---

## 🛠️ AI Tools Used

This project was built using **Claude** (claude.ai) for:
- Drafting company document content (`docs/*.txt`)
- Writing and iterating on `bot.py`
- Creating `agentic-brain/` documentation files

All AI outputs were reviewed, edited, and adapted to match realistic EPC industry context by the author.

---

## 📋 Extending the Knowledge Base

To add new documents, simply drop a `.txt` file into the `docs/` folder.  
The bot automatically loads all `.txt` files at startup — no code changes needed.
