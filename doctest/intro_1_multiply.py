"""
Module documentation.
This module provides the powerful `multiply` function.

>>> multiply(1, 2)
2
>>> multiply([3], 3)
[3, 3, 3]
"""

def multiply(a, b):
    """
    >>> multiply(6, 7)
    42   
    """
    return a * b


if __name__ == '__main__':
    import doctest
    doctest.testmod()