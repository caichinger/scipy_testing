
from hypothesis import given, assume  # <-- import assume
from hypothesis.strategies import lists, floats

def mean(x):
    return sum(x) / len(x)

# <-- do not allow nan, do not allow infinity
@given(x=lists(elements=floats(allow_nan=False, allow_infinity=False)))
def test_mean(x):
    assume(x)  # <-- assume that list is not empty
    assert min(x) <= mean(x) <= max(x)


if __name__ == '__main__':
    import pytest
    pytest.main([__file__])