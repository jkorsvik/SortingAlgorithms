from copy import copy
def mergesort_combined(A, threshold: int=10):
    if len(A) < threshold:
        return not_inplace_insertion_sort(A)

    result = []
    mid = int(len(A) / 2)

    y = mergesort_combined(A[:mid])
    z = mergesort_combined(A[mid:])

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




def not_inplace_insertion_sort(A):
    temp = copy(A) 
    for j in range(1, len(temp)):
        key = temp[j]

        while j > 0 and temp[j-1] > key:
            # Swap
            temp[j], temp[j-1] = temp[j-1], temp[j]
            j -= 1
    print(temp)
    return temp
