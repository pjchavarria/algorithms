def mergeSort(l):
    # Base case. A list of zero or one elements is sorted, by definition
    if len(l) <= 1:
        return l

    # Recursive case. First, *divide* the list into equal-sized sublists.
    middle = len(l) / 2
    left, right = l[:middle], l[middle:]

    # Recursively sort both sublists
    left = mergeSort(left)
    right = mergeSort(right)

    # Then merge the now-sorted sublists.
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[i]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result

print mergeSort([2,63,67,7,85]), [2,7,63,67,85] 