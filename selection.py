def selection(l: list):
    arr = l[::]
    for i in range(len(arr)):
        m = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[m]:
                m = j
        if i != m:
            arr[i], arr[m] = arr[m], arr[i]
    return arr
