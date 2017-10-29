
from hypothesis import given
from hypothesis.strategies import lists, floats

def mean(x):
    return sum(x) / len(x)

@given(x=lists(elements=floats()))
def test_mean(x):
    assert min(x) <= mean(x) <= max(x)


if __name__ == '__main__':
    import pytest
    pytest.main([__file__])