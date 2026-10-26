"""Reading the call log.

The log is JSON Lines: one JSON object per line, one line per LLM call.
Real logs are messy. Lines get truncated, people paste blank lines, a
deploy writes half a record. A parser that dies on line 3,000 of a
10,000-line log is useless.
"""
import json
from dataclasses import dataclass


@dataclass
class Call:
    model: str
    in_tokens: int
    out_tokens: int
    finish_reason: str
    day: str          # YYYY-MM-DD


def read_calls(path: str, errors: list[int] | None = None) -> list[Call]:
    calls = []
    with open(path, encoding="utf-8") as f:
        for lineno, line in enumerate(f, start=1):
            stripped = line.strip()
            if not stripped:
                continue
            try:
                row = json.loads(line)
                calls.append(
                    Call(
                        model=row["model"],
                        in_tokens=int(row["in_tokens"]),
                        out_tokens=int(row["out_tokens"]),
                        finish_reason=row.get("finish_reason", "stop"),
                        day=row["day"],
                    )
                )
            except Exception:
                if errors is not None:
                    errors.append(lineno)
    return calls
