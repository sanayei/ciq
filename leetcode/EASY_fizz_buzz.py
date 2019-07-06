# Write a program that outputs the string representation of numbers from 1 to n.
#

#
# Example:
#
# n = 15,
#
# Return:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]

def fizzBuzz(n):
    out = []
    for i in range(n):
        num = i + 1
        # print(num)
        if num % 3 == 0 and num % 5 == 0:
            out.append('FizzBuzz')
        elif num % 3 == 0:
            out.append('Fizz')
        elif num % 5 == 0:
            out.append('Buzz')
        else:
            out.append(str(num))

    return out


if __name__ == '__main__':
    n= 15
    print(fizzBuzz(n))