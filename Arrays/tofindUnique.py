def countUnique(list):
    s = set()
    count = 0
    for i in range(len(list)):
        if list[i] not in s:
            s.add(list[i])
            count += 1
    return count


list = [1, 2, 1, 3, 3]
print(countUnique(list))
# 0(n) time complexity
