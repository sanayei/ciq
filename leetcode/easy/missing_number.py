# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
#
# Example 1:
#
# Input: [3,0,1]
# Output: 2
# Example 2:
#
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
#



def missingNumber(nums):
    #         # O(n) space complexity
    #         temp = [False] * (len(nums)+1)

    #         for i in range(len(nums)):
    #             temp[nums[i]] = True
    #         print(temp)

    #         for i in range(len(temp)):
    #             if temp[i] == False:
    #                 return i

    # O(1) space complexity

    n = len(nums)
    return int( n *( n +1 ) /2) - sum(nums)


if __name__ == '__main__':
    nums = [3,0,1]
    print(missingNumber(nums))

