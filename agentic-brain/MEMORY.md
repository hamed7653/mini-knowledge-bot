# MEMORY.md
> Decisions made, mistakes encountered, lessons learned, and pivots taken during this project.

---

## Design Decisions & Rationale

### Decision 1: CLI over Web App
**When:** Early design phase  
**Decision:** Chose CLI (`argparse`) over a Flask/FastAPI web app  
**Why:** The goal is to demonstrate context management and document grounding, not frontend skills. CLI is simpler to demo via screenshots and requires zero deployment. A web app would add complexity without adding value to this evaluation.

### Decision 2: No Vector Database
**When:** Architecture phase  
**Decision:** Concatenate all docs into one prompt instead of using embeddings  
**Why:** With only 3 small documents (~3,000 tokens total), there is no need for retrieval. A vector DB (Chroma, FAISS) would be over-engineering for this scope and harder to explain in the AGENT_CONTEXT. Simpler = more maintainable.

### Decision 3: Plain `.txt` over Markdown or JSON
**When:** Docs structure phase  
**Decision:** Store knowledge base as `.txt` files  
**Why:** `.txt` is the most portable and readable format. No parsing required. Easy for non-technical team members to edit. Markdown headers could confuse the model; JSON adds unnecessary structure.

### Decision 4: Keyword-based EVAL scoring (not LLM-as-judge)
**When:** EVALS design  
**Decision:** Check for expected keywords in the response, not another LLM call  
**Why:** Keeps the eval fast, deterministic, and free of additional API costs. Keyword matching is transparent and auditable — you can see exactly which terms were matched or missed.

---

## Mistakes & Corrections

### Mistake 1: Overly permissive system prompt (v1)
**What happened:** Initial system prompt said "answer helpfully about Arvan Engineering." The model supplemented missing information with plausible hallucinations (invented phone numbers, fake project names).  
**Fix:** Rewrote system prompt with explicit restriction: "Only use information from the provided documents. If not found, say so explicitly."  
**Lesson:** For RAG-style bots, the system prompt's grounding rules are more important than the documents themselves.

### Mistake 2: EVAL-007 (out-of-scope question) gave partial answer
**What happened:** When asked about "financial performance last quarter," the model occasionally produced a vague answer like "Financial details are not available in the provided documents, however Arvan has completed 80+ projects worth $4B..."  
**Issue:** That last part comes from `product_intro.txt` and is technically grounded, but it's still an evasion of an out-of-scope query.  
**Fix:** Added stronger language in system prompt: "If the answer is not found in the documents, say ONLY: 'I don't have information about that in our current knowledge base.' Do not offer related facts."  
**Status:** Partially resolved. Model compliance is ~90%.

---

## Pivots

### Pivot: Added `--eval` flag instead of a separate `eval.py` script
**Original plan:** Create a separate `eval.py` file.  
**Changed to:** `--eval` flag in the main `bot.py`  
**Reason:** Keeps the project to a single executable file. Easier to demo. Less confusion about which file to run.

---

## Things Learned

- Claude API's `system` parameter is the right place for grounding rules (not the `user` message)
- `argparse` with `nargs="?"` for optional positional args allows both interactive and single-shot mode cleanly
- Keyword-based eval scoring needs at least 2-3 keywords per test case to avoid false positives
- Commit messages like "add docs" are useless; "add leave policy and FAQ for Arvan company knowledge base" is much better
