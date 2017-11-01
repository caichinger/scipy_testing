"""
Possible approach to the Adam's Patch problem.
"""
import pytest
import numpy as np
import numpy.testing as npt

from adams_patch import (area_under_curve, 
                         compute_inverse_function_value, 
                         inverse_area_under_curve, 
                         compute_covered_area, 
                         optimize_patch_area)

@pytest.mark.parametrize('fun,xmin_xmax,integral', [
    (lambda x: 0*x + 1, (0, 1), 1),
    (lambda x: 1*x + 0, (0, 1), 0.5),
    (lambda x: 1*x**2 + 1, (0, 2), 14/3),
])
def test_area_under_curve(fun, xmin_xmax, integral):
    #import pdb
    #pdb.set_trace()
    integral_actual = area_under_curve(fun, *xmin_xmax)
    assert integral - 1e-4 < integral_actual < integral + 1e-4


@pytest.mark.parametrize('fun,y,xmin_xmax,x', [
    (lambda x: x, 2, (-1, 3), 2), 
    (lambda x: x**2 + 1, 5, (0, 4), 2)
])
def test_compute_inverse_function_value(fun, y, xmin_xmax, x):
    x_actual = compute_inverse_function_value(fun, y, *xmin_xmax)
    assert x - 1e-4 < x_actual < x + 1e-4


def test_inverse_area_under_curve():
    xmin = 0
    xmax = 4
    area = 2
    x_expected = 2
    f = lambda x: x
    area_fun = lambda x: area_under_curve(f, xmin, x)
    x_actual = inverse_area_under_curve(area_fun, area, xmin, xmax)
    assert x_expected - 1e-4 < x_actual < x_expected + 1e-4


def test_compute_covered_area():
    f = lambda x: 0*x + 1
    area_patch = 1
    npatches = 2
    w = 1
    total_area_covered, separator_locations = \
        compute_covered_area(f, area_patch, npatches, w, 
                             0, 10)

    assert total_area_covered == 3
    npt.assert_allclose(separator_locations, 
                        np.array([[1, 2]]))


def test_that_optimize_patch_area_raises_value_error():
    
    with pytest.raises(ValueError):
        optimize_patch_area('f', 0, 1, 2, 1)


@pytest.mark.parametrize('fun,xmin_xmax,npatches,w,area_patch', [
    (lambda x: 0*x + 1, (0, 4), 0, 10, 4), 
    (lambda x: 0*x + 1, (0, 4), 3, 0.5, 1), 
    (lambda x: 1*x + 0, (0, 4), 2, 1, 2.608058909292573), 
])
def test_optimize_patch_area(fun, xmin_xmax, npatches, w, area_patch):
    area_patch_actual = optimize_patch_area(fun, xmin_xmax[0], xmin_xmax[1], 
                                            npatches, w)
    assert np.abs(area_patch_actual - area_patch) < 1e-5


if __name__ == '__main__':
    pass