def myPow_iter( x: float, n: int) -> float:
    if n < 0:
        x = 1 / x
        n = -1 * n
    ans = 1
    while n > 0:
        if n % 2 == 1:
            ans = ans * x
        x = x * x
        n = n // 2
    return ans

def myPow_recur( x: float, n: int) -> float:
    if n == 0:
        return 1
    half = myPow_recur(x, n//2)
    if n % 2 == 0:
        ans = half * half
    else:
        ans = half * half * x
    return ans


if __name__ == '__main__':
    print(myPow_iter(2,13))
    print(myPow_recur(2, 13))
