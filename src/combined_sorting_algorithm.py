from copy import copy
from quadratic_sorting_algorithms import insertion_sort


def mergesort_combined(A, 
                    threshold: int=10, 
                    comb_algo: str="insertion"
    ):

    if len(A) > threshold: 
        mid = len(A)//2 # Finding the mid of the array 
        L = A[:mid] # Dividing the array elements  
        R = A[mid:] # into 2 halves 
  
        mergesort_combined(L) # Sorting the first half 
        mergesort_combined(R) # Sorting the second half 
  
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
    else:
        if comb_algo == "insertion":
            insertion_sort(A)
        else:
            A.sort()




