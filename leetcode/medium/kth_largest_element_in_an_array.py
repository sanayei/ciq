

def quicksort(nums):
    def partition(left, right):
        pivot = nums[right]
        i = j = left
        while j < right:
            if nums[j] < pivot:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
            j += 1
        nums[i], nums[right] = nums[right], nums[i]
        return i

    def _sort(left, right):
        if left < right:
            i = partition(left, right)
            _sort(left, i-1)
            _sort(i+1, right)


    _sort(0, len(nums) - 1)
    return nums

def quickselect(nums, k):
    def partition(left, right):
        p = nums[right]
        i = j = left
        while j < right:
            if nums[i] < p:
                nums[i] , nums[j] = nums[i] , nums[j]
                i += 1
            j += 1
        nums[i], nums[right] = nums[right], nums[i]
        return i
    def select(left, right):
        if left == right:
            return nums[left]
        i = partition(left, right)
        if k == i:
            return nums[i]
        elif k < i:
            return select(left, i-1)
        else:
            return select(i+1, right)
    return select(0, len(nums)-1)




if __name__ == '__main__':
    nums = [8, 3, 1, 9, 1, 3, 2, 5, 6]
    print(quicksort(nums))
    print(quickselect(nums, 7))