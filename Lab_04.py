##Lab04 Required Questions ##

#########
# Lists #
#########

# RQ1
def cascade(lst):
    """Returns the cascade of the given list running forward and back.

    >>> cascade([1, 2, 3, 4])
    [1, 2, 3, 4, 4, 3, 2, 1]
    """
    "*** YOUR CODE HERE ***"

    return lst[:] + lst[::-1]

# RQ2
def maptwice(fn, seq):
    """Applies fn twice onto each element in seq and returns the resulting list.

    >>> maptwice(lambda x: x*x, [1, 2, 3])
    [1, 16, 81]
    """
    "*** YOUR CODE HERE ***"

    return list(map(lambda x: fn(fn(x)), seq))
#RQ3
def filterout(pred, seq):
    """Keeps elements in seq only if they do not satisfy pred.

    >>> filterout(lambda x: x % 2 == 0, [1, 2, 3, 4])
    [1, 3]
    """
    "*** YOUR CODE HERE ***"

    return [x for x in seq if not pred(x)]

#RQ4
def comp(n, pred):
    """ Uses a one line list comprehension to return list of the first n integers (0...n-1) which satisfy the predicate pred.
    >>> comp(7, lambda x: x%2 ==0)
    [0, 2, 4, 6]
    """
    "*** YOUR CODE HERE ***"

    return [x for x in range(n) if pred(x)]

#RQ5
def flatten(lst):
    """ Takes a nested list and "flattens" it.
    
    >>> flatten([1, 2, 3]) 
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] 
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    >>> lst = [1, [[2], 3], 4, [5, 6]]
    >>> flatten(lst)
    [1, 2, 3, 4, 5, 6]
    """
    "*** YOUR CODE HERE ***"



    if not lst:
        return [] # To stop recursion
    elif type(lst[0]) == list:
        return flatten(lst[0]) + flatten(lst[1:]) # add flattened first item of list to flattened remaining items
    else:
        return [lst[0]] + flatten(lst[1:]) # add first item of list to final output and flattened remaining items
            

    


import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)
