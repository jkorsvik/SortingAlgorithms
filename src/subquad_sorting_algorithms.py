"""
Algorithms for sorting with Theta(n*log(n)) as time complexity
"""


def mergesort(A):
    if len(A) > 1: 
        mid = int(len(A)/2) # Finding the mid of the array 
        left_array = A[:mid] # Dividing the array elements  
        right_array = A[mid:] # into 2 halves 
  
        mergesort(left_array) # Sorting the first half 
        mergesort(right_array) # Sorting the second half 
  

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




def swap(array, a, b):
    array[a], array[b] = array[b], array[a]
    return array

def partition(array, start, end):
    
    pivotindex = start
    pivotvalue = array[end]

    for left_index in range(start,end):
        if array[left_index] < pivotvalue:
            swap(array, left_index, pivotindex)
            pivotindex += 1
    swap(array, pivotindex, end)
    
    return array, pivotindex

def quick_sort(array, start, end):
    if start < end:
        array, index = partition(array, start, end)
        array = quick_sort(array, start, index-1)
        array = quick_sort(array, index+1, end)
        
    return array

def quicksort(array):
    array = quick_sort(array, 0, len(array)-1)






    