import pytest

from ledger.parse import Call, read_calls
from ledger.report import wasted_spend
from tests.conftest import SAMPLE


def test_wasted_spend_no_cutoff():
    calls = [
        Call("openai/gpt-oss-20b", 100, 100, "stop", "2026-11-01"),
        Call("openai/gpt-oss-120b", 200, 200, "stop", "2026-11-01"),
    ]
    dollars, count = wasted_spend(calls)
    assert count == 0
    assert dollars == pytest.approx(0.0)


def test_wasted_spend_sample_log():
    calls = read_calls(SAMPLE)
    dollars, count = wasted_spend(calls)
    assert count == 2
    # Two calls with length cut-off: both 84 in, 300 out on openai/gpt-oss-20b
    # (84 * 0.075 + 300 * 0.30) / 1_000_000 = 0.0000963 each -> 0.0001926 total
    assert dollars == pytest.approx(0.0001926)
