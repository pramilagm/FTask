def firstElement(arr, k):
    count_map = {}
    n = len(arr)
    for i in range(0, n):
        if(arr[i] in count_map.keys()):
            count_map[arr[i]] += 1
        else:
            count_map[arr[i]] = 1

    print(count_map)

    for i in range(0, n):

        # if count of element == k ,
        # then it is the required
        # first element
        print(count_map[arr[i]])
        if (count_map[arr[i]] == k):
            return arr[i]

    # no element occurs k times
    return -1


arr = [1, 7, 4, 3, 4, 8, 7]
k = 2
print(firstElement(arr, k))
