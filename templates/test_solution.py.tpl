
import pytest
from .solution import Solution

@pytest.fixture
def S():
    return Solution()

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
