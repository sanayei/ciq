# find all combinations of size k of a set
def combinations(lst, k):
    output = []
    n = len(lst)
    def backtrack(start_idx=0, curr=[]):
        if len(curr) == k:
            output.append(curr.copy())
        for i in range(start_idx, n):
            curr.append(lst[i])
            backtrack(i+1, curr)
            curr.pop()

    backtrack()
    return output


# find all subsets of a given set
def subsets(lst):
    n = len(lst)
    output = []
    for i in range(n+1):
        output.extend(combinations(lst,i))
    return output

if __name__ == '__main__':
    a = [1, 5, 10, 25]

    print(combinations(a, 2))

    print(subsets(a))