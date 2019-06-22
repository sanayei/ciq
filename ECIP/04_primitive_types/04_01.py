# find parity of a word
# parity of a binary word is based on number of ones: if number of is odd then parity is 1 otherwise is 0.


def parity1(x):
    '''
    Time complexity = O(n) where n is number of bits
    '''
    result = 0
    while x:
        result = result ^ x&1
        x = x >> 1
    return result


def parity2(x):
    '''
    Time complexity = O(k) where k is number of bits equal to 1
    '''

    result = 0
    while x:
        x = x & (x-1)
        result = result ^ 1
    return result


def parity3(x):

    x = x ^ x>>32
    x = x ^ x>>16
    x = x ^ x>>8
    x = x ^ x>>4
    x = x ^ x>>2
    x = x ^ x>>1
    return x & 1





if __name__ == '__main__':
    x = 45
    y = 47
    print(bin(x), x, parity1(x), parity2(x), parity3(x))
    print(bin(y), y, parity1(y), parity2(y), parity3(y))