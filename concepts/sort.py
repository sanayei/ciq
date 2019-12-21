import random


def quicksort(nums):
    if len(nums) <= 1:
        return nums
    pivot = random.choice(nums)
    ls = [n for n in nums if n < pivot]
    eq = [n for n in nums if n == pivot]
    rs = [n for n in nums if n > pivot]

    return quicksort(ls) + eq + quicksort(rs)


def quicksort2(nums, left=None, right=None):
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

    if len(nums) <= 1:
        return nums
    if left is None:
        left = 0
    if right is None:
        right = len(nums) - 1

    if left < right:
        p = _partition(left, right)
        quicksort2(nums, left, p - 1)
        quicksort2(nums, p + 1, right)

    return nums


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

    if len(nums)<= 1:
        return nums
    p = len(nums) //2
    left = mergesort(nums[:p])
    right = mergesort(nums[p:])
    return _merge(left, right)

nums = [4, 5, 1, 8, 3, 1, 7, 10, 9]

if __name__ == '__main__':
    print(nums)
    print(quicksort(nums))
    print(quicksort2(nums))
    print(mergesort(nums))