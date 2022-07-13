arr = [3, 5, 0, 1, 4, 2]


def mergeSort(l):
    if len(l) == 1:
        return l

    left = l[:len(l)//2]
    right = l[len(l)//2:]

    left = mergeSort(left)
    right = mergeSort(right)

    i, j = 0, 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    if i < len(left):
        res += left[i:]
    if j < len(right):
        res += right[j:]

    return res


print(mergeSort(arr))
