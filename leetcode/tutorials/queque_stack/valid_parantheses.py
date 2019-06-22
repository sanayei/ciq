def isValid( s: str) -> bool:
    if s is None or len(s) == 0:
        return True
    chars = {'(': ')', '[': ']', '{': '}'}
    stack = []
    for c in s:
        if c in chars.keys():
            stack.append(c)
        elif c in chars.values():
            if len(stack) == 0:
                return False
            p = stack.pop()
            if chars[p] != c:
                return False
        else:
            return False
    return len(stack) == 0


if __name__ == '__main__':
    s = '()'
    a = isValid(s)
    print(a)