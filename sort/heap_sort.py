def heapify(A, last):
    for i in range(last, 0, - 1):
        parent = (i - 1) // 2
        if A[i] > A[parent]:
            A[i], A[parent] = A[parent], A[i]


def heap_sort(A):
    last = len(A) - 1
    heapify(A, last)

    while last:
        A[0], A[last] = A[last], A[0]
        last -= 1
        heapify(A, last)
