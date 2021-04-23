def quick_sort(A):
    if len(A) <= 1:
        return
    left, right, middle = [], [], []
    pivot = A[0]
    for i in range(len(A)):
        if A[i] < pivot:
            left.append(A[i])
        elif A[i] > pivot:
            right.append(A[i])
        else:
            middle.append(A[i])
    quick_sort(left)
    quick_sort(right)
    A[:] = left + middle + right
