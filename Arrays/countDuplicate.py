def duplicateEle(arr):
    s = set()
    count = 0
    for i in range(len(arr)):
        if arr[i] in s:
            count += 1
        s.add(arr[i])
        print(count)
    return count


arr = [3, 1, 1, 2, 3, 1, 1, 1, 4]
print(duplicateEle(arr))
