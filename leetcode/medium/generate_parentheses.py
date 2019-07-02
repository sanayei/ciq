# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]


def generateParenthesis(n):
    output = []

    def backtrack(left=0, right=0, cur=''):
        if len(cur) == 2 * n:
            output.append(cur)
        if left < n:
            backtrack(left + 1, right, cur + '(')
        if right < left:
            backtrack(left, right + 1, cur + ')')

    backtrack()
    return output

if __name__ == '__main__':
    n = 5
    print(generateParenthesis(n))