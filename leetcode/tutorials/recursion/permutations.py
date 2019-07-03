def permutation(lst):
    output = []
    n = len(lst)
    def backtrack(sidx=0):
        if sidx == n:
            output.append(lst.copy())
        for i in range(sidx, n):
            lst[i], lst[sidx] = lst[sidx], lst[i]
            backtrack(sidx + 1)
            lst[i], lst[sidx] = lst[sidx], lst[i]
    backtrack()


if __name__ == '__main__':

    a = [1, 2, 3, 4, 5, 6]
    print(permutation(a))