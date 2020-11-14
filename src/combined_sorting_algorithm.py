from copy import copy
import numpy as np
import os

from numba import jit

path_suffix = os.path.normpath(os.getcwd()).split("\\")[-1]

if path_suffix == "notebooks":
    from src.quadratic_sorting_algorithms import insertion_sort
else:
    from quadratic_sorting_algorithms import insertion_sort


@jit()
def mergesort_combined(A: list, 
                    threshold: int=142, 
                    comb_algo: str="insertion"
    ):
    """
    Mergesort combined with insertion sort

    args:
        threshold [int] : Number of elements before using insertion instead of mergesort,
                            defaults to 11.
        comb_algo [str] : Which algorithm to sort with. Defaults to insertion sort, currently if 
                            any other str is provideded, python inplace sort on list is implementeted.
    """

    if len(A) > threshold: 
        mid = int(len(A)/2) # Finding the mid of the array 
        left_array = A[:mid] # Dividing the array elements  
        right_array = A[mid:] # into 2 halves 
  
        mergesort_combined(
            left_array,
            threshold=threshold, 
            comb_algo=comb_algo
        ) 
        # Sorting the first half 

        mergesort_combined(
            right_array,
            threshold=threshold,
            comb_algo=comb_algo
        )
        # Sorting the second half 
  

        # Merge process starts on lowest level first and completes finally at 
        # left_array[0:mid] and right_array[mid:len(A)], where mid is len(a)//2

        left_index = 0
        right_index = 0
        copy_index = 0
          
        
        while left_index < len(left_array) and right_index < len(right_array): 

            if left_array[left_index] < right_array[right_index]: 
                A[copy_index] = left_array[left_index] 
                left_index += 1

            else: 
                A[copy_index] = right_array[right_index] 
                right_index += 1

            copy_index += 1
          
        # Checking if elements are remaining in Left or Right
        # left_array is copied first since indexing(copy_index) goes from left to right
        while left_index < len(left_array): 

            A[copy_index] = left_array[left_index] 
            left_index += 1
            copy_index += 1
          
        while right_index < len(right_array): 

            A[copy_index] = right_array[right_index] 
            right_index += 1
            copy_index += 1


    else:

        if comb_algo == "insertion":
            insertion_sort(A)
        else:
            A = np.sort(A)




