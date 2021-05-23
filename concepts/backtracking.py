from typing import *


def combination(nums, k):
    res = []

    def backtrack(chosen, options, depth):
        if depth == 0:
            res.append(chosen[:])
        else:
            for i, opt in enumerate(options):
                chosen.append(opt)
                backtrack(chosen, options[i + 1:], depth - 1)
                chosen.pop()

    backtrack([], nums, k)
    return res


def permutation(nums, k):
    res = []

    def backtrack(chosen, options):
        if len(chosen) == k:
            res.append(chosen[:])
        else:
            for opt in options:
                if opt in chosen:
                    pass
                else:
                    chosen.append(opt)
                    backtrack(chosen, options)
                    chosen.pop()

    backtrack([], nums)
    return res


def subsets(nums):
    res = []

    def backtrack(chosen, options):
        res.append(chosen[:])
        for i, opt in enumerate(options):
            chosen.append(opt)
            backtrack(chosen, options[i + 1:])
            chosen.pop()

    backtrack([], nums)
    return res


if __name__ == '__main__':
    r = combination([1, 2, 3], 1)
    s = subsets([1, 2, 3])
    p = permutation([1, 2, 3], 3)
    print(r)
    print(s)
    print(p)
