# Class 2 Lab: Agentic Coding

A small, slightly broken Python project. You will fix it and extend it
**with an agent**, in Google Antigravity, without typing the fixes yourself.

The skill being practised is not "getting the agent to write code".
It is directing, constraining and checking an agent so that what it
writes is correct, small, and yours.

## Setup (10 minutes)

You need Python 3.12 (3.13 also works for this lab), Git, and Google Antigravity
(antigravity.google/download). Sign in to Antigravity with a **personal @gmail.com** account.

Type each line separately and press Enter after each one.
You never need to "activate" the environment: every command calls the
environment's own Python directly.

### Windows (PowerShell)

    cd $HOME\Downloads
    Expand-Archive .\class2-agentic-lab.zip -DestinationPath $HOME\Desktop
    cd $HOME\Desktop\class2-agentic-lab
    py -3.12 -m venv .venv
    .venv\Scripts\python -m pip install -r requirements.txt
    git init
    git add -A
    git commit -m "start"
    .venv\Scripts\python -m pytest -q

If `py -3.12` says that version is not found, run `py --list` to see what you
have and use that version instead, for example `py -3.13 -m venv .venv`.

### macOS or Linux (Terminal)

    cd ~/Downloads
    unzip class2-agentic-lab.zip -d ~/Desktop
    cd ~/Desktop/class2-agentic-lab
    python3.12 -m venv .venv
    .venv/bin/python -m pip install -r requirements.txt
    git init
    git add -A
    git commit -m "start"
    .venv/bin/python -m pytest -q

### What you should see

**6 failed, 4 passed.** That is the starting point. Then open this folder in
Antigravity and work through `PROMPTS.md` in order.

## Model settings for this lab

- Model: **Gemini 3.8 Flash**
- Thinking level: **Low** (raise it only for Exercise 4)

The free plan has a weekly quota that shrinks with how much work the agent
does. Small, precise tasks cost little. "Fix everything" costs a lot and
usually goes wrong. This whole lab fits inside the free quota if you follow the prompts.

## If something goes wrong

- `git` is not recognised: install Git from git-scm.com, then close and reopen PowerShell.
- `&&` is not a valid statement separator: you are in Windows PowerShell. Run each command on its own line.
- `No module named pytest`: you used the system Python. Use `.venv\Scripts\python` (Windows) or `.venv/bin/python` (macOS/Linux).
