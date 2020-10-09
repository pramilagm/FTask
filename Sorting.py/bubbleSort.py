def bubbleSort(arr):
    for i in range(0, len(arr)):
        swapped = False
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            break
    return arr


arr = [5, 1, 6, 12, 4, 8]
print(bubbleSort(arr))
