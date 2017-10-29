import pytest

def fun():
    raise ZeroDivisionError(1)

def test_fun_raises_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        fun()