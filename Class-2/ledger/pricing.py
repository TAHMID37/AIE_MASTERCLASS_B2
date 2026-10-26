"""Prices and cost arithmetic.

All prices are in US dollars per MILLION tokens, the way every provider
publishes them.
"""

PRICES = {
    "openai/gpt-oss-20b":  {"in": 0.075, "out": 0.30},
    "openai/gpt-oss-120b": {"in": 0.15,  "out": 0.60},
    "qwen/qwen3.8-27b":    {"in": 0.80,  "out": 4.00},
}


def call_cost(model: str, in_tokens: int, out_tokens: int) -> float:
    """Return the dollar cost of one call."""
    if model not in PRICES:
        raise KeyError(f"unknown model: {model}")
    rate = PRICES[model]
    return in_tokens / 1_000_000 * rate["in"] + out_tokens / 1_000_000 * rate["out"]
