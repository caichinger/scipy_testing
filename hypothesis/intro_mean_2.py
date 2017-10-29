
from hypothesis import given, assume  # <-- import assume
from hypothesis.strategies import lists, floats

def mean(x):
    return sum(x) / len(x)

@given(x=lists(elements=floats(allow_nan=False)))  # <-- do not allow nan
def test_mean(x):
    assume(x)  # <-- assume that list is not empty
    assert min(x) <= mean(x) <= max(x)


if __name__ == '__main__':
    import pytest
    pytest.main([__file__])