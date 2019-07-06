def topKFrequent(nums, k) :
    from heapq import _heapify_max, _heappop_max
    from collections import Counter
    c = Counter(nums)
    lst = [[f, n] for n, f in c.items()]
    _heapify_max(lst)
    i = 0
    res = []
    while lst and i < k:
        f, n = _heappop_max(lst)
        i += 1
        print(f, n)
        res.append(n)
    return res



if __name__ == '__main__':
    nums = [1,1,1,2,2,3, 9, 9,9, 9, 9]
    print(topKFrequent(nums, 2))