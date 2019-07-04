def quicksort(l:list) -> list:
    arr = l[::]
    if len(arr) <= 1:
        return arr
    l = [x for x in arr[1:] if x <= arr[0]]
    r = [x for x in arr[1:] if x > arr[0]]
    return quicksort(l) + arr[0:1] + quicksort(r)
