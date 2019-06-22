def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    phone = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}

    def backtrack(idx=0, cur=[]):
        # if there is no more digits to check
        if len(cur) == n:
            output.append(cur.copy())
        for i in range(idx, n):
            for letter in phone[digits[i]]:
                cur.append(letter)
                backtrack(i + 1, cur)
                cur.pop()

    output = []
    n = len(digits)
    if digits:
        backtrack()
    return [''.join(el) for el in  output]

if __name__ == '__main__':
    print(letterCombinations('238'))