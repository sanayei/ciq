
def firstUniqChar(s):
    from collections import defaultdict
    if not s:
        return s
    chars = defaultdict(int)
    n = len(s)
    for c in s:
        chars[c] += 1
    print(chars)
    for i in range(n):
        if chars[s[i]] == 1:
            return i
    return -1



if __name__ == '__main__':
    s = "loveleetcode"

    print(firstUniqChar(s))