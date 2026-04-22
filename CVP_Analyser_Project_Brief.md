# CVP Analyser Project Brief
## Context

I am Kunda Ng'ambi, a CIMA Dip MA student (Management Level).I am now building a **CVP Analyser Script** to automate CVP reporting. This is a personal learning project to develop genuine, defensible Python skills. I have completed Codecademy courses (Python 3, Intermediate, Advanced, OOP, Pandas, NumPy, SQL) but have not built an independent project without AI assistance before. **This project changes that.**

---
## Project Objective
Build a Python command-line tool that reads a CSV of product cost data and produces a single-product CVP report covering contribution margin, break-even, margin of safety, and target profit calculations.

1. Calculate contribution per unit and contribution ratio
2. Calculate break-even units and break-even revenue
3. Calculate margin of safety (units and %)
4. Calculate target profit units (given a user-supplied profit target(user input))
5. Output a clean formatted report
---
## Edge Cases

1. Negative target profit input.:
- Check if the supplied target profit is negative, and if so, warn the user: "Target profit is negative — this implies a planned loss, not a profit target."
2. Selling price <= variable cost (negative or zero contribution):
- After reading the CSV, immediately check if selling_price <= variable_cost.
If true, halt further calculations and print a clear error in the report: "Selling price does not exceed variable cost — no break-even point exists. Each unit sold deepens the loss."
Do not attempt to calculate or display break-even, margin of safety, or target profit in this state.
3. Fixed costs = 0 (trivial case):
- Allow the calculation to proceed normally — the math is valid.
Add a note in the report: "Fixed costs are zero — break-even is immediate (0 units)."
This prevents the user from thinking the output is an error.
4. Rounding on fractional break-even units:
- Always use math.ceil() (ceiling/round up) for break-even units, since you need to cover all fixed costs.
Derive break-even revenue from the ceiled unit figure (ceiled_units × selling_price) rather than calculating it independently — this keeps the two figures consistent.
Display the exact (unrounded) value alongside the ceiled value if useful, e.g.: "Break-even: 1,334 units (exact: 1,333.33)"
Apply the same ceiling logic to target profit units.
---

## Methodologies

**Fixed cost apportionment.** The ACCA article reports ZMW 200,000 in 
fixed costs for Company A as a whole (not split between products). For 
a single-product analysis of Product X, I apportioned fixed costs based 
on contribution share — Product X generates 72.73% of the company's 
total contribution (ZMW 400,000 of ZMW 550,000), so is allocated 
ZMW 145,455 of fixed costs. Rationale: products that generate more 
contribution have greater capacity to absorb fixed costs, making 
contribution-based apportionment more theoretically sound than 
unit-based or revenue-based methods for CVP analysis.
---
## Input Format


The script should accept a CSV file with the following structure:


| Product   | Selling Price(ZMW) | Variable Cost per Unit(ZMW) | Fixed Costs Attributable(ZMW) | Units |
|-----------|--------------------|-----------------------------|-------------------------------|-------|
| Product X | 50                 | 30                          | 145455                        | 20000 |

I will create my own sample CSV using real data from ACCA F5 Technical Article.
Using company A from the article.
The source data is published in USD (ACCA F5 article). I'm using ZMW labels for presentation consistency with my previous project; the numbers are treated as a generic currency unit.
---

## Required Output
The script must produce a report printed to the terminal. See the mock-up below for format.

### CVP Report
```
================================================================
CVP ANALYSIS — Product X (ACCA F5 Company A, apportioned)
================================================================
Selling Price per Unit            ZMW         50.00
Variable Cost per Unit            ZMW         30.00
Contribution per Unit             ZMW         20.00
Contribution Ratio                            40.00%

Fixed Costs                       ZMW    145,455.00
Break-Even (Units)                          7,273
Break-Even (Revenue)              ZMW    363,650.00

Expected Sales (Units)                     20,000
Expected Revenue                  ZMW  1,000,000.00
Margin of Safety (Units)                   12,727
Margin of Safety (%)                         63.64%

Target Profit                     ZMW     50,000.00
Units to Achieve Target                     9,773
================================================================
```
## Stretch Goals (only after core works)

These are optional. Only attempt after the core script runs correctly.

1. Performs a sensitivity analysis.
2. Creates a P/V Graph.
3. Multi-product CVP (v2) — Accept multiple products in the input CSV.
Calculate weighted average contribution margin, break-even for total revenue, 
and per-product contribution to break-even. This becomes a separate version (v2) rather than a feature added to v1.

---

## Rules of Engagement

### What I **CAN** do:

* Use Google, Stack Overflow, Python documentation, and my Codecademy notes
* Ask Claude to **explain a specific error message** I've been stuck on for 30+ minutes
* Ask Claude to **clarify a Python concept** (e.g., "what does .format() do?")
* Ask Claude to **review my finished code** and give feedback

### What I **CANNOT** do:

* Ask Claude (or any AI) to **write code for me**
* Ask Claude to **fix my bugs** — I can ask what an error means, but I figure out the fix myself
* Copy-paste code from AI tools
* Use GitHub Copilot or similar autocomplete tools

### How Claude should respond in this project:

* If I paste code and say "write this for me" or "fix this" — **refuse and redirect me**
* If I paste an error and say "what does this mean?" — **explain the error concept only, do not write the fix**
* If I ask "how do I do X?" — **point me to the right Python documentation or concept, do not write the implementation**
* If I submit finished code for review — **review it honestly: what's good, what's weak, what an interviewer would think**
* **Be ruthless.** If my code is bad, say so. If my logic is wrong, say so. Do not praise mediocre work.

---

### Technical Constraints
* Python 3.x only
* Standard library preferred for core (csv module, string formatting)
* External libraries allowed only for stretch goals (openpyxl, matplotlib, argparse)
* Script must run from the command line: `python cvp_report.py`
* Code must be readable, commented, and structured — not one giant block
---

### Deliverables

1. `cvp_report.py` — the main script
2. `sample_data.csv` — test CSV built from real public data
3. A screenshot or copy of the terminal output showing the report working
---

### Timeline

* Day 1: Read CSV, print parsed data 
* Day 2–3: Core calculations (contribution, break-even, margin of safety)
* Day 4: Target profit calculation with user input
* Day 5: Formatted output
* Day 6: Refactor into functions
* Day 7: Write README
* Day 8: Implement one stretch goal if time permits
* Day 9: Buffe
* Day 10: Polish + push to GitHub

---

### Why This Matters

This project exists so that when a recruiter or interviewer asks "tell me about your Python skills," I can open this script, walk through every line, explain why I made each decision, and demonstrate that I understand what the code does — because I wrote it myself. One real project I can defend beats ten certificates I can't.

### versions
- v1 accepts a single-row CSV. If multi-row, use only the first row and warn.
if user csv is malformed, crash with a useful error message


