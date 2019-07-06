# Given a string, find the length of the longest substring without repeating characters.
#
# Example 1:
#
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.




def lengthOfLongestSubstring(s: str) -> int:
    d = {}
    n = len(s)
    if n < 2:
        return n
    max_, i, j= 0, 0, 0
    while j < n:
        if s[j] not in d:
            d.update({s[j]: j})
            max_ = max(max_, j-i+1)
        else:
            i = d[s[j]] + 1
            dellist = []
            for k, v in d.items():
                if v < i:
                    dellist.append(k)
            for k in dellist:
                del d[k]
            d.update({s[j]: j})
        j += 1
    return max_


if __name__ == '__main__':

    s1 = 'bbbbb'
    s2 = 'abcabcbb'
    s3 = "pwwkew"
    s4 = ' '
    s5 = 'au'
    s6 = 'dvdf'
    s7 = "tmmzuxt"
    print(lengthOfLongestSubstring(s7))