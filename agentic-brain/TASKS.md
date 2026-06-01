# TASKS.md
> Completed tasks and remaining/future work.

---

## ✅ Completed

- [x] Define project scope and MVP — CLI-based knowledge bot for fictional EPC company
- [x] Create `docs/faq.txt` — 10 Q&A pairs covering services, tools, contacts, certifications
- [x] Create `docs/leave_policy.txt` — Full HR leave policy with 8 sections (annual, sick, maternity, etc.)
- [x] Create `docs/product_intro.txt` — Company background, service lines, sectors, flagship projects
- [x] Write `bot.py` — Main CLI application with load, ask, interactive, and eval modes
- [x] Write system prompt with strict grounding rules to prevent hallucination
- [x] Implement `--eval` mode with 7 test cases and keyword-based scoring
- [x] Write `README.md` with setup instructions and usage examples
- [x] Write `agentic-brain/PROJECT_BRIEF.md`
- [x] Write `agentic-brain/AGENT_CONTEXT.md`
- [x] Write `agentic-brain/MEMORY.md`
- [x] Write `agentic-brain/TASKS.md` (this file)
- [x] Write `agentic-brain/EVALS.md`
- [x] Create `requirements.txt`
- [x] Initialize Git repo and make meaningful commits
- [x] Test bot in interactive mode with 5+ manual questions
- [x] Test `--eval` mode and verify pass/fail logic

---

## 🔲 Future / Optional (Not in MVP)

- [ ] Add a 4th document: `support_guide.txt` — IT/HR internal support procedures
- [ ] Add conversation memory (multi-turn) so the bot remembers earlier context in the session
- [ ] Wrap `ask()` in a FastAPI endpoint: `GET /ask?q=...` for API mode
- [ ] Add streaming response output (print tokens as they arrive, not all at once)
- [ ] Build a simple web UI with HTML/JS that calls the API endpoint
- [ ] Add semantic search with `chromadb` for larger document sets (10+ files)
- [ ] Add Persian-language document support and test bilingual Q&A
- [ ] Add logging to a `.jsonl` file for audit trail of all questions asked
- [ ] Write a `Dockerfile` for containerized deployment
