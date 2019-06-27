def countPrimes(n):
    """
    :type n: int
    :rtype: int
    """
    if n < 2:
        return 0
    isPrime = [True] * n
    isPrime[0] = isPrime[1] = False

    for p in range(2, int(n ** 0.5) + 1, 1):
        if isPrime[p]:
            for i in range(2 * p, n, p):
                isPrime[i] = False
    return sum(isPrime)


if __name__ == '__main__':
    n = 10
    print(countPrimes(n))