'''
Write a program that takes double x and integer y and returns x to the power of y
'''


def power(x, y):
    if y < 0:
        y = -y
        x = 1/x
    r = 1
    while y:
        if y & 1:
            r = r * x
        x = x * x
        y = y >> 1
    return r


if __name__ == '__main__':
    x = 2
    y = 5

    print(x, y, power(x, y))
