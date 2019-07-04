def bubble_sort(l: list):
    arr = l[::]
    is_sorted = True
    end = len(arr)
    while is_sorted:
        is_sorted = False
        for i in range(1, end):
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                is_sorted = True
        end -= 1
    return arr
