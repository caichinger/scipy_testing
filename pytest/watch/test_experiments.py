from experiments import fun


def test_fun():
    assert fun(2) == 2


if __name__ == '__main__':
    import pytest
    pytest.main([__file__])
