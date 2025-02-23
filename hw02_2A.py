# Challenge 2A


from math import sin, cos

def fixed_point_iteration(func, guess, iter=0):
    """
    Finds fixed point by applying guess to func repeatedly until almost no change in value
    
    >>> fixed_point_iteration(lambda x: sin(x) + x, 3.0)
    (3.141592653589793, 3)
    
    >>> fixed_point_iteration(lambda x: cos(x), 1.0)
    (0.7390851332151611, 86)
    """
    new_guess = func(guess)
    if abs(new_guess - guess) < 1e-15:
        return new_guess, iter
    return fixed_point_iteration(func, new_guess, iter + 1)

def newton_find_zero(func, deriv, guess, iter=0):
    """
    Uses Newton's method to find zero in the func
    
    >>> newton_find_zero(lambda x: sin(x) , lambda x: cos(x), 3.0)
    (3.141592653589793, 3)
    
    >>> newton_find_zero(lambda x: cos(x) - x , lambda x: -sin(x)-1, 1.0)
    (0.7390851332151606, 7)
    """
    if abs(func(guess)) < 1e-15:
        return guess, iter
    new_guess = guess - func(guess) / deriv(guess)

    return newton_find_zero(func, deriv, new_guess, iter + 1)

import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)