# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
# Example:
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.




def maxSubArray(nums):
    if not nums or len(nums) == 0:
        return 0
    n = len(nums)
    o = [0] * n
    o[0] = nums[0]
    maxsofar = o[0]
    for j in range(1, n):
        o[j] = max(o[j - 1] + nums[j], 0)
        maxsofar = max(maxsofar, o[j])
    return maxsofar


if __name__ == '__main__':
    nums = [1]
    print maxSubArray(nums)