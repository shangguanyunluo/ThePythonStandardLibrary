def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        middle = (low + high) / 2
        if item == list[middle]:
            return middle
        elif item > list[middle]:
            low = middle + 1
        else:
            high = middle - 1
    return None


list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print binary_search(list, 8)
print binary_search(list, 10)

