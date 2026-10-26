"""Turning a list of calls into numbers someone can act on."""
from .pricing import call_cost


def spend_by_model(calls, totals=None):
    """Total dollars per model."""
    if totals is None:
        totals = {}
    for c in calls:
        totals[c.model] = totals.get(c.model, 0.0) + call_cost(c.model, c.in_tokens, c.out_tokens)
    return totals


def total_spend(calls) -> float:
    return sum(call_cost(c.model, c.in_tokens, c.out_tokens) for c in calls)


def over_budget(calls, budget: float) -> bool:
    return total_spend(calls) > budget


def wasted_spend(calls) -> tuple[float, int]:
    cutoffs = [c for c in calls if c.finish_reason == "length"]
    dollars = sum(call_cost(c.model, c.in_tokens, c.out_tokens) for c in cutoffs)
    return dollars, len(cutoffs)

