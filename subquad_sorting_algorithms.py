"""
Algorithms for sorting with Theta(n*log(n)) as time complexity
"""


def mergesort(A):
    if len(A) < 2:
        return A

    result = []
    mid = int(len(A) / 2)

    y = mergesort(A[:mid])
    z = mergesort(A[mid:])

    i = 0
    j = 0
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1
    result += y[i:]
    result += z[j:]




def swap(array, a, b):
    array[a], array[b] = array[b], array[a]
    return array

def partition(array, start, end):
    
    pivotindex = start
    pivotvalue = array[end]

    for i in range(start,end):
        if array[i] < pivotvalue:
            swap(array, i, pivotindex)
            pivotindex += 1
    swap(array, pivotindex, end)
    
    return array, pivotindex

def quicksort(array, start, end):
    if start < end:
        array, index = partition(array, start, end)
        array = quicksort(array, start, index-1)
        array = quicksort(array, index+1, end)
        
    return array
