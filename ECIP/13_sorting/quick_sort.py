'''
Code for quick sort
'''


def partition(a, low, high):
    pivot = a[high]
    i = low
    for j in range(low, high):
        if pivot >= a[j]:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[high] = a[high], a[i]
    return i


def _quicksort(a, low, high):
    if low < high:
        p = partition(a, low, high)
        _quicksort(a, low, p - 1)
        _quicksort(a, p + 1, high)
    return a


def quicksort(a):
    return _quicksort(a, 0, len(a) - 1)


if __name__ == '__main__':
    a = [7, 9, 1, 4, 2, 1, 3, 5, 6]
    print(a)
    print(quicksort(a))
