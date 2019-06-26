#!/usr/bin/python3

"""
This module performs speed tests on 10 different sorting algorithms.
"""


if __name__ == "__main__":
    import random
    import timeit
    from bubble import *
    from insertion import *
    from selection import *
    from quicksort import *
    from mergesort import *
    from heapsort import *
    from countsort import *
    from radix import *
    from shaker import *
    from shell import *

    def randomlist(n):
        return [random.randint(0, 100000) for x in range(n)]

    ex = randomlist(500)
    print(ex)

    print("bubble")
    print(timeit.timeit("bubble_sort(ex)", globals=globals(), number=100))

    print("insertion")
    print(timeit.timeit("insertion(ex)", globals=globals(), number=100))

    print("selection")
    print(timeit.timeit("selection(ex)", globals=globals(), number=100))

    print("quicksort")
    print(timeit.timeit("quicksort(ex)", globals=globals(), number=100))

    print("mergesort")
    print(timeit.timeit("merge_sort(ex)", globals=globals(), number=100))

    print("heapsort")
    print(timeit.timeit("heap_sort(ex)", globals=globals(), number=100))

    print("countsort")
    print(timeit.timeit("countsort(ex)", globals=globals(), number=100))

    print("radix")
    print(timeit.timeit("radix_sort(ex)", globals=globals(), number=100))

    print("shaker")
    print(timeit.timeit("shaker(ex)", globals=globals(), number=100))

    print("shell")
    print(timeit.timeit("shell(ex)", globals=globals(), number=100))
