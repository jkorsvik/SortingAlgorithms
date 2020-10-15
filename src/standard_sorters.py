import numpy as np

def numpy_sort(array, method="quicksort"):
    """
    Numpy sort can use a range of different algorithms, quicksort is default.
    
kind            speed    worst case     work space      stable
‘quicksort’     1           O(n^2)          0              no

‘heapsort’      3        O(n*log(n))        0              no

‘mergesort’     2        O(n*log(n))       ~n/2            yes

‘timsort’       2        O(n*log(n))       ~n/2            yes


    The above table is taken from: https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort

    """
    return np.asarray(array).sort(kind=method)


def python_sort(array):
    """
    Python's sorted function uses the timsort algorithm.
    """
    return list(array).sort()