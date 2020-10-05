"""
Algorithms for sorting with Theta(n*log(n)) as time complexity
"""


def mergesort(A):
    if len(A) >1: 
        mid = len(A)//2 # Finding the mid of the array 
        L = A[:mid] # Dividing the array elements  
        R = A[mid:] # into 2 halves 
  
        mergesort(L) # Sorting the first half 
        mergesort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data from temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                A[k] = L[i] 
                i+= 1
            else: 
                A[k] = R[j] 
                j+= 1
            k+= 1
          
        # Checking if any element was left 
        while i < len(L): 
            A[k] = L[i] 
            i+= 1
            k+= 1
          
        while j < len(R): 
            A[k] = R[j] 
            j+= 1
            k+= 1
  

    """if len(A) < 2:
        return A
    


    result = []
    mid = int(len(A) / 2)
    print(mid)
    print(A)

    y = A[:mid]
    z = A[mid:]
    print("====================\n", y, z)
    y = mergesort(y)
    z = mergesort(z)
    

    
    i = 0
    j = 0

    while (len(y) > 0) and (len(z) > 0):
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1

    result += y[i:]
    result += z[j:]
    A = result"""




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
