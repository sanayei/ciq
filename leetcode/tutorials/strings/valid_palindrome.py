def isPalindrome(s):
    if not s:
        return True
    if len(s) == 0:
        return True
    left, right = 0, len(s) - 1
    s = s.lower()
    while left < right:

        while not s[left].isalnum() and left < right:
            left += 1
        while not s[right].isalnum() and left < right:
            right -= 1

        if s[left] != s[right]:
            return False
        right -= 1
        left += 1

    return True


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    s1 = ".,"
    print(isPalindrome(s1))