"""
Possible approach to the Adam's Patch problem.
Proof of concept; several small issues still need to be resolved (see comments) 
to obtain a proper *solver*.

Comments:
- While developming, it is often convenient to have an automatic test runner 
  like pytest-watch in place (if this is feasible).
- We are passing around a lot of the same arguments, an OOP solution might be
  more suitable.
- Input could be a csv file with x, ylower, yupper values (see below).
- Plotting could be wrapped in a separate function.
- Not that basic functionality is established, refactorings and 
  improvements can take place now.
- Should a refactoring touch an area not yet under test, a test needs to be
  written first.
- Documentation obviously missing, needs to be added (at the latest) when we 
  know we like it that way.
- We could turn some of the parameters into tuples to explicitely express 
  that they belong together.
- Function parameter order inconsistent, needs to be fixed.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq


def area_under_curve(f, xmin, xmax):
    """
    >>> area_under_curve(lambda x: x, 1, 2)
    1.5
    """
    integral, _ = quad(f, xmin, xmax)
    return integral


def compute_inverse_function_value(fun, y, xmin, xmax):
    """
    >>> compute_inverse_function_value(lambda x: x, 2, 0, 3)
    2.0
    >>> compute_inverse_function_value(lambda x: x**2 + x + 1, 3, 0, 4)
    1.0
    """    
    def target(x):
        return fun(x) - y
    
    x_root, _ = brentq(target, xmin, xmax, full_output=True)
    return x_root


def inverse_area_under_curve(area_fun, area, xmin, xmax):
    """
    >>> xmin = 0
    >>> xmax = 3
    >>> area_fun = lambda x: area_under_curve(lambda x: x, xmin, x)
    >>> inverse_area_under_curve(area_fun, 4.5, xmin, xmax)
    3.0
    """
    x_area = compute_inverse_function_value(area_fun, area, xmin, xmax)
    
    return x_area 


def compute_covered_area(f, area_patch, npatches, w, xmin, xmax):
    
    separator_locations = []
    total_area_covered = area_patch
    for patch in range(npatches - 1):
        x_end_of_patch = \
            inverse_area_under_curve(lambda x: area_under_curve(f, xmin, x), 
                                     total_area_covered, 
                                     xmin, xmax)
        x_end_of_separator = x_end_of_patch + w
        area_separator = area_under_curve(f, 
                                          x_end_of_patch, 
                                          x_end_of_separator)
        total_area_covered += area_separator +  area_patch
        separator_locations.append((x_end_of_patch, x_end_of_separator))
        
    return total_area_covered, np.array(separator_locations)


def optimize_patch_area(f, xmin, xmax, npatches, w):
        
    if w * (npatches - 1) >= xmax - xmin:
        raise ValueError('Unsatisfieable constraints')

    total_available_area = area_under_curve(f, xmin, xmax)
    
    if npatches == 0:
        return total_available_area
    
    def target(area_patch):
        area_patched, _ = compute_covered_area(f, area_patch, npatches, w, 
                                               xmin, xmax)
        return total_available_area - area_patched
    
    f_max = f(np.linspace(xmin, xmax, 100)).max()
    area_patch_min = np.max([(total_available_area - (w * f_max) * (npatches - 1)) / npatches, 0])
    area_patch_max = total_available_area / npatches
    area_patch, _ = brentq(target, area_patch_min * 0.9, area_patch_max * 1.1,
                           full_output=True)
    
    return area_patch


if __name__ == '__main__':
    #%% define input
    xmin = 0
    xmax = 3
    npatches = 3
    w = 0.3   
    
    flower = lambda x: 0*x
    fupper = lambda x: x**2 + 1  
    area_function = lambda x: fupper(x) - flower(x)

    #%% solve problem
    area_patch = optimize_patch_area(area_function, xmin, xmax, npatches, w)
    area_patch, separator_locations = \
        compute_covered_area(area_function, area_patch, npatches, w, 
                             xmin, xmax)
    
    #%% plot
    x = np.linspace(xmin, xmax, 100)
    ylower = flower(x)
    yupper = fupper(x)
    
    plt.show()
    fig, ax = plt.subplots()
    ax.plot(x, ylower, color='grey')
    ax.plot(x, yupper, color='grey')
    ax.fill_between(x, ylower, yupper, 
                    facecolor='green', alpha=0.5, 
                    label='patches')
    
    #%% add flowers
    n_flowers = 80
    flowers_x = xmin + (xmax - xmin) * np.random.rand(n_flowers)
    flowers_y = [flower(x) + (fupper(x) - flower(x)) * np.random.rand() for x in flowers_x]
    flowers = np.c_[flowers_x, flowers_y]
    flowers
    
    ax.scatter(*flowers.T, 
               c=np.random.choice(['r', 'b', 'y', 'c', 'm', 'y'], size=n_flowers),
               s=np.random.rand(n_flowers) * 30, 
               marker='*', 
               label='flowers')
    
    label ='separators'
    for separator_xmin, separator_xmax in separator_locations:
        ax.fill_between(x, ylower, yupper, 
                        where=(x >= separator_xmin) & (x<separator_xmax), 
                        facecolor='grey', 
                        label=label)
        label = None
    
    ax.legend()
