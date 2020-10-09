def insertionSort(array):
    # for i in range(1, len(arr)):
    #     key = arr[i]
    #     j = i-1
    #     while j >= 0 and key < arr[j]:
    #         arr[j+1] = arr[j]
    #         j -= 1
    #     arr[j+1] = key
    # return arr
    # for i in range(len(array)):
    #     # while i > 0 and array[i-1] > array[i]:
    #     #     array[i-1], array[i] = array[i], array[i-1]
    #     #     i -= 1
    for i in range(len(array)):
        while i > 0 and array[i-1] > array[i]:
            array[i-1], array[i] = arr[i], array[i-1]
    return array


arr = [5, 6, 11, 12, 13]
print(insertionSort(arr))
