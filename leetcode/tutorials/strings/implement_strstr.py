# mplement strStr().
#
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
# Example 1:
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Clarification:
#
# What should we return when needle is an empty string? This is a great question to ask during an interview.
#
# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().


def strStr(haystack, needle):
    if haystack is None or  needle is None:
        return -1

    if len(haystack) == 0 and len(needle) == 0:
        return 0
    elif len(haystack) == 0:
        return -1
    else:
        return 0


    h, n = len(haystack), len(needle)
    for i in range(h - n + 1):
        print(i, haystack[i:i + n], needle)
        if haystack[i:i + n] == needle:
            return i
    return -1

if __name__ == '__main__':
    haystack = ""
    needle = ""
    print strStr(haystack, needle)