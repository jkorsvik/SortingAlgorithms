"""
Algorithms for sorting with Theta(n*log(n)) as time complexity
"""
import numpy as np

def mergesort(A: np.array or list):
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
        # left_array is copartionining_indexed first since indexing(copy_index) goes from left to right
        while left_index < len(left_array): 

            A[copy_index] = left_array[left_index] 
            left_index += 1
            copy_index += 1
          
        while right_index < len(right_array): 

            A[copy_index] = right_array[right_index] 
            right_index += 1
            copy_index += 1


def mergesort_iterative(A: np.array or list):

    new_list = map(lambda x: [x], A)
    theLength = 1

    while theLength < len(A):
        temp_list = []

        pairs = zip(new_list[::2], new_list[1::2])

        for pair in pairs:
            temp_list.append( mergesort_iterative( pair[0], pair[1] ) )

        if len(pairs) * 2 < len(new_list):
            temp_list.append(new_list[-1])

        theLength *= 2
        new_list = temp_list

    return temp_list[0]




def swap(array, a, b):
    array[a], array[b] = array[b], array[a]
    return array

def partition(array, start, end):
    
    pivot_index = start
    pivot_value = array[end]

    for left_index in range(start,end):
        if array[left_index] < pivot_value:
            swap(array, left_index, pivot_index)
            pivot_index += 1
    swap(array, pivot_index, end)
    
    return array, pivot_index

def quick_sort(array, start, end):
    if start < end:
        array, index = partition(array, start, end)
        array = quick_sort(array, start, index-1)
        array = quick_sort(array, index+1, end)
        
    return array

def quicksort(array):
    array = quick_sort(array, 0, len(array)-1)





def iterative_quicksort(array):
    quickSort_iterative(array, 0, len(array) - 1)


def iter_partition(arr, low, high): 
    i = ( low - 1 ) 
    x = arr[high] 
  
    for j in range(low, high): 
        if   arr[j] <= x: 
  
            # increment index of smaller element 
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i] 
  
    arr[i + 1], arr[high] = arr[high], arr[i + 1] 
    return (i + 1) 
  

def quickSort_iterative(arr, low, high): 
  
    # Create an auxiliary stack 
    size = high - low + 1
    stack = [0] * (size) 
  
    # initialize top of stack 
    top = -1
  
    # push initial values of low and high to stack 
    top = top + 1
    stack[top] = low 
    top = top + 1
    stack[top] = high 
  
    # Keep popping from stack while is not empty 
    while top >= 0: 
  
        # Pop high and low 
        high = stack[top] 
        top = top - 1
        low = stack[top] 
        top = top - 1
  
        # Set pivot element at its correct position in 
        # sorted array 
        p = iter_partition(arr, low, high) 
  
        # If there are elements on left side of pivot, 
        # then push left side to stack 
        if p-1 > low: 
            top = top + 1
            stack[top] = low 
            top = top + 1
            stack[top] = p - 1
  
        # If there are elements on right side of pivot, 
        # then push right side to stack 
        if p + 1 < high: 
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = high 




    