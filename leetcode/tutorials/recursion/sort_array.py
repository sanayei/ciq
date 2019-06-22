def merge(left, right):
    li, ri, ret = 0, 0, []
    while li < len(left) and ri < len(right):
        if left[li] < right[ri]:
            ret.append(left[li])
            li += 1
        else:
            ret.append(right[ri])
            ri += 1

    ret.extend(left[li:])
    ret.extend(right[ri:])
    return ret

def sortArray(nums):
    if len(nums) <= 1:
        return nums
    p = len(nums) // 2
    left = sortArray(nums[:p])
    right = sortArray(nums[p:])
    print(left, right)
    return merge(left, right)

if __name__ == '__main__':
    a = [-1,2,-8,-10]
    print(sortArray(a))