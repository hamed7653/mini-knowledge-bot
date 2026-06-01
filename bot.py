#!/usr/bin/env python3
"""
Mini Company Knowledge Bot
Arvan Engineering & Construction Co. — Internal Q&A Assistant

Usage:
    python bot.py                  # Interactive mode
    python bot.py "your question"  # Single question mode
    python bot.py --eval           # Run built-in EVALS
"""

import os
import sys
import glob
import argparse
from pathlib import Path

try:
    import anthropic
except ImportError:
    print("ERROR: anthropic package not installed.")
    print("Run: pip install anthropic")
    sys.exit(1)


DOCS_DIR = Path(__file__).parent / "docs"
MODEL = "claude-sonnet-4-6"


def load_documents() -> dict[str, str]:
    """Load all .txt files from the docs/ directory."""
    docs = {}
    txt_files = glob.glob(str(DOCS_DIR / "*.txt"))
    if not txt_files:
        print(f"WARNING: No .txt files found in {DOCS_DIR}")
        return docs
    for filepath in txt_files:
        name = Path(filepath).stem
        with open(filepath, "r", encoding="utf-8") as f:
            docs[name] = f.read()
    return docs


def build_context(docs: dict[str, str]) -> str:
    """Combine all documents into a single context string for the prompt."""
    sections = []
    for name, content in docs.items():
        sections.append(f"=== DOCUMENT: {name.upper()} ===\n{content}")
    return "\n\n".join(sections)


def build_system_prompt(context: str) -> str:
    return f"""You are an internal knowledge assistant for Arvan Engineering & Construction Co.
Your job is to answer employee and stakeholder questions strictly based on the company documents provided below.

RULES:
- Only use information from the provided documents. Do not use outside knowledge.
- If the answer is not found in the documents, say: "I don't have information about that in our current knowledge base."
- Be concise and professional. Use bullet points for multi-part answers.
- When referencing a policy or procedure, mention the document it comes from.
- Do not make up names, numbers, or dates that are not in the documents.

--- COMPANY KNOWLEDGE BASE ---
{context}
--- END OF KNOWLEDGE BASE ---
"""


def ask(question: str, docs: dict[str, str]) -> str:
    """Send a question to the bot and return the answer."""
    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    context = build_context(docs)
    system_prompt = build_system_prompt(context)

    response = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        system=system_prompt,
        messages=[{"role": "user", "content": question}],
    )
    return response.content[0].text


def run_evals(docs: dict[str, str]):
    """Run the built-in evaluation suite from EVALS.md."""
    evals = [
        {
            "id": "EVAL-001",
            "question": "What certifications does Arvan Engineering hold?",
            "expected_keywords": ["ISO 9001", "ISO 14001", "ISO 45001", "Grade-1"],
        },
        {
            "id": "EVAL-002",
            "question": "How many days of annual leave do site employees get?",
            "expected_keywords": ["32", "remote", "hazardous"],
        },
        {
            "id": "EVAL-003",
            "question": "What is the process to submit a leave request?",
            "expected_keywords": ["portal", "supervisor", "HR"],
        },
        {
            "id": "EVAL-004",
            "question": "What sectors does Arvan operate in?",
            "expected_keywords": ["Oil", "Gas", "Power", "Petrochemical"],
        },
        {
            "id": "EVAL-005",
            "question": "How are variation orders handled?",
            "expected_keywords": ["CMP-003", "Variation Order", "written", "Project Manager"],
        },
        {
            "id": "EVAL-006",
            "question": "What is Arvan's maternity leave policy?",
            "expected_keywords": ["9 months", "paid"],
        },
        {
            "id": "EVAL-007",
            "question": "Tell me about Arvan's financial performance last quarter.",
            "expected_keywords": ["don't have", "not found", "knowledge base"],
        },
    ]

    print("\n" + "=" * 60)
    print("RUNNING EVALUATION SUITE")
    print("=" * 60)

    passed = 0
    failed = 0

    for eval_case in evals:
        print(f"\n[{eval_case['id']}] {eval_case['question']}")
        print("-" * 50)
        answer = ask(eval_case["question"], docs)
        print(f"ANSWER: {answer[:300]}{'...' if len(answer) > 300 else ''}")

        # Simple keyword check
        answer_lower = answer.lower()
        hits = [kw for kw in eval_case["expected_keywords"] if kw.lower() in answer_lower]
        score = len(hits) / len(eval_case["expected_keywords"])

        if score >= 0.5:
            print(f"✅ PASS (keywords matched: {hits})")
            passed += 1
        else:
            print(f"❌ FAIL (expected keywords: {eval_case['expected_keywords']}, got hits: {hits})")
            failed += 1

    print("\n" + "=" * 60)
    print(f"EVAL RESULTS: {passed}/{passed+failed} passed ({100*passed//(passed+failed)}%)")
    print("=" * 60)


def interactive_mode(docs: dict[str, str]):
    """Run the bot in interactive CLI mode."""
    print("\n" + "=" * 60)
    print("  ARVAN ENGINEERING — COMPANY KNOWLEDGE BOT")
    print("  Type your question and press Enter.")
    print("  Type 'exit' or 'quit' to stop.")
    print("=" * 60)
    print(f"  Loaded {len(docs)} document(s): {', '.join(docs.keys())}")
    print("=" * 60 + "\n")

    while True:
        try:
            question = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

        if not question:
            continue
        if question.lower() in ("exit", "quit", "bye"):
            print("Goodbye!")
            break

        print("\nBot: ", end="", flush=True)
        answer = ask(question, docs)
        print(answer)
        print()


def main():
    parser = argparse.ArgumentParser(
        description="Arvan Engineering — Mini Company Knowledge Bot"
    )
    parser.add_argument(
        "question",
        nargs="?",
        help="Ask a single question (optional; omit for interactive mode)",
    )
    parser.add_argument(
        "--eval",
        action="store_true",
        help="Run the built-in evaluation suite",
    )
    args = parser.parse_args()

    # Check API key
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY environment variable not set.")
        print("Set it with: export ANTHROPIC_API_KEY=your_key_here")
        sys.exit(1)

    # Load documents
    docs = load_documents()
    if not docs:
        print("ERROR: No documents loaded. Check the docs/ folder.")
        sys.exit(1)

    print(f"✓ Loaded {len(docs)} document(s) from docs/")

    if args.eval:
        run_evals(docs)
    elif args.question:
        answer = ask(args.question, docs)
        print(f"\nBot: {answer}")
    else:
        interactive_mode(docs)


if __name__ == "__main__":
    main()
