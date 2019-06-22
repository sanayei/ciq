# Given two arrays, write a function to compute their intersection.
#
# Example 1:
#
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:
#
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Note:
#
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.
# Follow up:
#
# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?


def intersect(nums1, nums2):
    from collections import defaultdict

    if not nums1 or not nums2 or len(nums1) == 0 or len(nums2) == 0:
        return []
    d = defaultdict(int)
    ans = []
    n1, n2 = len(nums1), len(nums2)
    for i in range(n1):
        d[nums1[i]] += 1

    for i in range(n2):
        if d[nums2[i]] >= 1:
            ans.append(nums2[i])
            d[nums2[i]] -= 1
    return ans

if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(intersect(nums1, nums2))