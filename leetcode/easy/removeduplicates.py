def removeDuplicates(nums):
    if not nums or len(nums) == 0:
        return 0

    n = len(nums)
    idx = 0
    for i in range(1, n):
        if nums[i] == nums[i - 1]:
            pass
        else:
            idx += 1
            nums[idx] = nums[i]
    nums = nums[:idx+1]
    return nums

if __name__ == '__main__':

    nums = [1,1,2]

    print(removeDuplicates(nums))
