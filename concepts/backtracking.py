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


def permutation2(lst):
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
    return output


def allpermutation(lst):
    s = set()

    def dfs(path, t):
        if path:
            s.add(path)
        for i in range(len(t)):
            dfs(path+t[i], t[:i]+t[i+1:])

    dfs('', lst)
    return s

def permutation1(lst):
    s = set()
    n = len(lst)
    def dfs(path, t):
        if len(path) == n:
            s.add(path)
        for i in range(len(t)):
            dfs(path+t[i], t[:i]+t[i+1:])
    dfs('', lst)
    return s



if __name__ == '__main__':
    nums = '123'
    print(permutation2(nums))