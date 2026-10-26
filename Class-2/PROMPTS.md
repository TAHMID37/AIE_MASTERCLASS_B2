# Class 2 Lab: Prompts

Work in order. Each exercise has a prompt to **copy and paste** into the
Antigravity agent panel, and a list of what **you** must check before moving on.

Rules for the whole lab:

- **Model:** Gemini 3.8 Flash. **Thinking:** Low, unless an exercise says otherwise.
- **New conversation for every exercise.** Old conversations carry old mistakes.
- **Commit after every green run:** `git add -A && git commit -m "exercise N"`.
  A commit is your undo button. Agents make mistakes. Commits make them cheap.
- **Read every diff before you accept it.** If you cannot explain a line, do not accept it.

---

## Exercise 0: Look before you leap (no agent)

Run the tests yourself:

    python -m pytest -q

Write down how many fail. You need this number to know whether the agent
made things better or worse.

---

## Exercise 1: Understand before you change

**Mode:** Fast. **Goal:** get oriented without changing a single file.

```text
Read this repository and AGENTS.md. Do not change any files.

Explain to me, as if I joined the team today:
1. What this program does, in two sentences.
2. Which file does what, one line each.
3. Run `python -m pytest -q` and tell me which tests fail and, for each one,
   your best guess at the cause. Guesses only. Do not fix anything yet.
```

**You check:**
- [ ] No files changed (`git status` shows nothing).
- [ ] It actually ran the tests, rather than guessing what they would say.
- [ ] Its guesses: write down which ones you think are right.

---

## Exercise 2: Plan, then fix the pricing bug

**Mode:** Planning. **Goal:** approve a plan before any code is written.

```text
Two tests in tests/test_pricing.py fail. Find the root cause.

Before changing any code, give me a plan that says:
- the root cause in one sentence
- the exact line you will change
- how you will prove it is fixed

Wait for my approval. Change only ledger/pricing.py.
After the change, run `python -m pytest -q` and show me the output.
```

**You check:**
- [ ] Read the plan. Leave **one comment** on it, even a small one, before you approve.
- [ ] The diff is one line. If it is more, ask why.
- [ ] `test_matches_the_class_1_notebook` passes. That number, $0.00004672, is the
      one you saw in Class 1. Same arithmetic, now inside a real program.
- [ ] Commit.

---

## Exercise 3: A surgical fix

**Mode:** Fast. **Goal:** a fix with hard limits on what it may touch.

```text
read_calls() in ledger/parse.py crashes on real log files.
data/sample_calls.jsonl has a blank line and a truncated line, like real logs do.

Required behaviour, from tests/test_parse.py:
- skip blank lines silently
- skip malformed lines, and if an `errors` list is passed in, append the
  1-based line number of each malformed line to it
- never crash on a bad line

Change only ledger/parse.py. Do not touch the tests.
Run `python -m pytest -q` and show me the output.
```

**You check:**
- [ ] Only `ledger/parse.py` changed.
- [ ] It catches specific exceptions, not a bare `except:`. A bare except hides real bugs.
      If it used one, tell it to fix that.
- [ ] Run `python -m ledger data/sample_calls.jsonl` yourself. It should not crash.
- [ ] Commit.

---

## Exercise 4: The bug no test catches

**Mode:** Planning. **Thinking:** Medium. **Goal:** make the agent prove a bug exists
before it is allowed to fix it.

All tests may be green now. There is still a bug. A user reports:

> "Our dashboard calls `spend_by_model()` every time the page refreshes.
> The numbers go up every refresh, even when no new calls happened."

**Prompt A: reproduce, do not fix**

```text
Bug report: calling spend_by_model() in ledger/report.py more than once
with the same calls gives different, growing totals.

Do NOT fix it yet.
1. Write one new test in tests/test_report.py that reproduces this bug.
2. Run it and show me that it FAILS.
3. Explain the root cause in two sentences.
Then stop.
```

**You check:**
- [ ] The new test fails, for the reason described. A test that passes here proves nothing.
- [ ] Do you understand the root cause? If not, ask it to explain again, more simply.
      This bug is a classic Python trap. You will meet it again.
- [ ] Commit the failing test.

**Prompt B: now fix it**

```text
Now fix the bug. Change only the function itself. Do not change any test.
Run `python -m pytest -q` and show me the output.
```

- [ ] The test you committed is unchanged (`git diff HEAD -- tests/` is empty).
- [ ] Everything passes. Commit.

---

## Exercise 5: Build a feature, tests first

**Mode:** Planning. **Goal:** a feature where the tests are written and agreed
before the code.

The feature, which you met in Class 1:

> A call that ends with `finish_reason == "length"` was cut off by `max_tokens`.
> You paid for it in full and probably got nothing useful.
> Add `wasted_spend(calls)` to ledger/report.py. It returns
> `(dollars, number_of_calls)` for cut-off calls only.
> The CLI prints one extra line: `wasted on cut-off answers $X across N calls`.

**Prompt A: tests only**

```text
Read the feature below. Write tests for it in a new file tests/test_waste.py.
Cover: a log with no cut-off calls, and the real sample log
(data/sample_calls.jsonl), which has exactly two.
Do NOT write the feature. Run the tests and show me they fail. Then stop.

Feature: wasted_spend(calls) in ledger/report.py returns (dollars, count)
for calls whose finish_reason is "length".
```

- [ ] Read the tests. Are the expected numbers right? Check one by hand:
      84 input tokens and 300 output tokens on gpt-oss-20b.
- [ ] They fail. Commit them.

**Prompt B: implement**

```text
Implement wasted_spend() in ledger/report.py and add the one-line output to
ledger/cli.py, as described. Do not change any file in tests/.
Run `python -m pytest -q` and `python -m ledger data/sample_calls.jsonl`
and show me both outputs.
```

- [ ] Tests unchanged, all green, CLI prints the new line. Commit.

---

## Exercise 6: Fresh eyes

**New conversation.** **Goal:** a review by an agent that did not write the code.

```text
You are reviewing a pull request. Do not change any files.

Run `git log --oneline` and `git diff HEAD~6` to see the changes made today.
Review them against AGENTS.md.

List problems in order of severity: bugs first, then anything that breaks
a rule in AGENTS.md, then style. For each one give the file, the line, and
why it matters. If you find nothing serious, say so; do not invent problems.
```

**You check:**
- [ ] Pick the one finding you most agree with and the one you most disagree with.
      Be ready to say why, out loud, in class.

---

## Exercise 7: Teach the rules file

No agent. **You** write this.

Add one line to the "How to work here" or "Never" section of `AGENTS.md`,
based on a mistake you actually watched the agent make today.

Write it yourself. Research from ETH Zurich (2026) found human-written
instruction files helped agents slightly, while auto-generated ones made
them slightly worse and every file added cost. One true line beats a page
of generic advice.

Commit it. This file is how today's mistake stops happening tomorrow.

---

## Hand in

Push the repo. Your `git log` should show one commit per exercise.
Add three lines to the README:

1. The exercise where the agent was most wrong, and how you caught it.
2. The line you added to AGENTS.md, and why.
3. One thing you would never let an agent do unreviewed.
