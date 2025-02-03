
def egypt(n,d):
    """
    >>> egypt(3,4)
    '1/2 + 1/4'
    >>> egypt(11,12)
    '1/2 + 1/3 + 1/12'
    >>> egypt(123,124)
    '1/2 + 1/3 + 1/7 + 1/64 + 1/8333 + 1/347186112'
    >>> egypt(103,104)
    '1/2 + 1/3 + 1/7 + 1/71 + 1/9122 + 1/141449381 + 1/100039636784966424'
    """

    # ceiling function (closest smallest int)
    unit = (n+d-1) // n
    # get next numerator and denominator ( p/q - 1/n )
    next_n = n * unit - d
    next_d = d * unit 

    # final item in sequence
    if next_n == 0:
        return f"1/{unit}"
    return f"1/{unit} + " + egypt(next_n,next_d)

import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)
