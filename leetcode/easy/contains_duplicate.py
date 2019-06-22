# Given an array of integers, find if the array contains any duplicates.
#
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
#
# Example 1:
#
# Input: [1,2,3,1]
# Output: true
# Example 2:
#
# Input: [1,2,3,4]
# Output: false
# Example 3:
#
# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true


# using hashtable
def containsDuplicate(nums):
    if not nums or len(nums) == 0:
        return False
    seen = set()
    n = len(nums)
    for i in range(n):
        if nums[i] not in seen:
            seen.add(nums[i])
        else:
            return True
    return False


# using sort
def containsDuplicate_sort(nums):
    if not nums or len(nums) == 0:
        return False
    nums.sort()
    n = len(nums)
    for i in range(n-1):
        if nums[i+1] == nums[i]:
            return True
    return False




if __name__ == '__main__':
    nums = [1,1,1,3,3,4,3,2,4,2]
    print(containsDuplicate(nums))
    print(containsDuplicate_sort(nums))