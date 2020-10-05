"""
Algorithms with Theta(n^2) time complexity, 
both of them have O(n) space complexity which gives them an advantage in memory dependents task with small arrays
"""


def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]

        while j > 0 and A[j-1] > key:
            # Swap
            A[j], A[j-1] = A[j-1], A[j]
            j -= 1



def bubble_sort(A):
    n = len(A)
    has_swapped = True
    num_rounds = 0

    while(has_swapped):
        has_swapped = False

        # shortens end of list by n - kth iteration - 1
        for i in range(n - num_rounds - 1):

            if A[i] > A[i+1]:
                # Swap
                A[i], A[i+1] = A[i+1], A[i]
                has_swapped = True
        num_rounds += 1