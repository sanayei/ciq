# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


def threeSum(nums):
    output = set()
    nums.sort()
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                a, b, c = nums[i], nums[j], nums[k]
                if a + b + c == 0:
                    output.add((a, b, c))

    return list(output)

def threeSum_on2(nums):
    res = []
    nums.sort()
    if len(nums) < 3: return res
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]: continue
        l, r = i + 1, len(nums) - 1
        while l < r :
            s = nums[i] + nums[l] + nums[r]
            if s == 0:
                res.append([nums[i] ,nums[l] ,nums[r]])
                l += 1; r -= 1
                while l < r and nums[l] == nums[l - 1]: l += 1
                while l < r and nums[r] == nums[r + 1]: r -= 1
            elif s < 0 :
                l += 1
            else:
                r -= 1
    return res


if __name__ == '__main__':
    nums1 = [6, -5, -6, -1, -2, 8, -1, 4, -10, -8, -10, -2, -4, -1, -8, -2, 8, 9, -5, -2, -8, -9, -3, -5]
    nums2 = [9, -15, 6, 6, 10, -2, 8, 8, 0, -6, -4, -2, 14, -6, -14, -2, 12, 5, -2, -8, 13, 13, -10, 4, -6, 8, 6, -15,
             -5, 11, -15, 11, 3, -2, -6, -10, 11, -12, 13, -12, -11, -5, 2, 10, -4, -5, -15, -7, 7, -2, 0, 5, -11, -3,
             -13, -10, -9, 0, -10, -7, -12, 12, -11, 7, -5, -1, 12, -8, -6, 3, -13, -10, 5, -4, -14, -14, 6, 8, -14, -9,
             -8, -7, 3, -4, 6, 5, 1, 12, -9, 6, -10, -6, -5, -14, -14, 5, -8, 6, 4, 1]
    nums = [-1, 0, 1, 2, -1, -4]

    # print(threeSum(nums2))
    print(threeSum_on2(nums2))

