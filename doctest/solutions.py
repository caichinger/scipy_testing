"""
Doctest Exercises.
"""
import matplotlib.pyplot as plt
import numpy as np


def integrate_using_trapezoidal_rule(fun, x):
    """
    Implement a function that computes the area under a curve using the 
    [trapezoidal rule]()
    

    Examples
    --------
    >>> x = np.linspace(0, 1, 10)
    >>> def fun(x): 
    ...     return 0*x + 2
    >>> integrate_using_trapezoidal_rule(fun, x)
    2.0
    
    >>> x = np.linspace(0, 1, 10)
    >>> def fun(x):
    ...     return x
    >>> integrate_using_trapezoidal_rule(fun, x)
    0.5
    """    
    fun_x = fun(x)
    return ((fun_x[:-1] + fun_x[1:])/2 * np.diff(x)).sum()


def fancy_plot():
    """
    >>> fancy_plot()  # doctest: +ELLIPSIS
    <matplotlib.axes._subplots.AxesSubplot ... at ...>
    """
    fig, ax = plt.subplots()
    ax.plot([1, 2])
    return ax

def unordered_return_value():
    """
    >>> unordered_return_value() == {'a': 1, 'b': 2}
    True
    >>> sorted(unordered_return_value().items())
    [('a', 1), ('b', 2)]
    """
    return {'b': 2, 'a': 1}

def many_digit_number():
    """
    >>> print('{:.4f}'.format(many_digit_number()))
    0.0238
    >>> many_digit_number()  # doctest: +ELLIPSIS
    0.02380...
    """
    return 1/42

def some_exception():
    """
    >>> some_exception()
    Traceback (most recent call last):
    ...
    ZeroDivisionError: O.o
    """
    raise ZeroDivisionError('O.o')

def multiply(a, b):
    """
    Computes a * b
    
    >>> multiply(['A', 'B'], 2)  # doctest: +NORMALIZE_WHITESPACE
    ['A', 'B',
     'A', 'B']    
    >>> multiply(['A', 'B'], 2)
    ['A', 'B', 'A', 'B']
    """
    return a * b


if __name__ == '__main__':
    import doctest
    doctest.testmod()