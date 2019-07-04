def merge_sort(l:list):
    arr = l[::]
    if len(arr) < 2:
        return arr
    mid = len(arr)//2;
    left = arr[:mid]
    right = arr[mid:]
    return merge(merge_sort(left), merge_sort(right))

def merge(l, r):
    arr = []
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            arr.append(l[i])
            i += 1
        else:
            arr.append(r[j])
            j += 1
    while i < len(l):
        arr.append(l[i])
        i += 1
    while j < len(r):
        arr.append(r[j])
        j += 1
    return arr
