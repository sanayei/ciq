# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
# Example 1:
#
# Input: [2,2,1]
# Output: 1
# Example 2:
#
# Input: [4,1,2,1,2]
# Output: 4


def singleNumber(nums):
    from collections import defaultdict
    counts = defaultdict(int)
    n = len(nums)
    for i in range(n):
        counts[nums[i]] += 1
    for i in range(n):
        if counts[nums[i]] == 1:
            return nums[i]


def singleNumber_no_extra_mem(nums):
    return 2* sum(set(nums)) - sum(nums)

if __name__ == '__main__':
    nums = [4,1,2,1,2]
    print(singleNumber(nums))
    print(singleNumber_no_extra_mem(nums))