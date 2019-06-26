def countsort(l:list) -> list:
    arr = l[::]
    k = 0
    l = (max(arr) + 1) * [0]
    for j in arr:
        l[j] += 1
    for i in range(max(arr) + 1):
        if i != 0:
            l[i] += l[i - 1]
        while l[i] != k:
            arr[k] = i;
            k += 1
    return arr
