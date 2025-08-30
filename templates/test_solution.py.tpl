from pathlib import Path
import runpy
import pytest


def _load_solution_cls():
    ns = runpy.run_path(str(Path(__file__).with_name("solutions.py")))
    # Prefer ALL_SOLUTIONS if present, otherwise single Solution class
    if "ALL_SOLUTIONS" in ns:
        return ns["ALL_SOLUTIONS"][0]
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
