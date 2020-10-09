def selectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr


arr = [8, 15, 7, 1, 2, 4]
print(selectionSort(arr))


# Time Complexities:

# Worst Case Complexity: O(n2)
# If we want to sort in ascending order and the array is in descending order then, the worst case occurs.
# Best Case Complexity: O(n2)
# It occurs when the array is already sorted
# Average Case Complexity: O(n2)
# It occurs when the elements of the array are in jumbled order (neither ascending nor descending).
