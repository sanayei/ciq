import random


def quicksort(nums):
    if len(nums) <= 1:
        return nums
    pivot = random.choice(nums)
    ls = [n for n in nums if n < pivot]
    eq = [n for n in nums if n == pivot]
    rs = [n for n in nums if n > pivot]

    return quicksort(ls) + eq + quicksort(rs)


def quicksort2(nums):
    def _partition(l, r):
        pivot = random.choice(nums[l:r])
        i = j = l
        while j < r:
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i

    def _sort(nums, left, right):
        if left < right:
            p = _partition(left, right)
            _sort(nums, left, p - 1)
            _sort(nums, p + 1, right)

    if len(nums) <= 1:
        return nums
    _sort(nums, 0, len(nums)-1)
    return nums


def quickselect(nums, k):
    def _partition(left, right):
        p = nums[right]
        i = j = left
        while j < right:
            if nums[j] < p:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        nums[i], nums[right] = nums[right], nums[i]
        return i

    def _select(left, right, k):
        if left == right:
            return left
        i = _partition(left, right)
        if i == k:
            return i
        elif i > k:
            return _select(left, i - 1, k)
        else:
            return _select(i + 1, right, k)
    idx = _select(0, len(nums) - 1, k)
    return nums[:idx], nums[idx], nums[idx+1:]


def mergesort(nums):
    def _merge(A, B):
        ret = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                ret.append(A[i])
                i += 1
            else:
                ret.append(B[j])
                j += 1
        ret.extend(A[i:])
        ret.extend(B[j:])

        return ret

    if len(nums) <= 1:
        return nums
    p = len(nums) // 2
    left = mergesort(nums[:p])
    right = mergesort(nums[p:])
    return _merge(left, right)


if __name__ == '__main__':
    nums = [4, 5, 1, 8, 3, 1, 7, 10, 9]
    print(nums)
    print(quicksort(nums))
    print(quicksort2(nums))
    print(mergesort(nums))

    print(quickselect(nums, k=3))
