import numpy as np

def numpy_sort(array, method="quicksort"):
    """
    Numpy sort can use a range of different algorithms, quicksort is default.
    """
    return np.sort(array, method=method)


def python_sort(array):
    """
    Python's sorted function uses the timsort algorithm.
    """
    return sorted(array)