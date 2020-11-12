import numpy as np
from numba import jit


@jit() 
def radixsort(A: list) -> None:
    """
    Radix sort

    A must be an A of integers
    """

    max_element = max(A)

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(A, place)
        place *= 10

# Using counting sort to sort the elements in the basis of significant places
@jit() 
def countingSort(A, place):
    size = len(A)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = A[i] // place
        count[index % 10] += 1

    # Calculate cummulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = A[i] // place
        output[count[index % 10] - 1] = A[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        A[i] = output[i]





