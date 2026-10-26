import pytest

from ledger.pricing import call_cost


def test_matches_the_class_1_notebook():
    # The exact call from Class 1: 103 in, 130 out on gpt-oss-20b printed $0.00004672
    assert call_cost("openai/gpt-oss-20b", 103, 130) == pytest.approx(0.000046725)


def test_output_tokens_cost_more_than_input():
    assert call_cost("openai/gpt-oss-120b", 0, 1000) > call_cost("openai/gpt-oss-120b", 1000, 0)


def test_one_million_input_tokens_costs_the_list_price():
    assert call_cost("qwen/qwen3.8-27b", 1_000_000, 0) == pytest.approx(0.80)


def test_unknown_model_is_an_error_not_a_zero():
    with pytest.raises(KeyError):
        call_cost("made-up-model", 10, 10)
