"""Command line entry point.

    python -m ledger data/sample_calls.jsonl --budget 0.01
"""
import argparse

from .parse import read_calls
from .report import spend_by_model, total_spend, over_budget, wasted_spend


def main(argv=None):
    ap = argparse.ArgumentParser(prog="ledger")
    ap.add_argument("path")
    ap.add_argument("--budget", type=float, default=None)
    args = ap.parse_args(argv)

    calls = read_calls(args.path)
    print(f"{len(calls)} calls")
    for model, dollars in sorted(spend_by_model(calls).items(), key=lambda kv: -kv[1]):
        print(f"  {model:24} ${dollars:.6f}")
    print(f"total ${total_spend(calls):.6f}")
    wasted_dollars, wasted_count = wasted_spend(calls)
    print(f"wasted on cut-off answers ${wasted_dollars:.6f} across {wasted_count} calls")
    if args.budget is not None:
        print("OVER BUDGET" if over_budget(calls, args.budget) else "within budget")


if __name__ == "__main__":
    main()
