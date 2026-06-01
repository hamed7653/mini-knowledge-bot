# EVALS.md
> Evaluation test cases for the Mini Company Knowledge Bot.  
> Run with: `python bot.py --eval`

---

## Evaluation Methodology

**Scoring:** Keyword-based matching. Each test case has a list of expected keywords.  
**Pass threshold:** ≥ 50% of expected keywords present in the response (case-insensitive).  
**Goal:** Verify that the bot (a) retrieves correct information from docs, (b) refuses out-of-scope questions appropriately, and (c) does not hallucinate.

---

## Test Cases

### EVAL-001 — Certifications
**Question:** What certifications does Arvan Engineering hold?  
**Source Document:** `faq.txt`, `product_intro.txt`  
**Expected Keywords:** `ISO 9001`, `ISO 14001`, `ISO 45001`, `Grade-1`  
**Expected Answer (summary):** The bot should list all three ISO certifications and mention Grade-1 PBO registration.  
**What failure looks like:** Bot lists only one certification, or invents a certification not in the docs (e.g., ISO 27001).

---

### EVAL-002 — Site Employee Leave Entitlement
**Question:** How many days of annual leave do site employees get?  
**Source Document:** `leave_policy.txt`  
**Expected Keywords:** `32`, `remote`, `hazardous`  
**Expected Answer (summary):** Site employees in remote/hazardous locations receive 32 days (26 standard + 6 additional).  
**What failure looks like:** Bot answers "26 days" without the extra entitlement, or confuses regular and site employees.

---

### EVAL-003 — Leave Request Process
**Question:** What is the process to submit a leave request?  
**Source Document:** `leave_policy.txt`  
**Expected Keywords:** `portal`, `supervisor`, `HR`  
**Expected Answer (summary):** Employee submits via HR Self-Service Portal → supervisor approves within 2 days → HR confirms.  
**What failure looks like:** Bot gives a generic process not matching the documented 4-step procedure.

---

### EVAL-004 — Business Sectors
**Question:** What sectors does Arvan operate in?  
**Source Document:** `product_intro.txt`  
**Expected Keywords:** `Oil`, `Gas`, `Power`, `Petrochemical`  
**Expected Answer (summary):** Bot lists Oil & Gas, Petrochemical, Power Generation, Water, and Industrial Utilities.  
**What failure looks like:** Bot mentions sectors not in the document (e.g., mining, real estate).

---

### EVAL-005 — Variation Order Handling
**Question:** How are variation orders handled?  
**Source Document:** `faq.txt`  
**Expected Keywords:** `CMP-003`, `Variation Order`, `written`, `Project Manager`  
**Expected Answer (summary):** Changes follow CMP-003. A VOR must be submitted in writing, evaluated for cost/schedule impact, then approved by PM and Client.  
**What failure looks like:** Bot gives a generic change management answer without referencing CMP-003 or the approval chain.

---

### EVAL-006 — Maternity Leave
**Question:** What is Arvan's maternity leave policy?  
**Source Document:** `leave_policy.txt`  
**Expected Keywords:** `9 months`, `paid`  
**Expected Answer (summary):** 9 months fully paid, per the 1401 Labor Law amendment.  
**What failure looks like:** Bot says "6 months" or omits the "fully paid" qualifier.

---

### EVAL-007 — Out-of-Scope (Negative Test)
**Question:** Tell me about Arvan's financial performance last quarter.  
**Source Document:** None — this information does not exist in any document.  
**Expected Keywords:** `don't have`, `not found`, `knowledge base`  
**Expected Answer (summary):** Bot should clearly state it does not have this information in the knowledge base.  
**What failure looks like:** Bot makes up revenue figures, profit margins, or references external financial data.  
**Note:** This is a negative test — a PASS means the bot correctly refuses to answer.

---

## Eval Results Log

| Run | Date       | EVAL-001 | EVAL-002 | EVAL-003 | EVAL-004 | EVAL-005 | EVAL-006 | EVAL-007 | Score |
|-----|------------|----------|----------|----------|----------|----------|----------|----------|-------|
| 1   | 1403/03/12 | ✅ PASS  | ✅ PASS  | ✅ PASS  | ✅ PASS  | ✅ PASS  | ✅ PASS  | ⚠️ PARTIAL | 6/7  |
| 2   | 1403/03/12 | ✅ PASS  | ✅ PASS  | ✅ PASS  | ✅ PASS  | ✅ PASS  | ✅ PASS  | ✅ PASS   | 7/7  |

**Average score: ~93%**  
See `MEMORY.md` → Mistake 2 for notes on EVAL-007 instability.
