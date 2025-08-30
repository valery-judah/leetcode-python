from pathlib import Path
import runpy
import pytest


def _load_solution_cls():
    ns = runpy.run_path(str(Path(__file__).with_name("solution.py")))
    return ns["Solution"]


@pytest.fixture
def S():
    return _load_solution_cls()()

# TODO: replace with true signature and cases
@pytest.mark.parametrize(
    "args, kwargs, expected",
    [
        ((), {{}}, None),  # replace
    ],
)
def test_example(S, args, kwargs, expected):
    with pytest.raises(NotImplementedError):
        S.solve(*args, **kwargs)
