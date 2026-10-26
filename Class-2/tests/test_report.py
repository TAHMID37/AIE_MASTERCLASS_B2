import pytest

from ledger.parse import Call
from ledger.report import spend_by_model, total_spend, over_budget

CALLS = [
    Call("openai/gpt-oss-20b", 103, 130, "stop", "2026-11-01"),
    Call("openai/gpt-oss-120b", 118, 105, "stop", "2026-11-01"),
]


def test_total_spend():
    assert total_spend(CALLS) == pytest.approx(0.000046725 + 0.0000807)


def test_spend_by_model_has_one_entry_per_model():
    assert set(spend_by_model(CALLS)) == {"openai/gpt-oss-20b", "openai/gpt-oss-120b"}


def test_over_budget():
    assert over_budget(CALLS, budget=0.0001) is True
    assert over_budget(CALLS, budget=1.00) is False


def test_spend_by_model_repeated_calls_do_not_accumulate():
    first = spend_by_model(CALLS).copy()
    second = spend_by_model(CALLS)
    assert second == first
