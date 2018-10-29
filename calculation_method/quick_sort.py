def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        lower = [i for i in array[1:] if i <= pivot]
        higher = [i for i in array[1:] if i > pivot]
        return quicksort(lower) + [pivot] + quicksort(higher)


print quicksort([10, 5, 2, 3])
