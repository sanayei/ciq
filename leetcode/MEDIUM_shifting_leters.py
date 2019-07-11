def shiftingLetters(S, shifts):
    sum_ = 0
    ans = []
    for i in reversed(range(len(shifts))):
        sum_ += shifts[i]
        n = (ord(S[i]) - 97 + sum_) % 26
        ans.append(chr(n + 97))

        # print(i, n, chr(n+96), chr(ord(S[i]) + sum_))
    return ''.join(ans[::-1])


if __name__ == '__main__':
    S = 'z'
    shifts = [52]
    print(shiftingLetters(S, shifts))