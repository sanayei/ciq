# Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.
#
# Example:
#
# Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
# Output: ["2", "4->49", "51->74", "76->99"]


def findMissingRanges( nums, lower, upper):
    def gen_range(l, r):
        if l < r:
            return str(l) + '->' + str(r)
        elif l == r:
            return str(l)

    output = []
    n = len(nums)

    if len(nums) == 0:
        output.append(gen_range(lower, upper))
        return output



    if lower < nums[0]:
        nums.insert(0, lower-1)

    for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] > 1:
            output.append(gen_range(nums[i - 1] + 1, nums[i] - 1))
    if upper - nums[-1] >= 1:
        output.append(gen_range(nums[-1] + 1, upper))
    return output


if __name__ == '__main__':
    nums, lower, upper = [], 1, 1
    print(findMissingRanges(nums, lower, upper))
    nums, lower, upper = [-1], -2, -1
    print(findMissingRanges(nums, lower, upper))
    nums, lower, upper = [-1], -1, 0
    print(findMissingRanges(nums, lower, upper))
