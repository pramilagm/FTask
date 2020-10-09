def sortMerg(arr):
    if len(arr) == 1:
        return arr
    midIdx = len(arr)//2
    left_half = arr[:midIdx]
    right_half = arr[midIdx:]
    print(left_half)
    print(right_half)
    return mergeSortArr(sortMerg(left_half), sortMerg(right_half))


def mergeSortArr(left_half, right_half):
    sorted = [0] * (len(left_half) + len(right_half))

    i = j = k = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            sorted[k] = left_half[i]
            i += 1
        else:
            sorted[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        sorted[k] = left_half[i]
        i += 1
        k += 1
    while j < len(right_half):
        sorted[k] = right_half[j]
        j += 1
        k += 1
    return sorted


arr = [15, 6, 8, 4, 9]
print(sortMerg(arr))
