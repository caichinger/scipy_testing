
from hypothesis import given, assume, example  # <-- import assume, example
from hypothesis.strategies import lists, floats

def mean(x):
    return sum(x) / len(x)

# <-- do not allow nan, do not allow infinity
@example([0.1, 0.1, 0.1])
@given(x=lists(elements=floats(allow_nan=False, allow_infinity=False)))
def test_mean(x):
    assume(x)  # <-- assume that list is not empty
    assert min(x) - 1e-8 <= mean(x) <= max(x) + 1e-8


if __name__ == '__main__':
    import pytest
    pytest.main([__file__])