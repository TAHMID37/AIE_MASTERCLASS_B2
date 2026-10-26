from ledger.parse import read_calls
from tests.conftest import SAMPLE


def test_reads_every_good_line():
    # 8 lines in the file: 6 good, 1 blank, 1 truncated
    calls = read_calls(SAMPLE)
    assert len(calls) == 6


def test_reports_bad_lines_by_line_number():
    errors = []
    read_calls(SAMPLE, errors=errors)
    assert errors == [6]          # line 6 is truncated; blank lines are not errors


def test_finish_reason_defaults_to_stop():
    calls = read_calls(SAMPLE)
    assert all(c.finish_reason in ("stop", "length") for c in calls)
