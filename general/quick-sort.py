def quicksort(array, low, high):
    if low < high:
        p = partition(array, low, high)
        quicksort(array, low, p - 1)
        quicksort(array, p + 1, high)

    return array

def partition(array, low, high):
    pivot = array[high]
    i = low # Place for swapping
    for j in xrange(low, high):
        if array[j] <= pivot:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
            i += 1

    temp = array[i]
    array[i] = array[high]
    array[high] = temp

    return i

array = [2,63,67,85,7]
print quicksort(array, 0, len(array)-1), [2,7,63,67,85] 