def _add(num1, num2):
    res = [0] * (len(num1) + len(num2))
    for i in range(len(num1) - 1, -1, -1):
        carry = 0
        for j in range(len(num2) - 1, -1, -1):
            tmp = int(num1[i]) + int(num2[j]) + carry
            # take care of the order of the next two lines
            carry = (res[i + j + 1] + tmp) // 2
            res[i + j + 1] = (res[i + j + 1] + tmp) % 2
            # or simply: carry, res[i+j+1] = divmod((res[i+j+1] + tmp), 10)
        res[i] += carry
    res = "".join(map(str, res))
    return res


if __name__ == '__main__':
    a = '11'
    b ='1'
    print(_add(a,b))