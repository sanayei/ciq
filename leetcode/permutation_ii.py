def permuteUnique(nums):
    output = []
    n = len(nums)
    nums.sort()

    def backtrack(idx=0):
        # if idx == n:
        for i in range(idx, n):
            if i > 0 and nums[i] == nums[idx]:
                continue
            nums[i], nums[idx] = nums[idx], nums[i]
            output.append(nums.copy())
            backtrack(idx+1)
            nums[i], nums[idx] = nums[idx], nums[i]

    backtrack()
    return output


if __name__ == '__main__':
    nums = [1,1,2]

    print(permuteUnique(nums))