# CS2023 - Lab 3 Required Questions 
# All functions should be written using recursion.
# RQ1
def doubletime(i,n):
    """Returns the result of repeatedly doubling the number i a total of n times
    >>> doubletime(3, 1)
    6
    >>> doubletime(2, 0)
    2
    >>> doubletime(2, 9)
    1024
    """
    "*** YOUR CODE HERE ***"
    return i * (2**n)



# RQ2
def skip2_add(n):
    """ Takes a number x and returns x + x-3 + x-6 + x-9 + ... + 0.

    >>> skip2_add(5)  # 5 + 2  + 0
    7
    >>> skip2_add(10) # 10 + 7 + 4 + 1 + 0
    22
    """
    "*** YOUR CODE HERE ***"
    total = 0
    while n > 0:
        total += n
        n -= 3
    return total

# RQ3
def a(n):
    """Return the number in the sequence defined by a(1) = 1;
    a(n) = (3/2)*a(n-1) if a(n-1) is even; a(n) = (3/2)*(a(n-1)+1) if a(n-1) is odd.
    (see, http://oeis.org/A070885)

    >>> a(1)
    1
    >>> a(2) 
    3
    >>> a(3)
    6
    >>> a(10)
    123
    """
    "*** YOUR CODE HERE ***"

    seq = [1]
    for i in range(n-1):
        
        if seq[i] % 2 == 0:
            seq.append(int(1.5*seq[i]))
        else:
            seq.append(int(1.5 * (seq[i] + 1)))
    return seq[n-1]
    
#RQ4
def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.
    >>> paths(2, 2)
    2
    >>> paths(3, 3)
    6
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"

    def fact(x):
        total = 1
        for i in range(1,x+1):
            total *= i
        return total
    total = m+n-2
    horizontal = m - 1
    vertical = n - 1
    output = int(fact(total) / (fact(horizontal) * fact(vertical)))

    if m == 1 or n == 1:
        return 1
    else:
        return output


import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)