# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example 1:
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
#
# Input: "cbbd"
# Output: "bb"
#
def longestPalindrome(s: str) -> str:
    # base equations:
    # p(i,j) = p(i+1, j-1) and s[i] == s[j]  example: p(baab) = p(aa) abd b == b
    # p(i, i) = True
    # p(i, i+1) = s[i] == s[i+1]
    ans = ''
    max_len = 0
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = True
        max_ = 1
        ans = s[i]
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            ans = s[i:i + 2]
            max_ = 2
    for j in range(1, n):
        for i in range(0, j - 1):
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if max_ < j - i + 1:
                    ans = s[i:j + 1]
                    max_ = j - i + 1
    return ans

if __name__ == '__main__':
    s = 'babad'
    print(longestPalindrome(s))