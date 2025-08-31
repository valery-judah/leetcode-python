import pytest
from common.testutil import S_fixture_for_this_dir, cases_from_solutions


# Use shared fixture; S yields the solution class, call S() to instantiate
S = S_fixture_for_this_dir(__file__)

# TODO: replace with true signature and cases
@pytest.mark.parametrize(("label", "args", "kwargs"), cases_from_solutions(__file__, "TEST_CASES"))
def test_example_raises_not_implemented(S, label, args, kwargs, run_summary):
    ok = False
    try:
        with pytest.raises(NotImplementedError):
            S().solve(*args, **kwargs)
        ok = True
    finally:
        run_summary[S.__name__].append((label, ok))
    assert ok
