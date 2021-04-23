def bubble_sort(A):
    sorted = 0
    while sorted < len(A):
        for j in range(1, len(A) - sorted):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]
        sorted += 1
