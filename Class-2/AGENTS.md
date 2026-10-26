# AGENTS.md

Read this before every task in this repository.

## What this project is

`ledger` reads a JSON Lines log of LLM calls and reports what they cost.
Prices in `ledger/pricing.py` are US dollars per **million** tokens.

## Commands

Always use this project's virtual environment. Never use the system Python.

- Windows: `.venv\Scripts\python`
- macOS / Linux: `.venv/bin/python`

Wherever these instructions or my prompts say `python`, use the one above.

- Run all tests: `python -m pytest -q`
- Run the tool: `python -m ledger data/sample_calls.jsonl --budget 0.001`
- On Windows PowerShell, run commands one at a time. Do not chain them with `&&`.

## How to work here

1. **Think before coding.** State your assumptions. If the request is ambiguous, ask me. Do not guess.
2. **Simplicity first.** Write the least code that solves the problem. No new dependencies. No new abstractions I did not ask for.
3. **Surgical changes.** Change only what the task needs. If you notice something else wrong, tell me, do not fix it.
4. **Prove it.** Every change ends with `python -m pytest -q` and you show me the output. "It should work" is not done.

## Never

- Never edit or delete a test to make it pass. If you think a test is wrong, stop and tell me why.
- Never run commands outside this fol
der.
- Never commit for me.