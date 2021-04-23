def merge(left, right):
    i = j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    for k in range(i, len(left)):
        result.append(left[k])
    for k in range(j, len(right)):
        result.append(right[k])
    return result


def merge_sort(A):
    if len(A) <= 1:
        return
    middle = len(A) // 2
    left = A[:middle]
    right = A[middle:]
    merge_sort(left)
    merge_sort(right)
    temp = merge(left, right)
    A[:] = temp
