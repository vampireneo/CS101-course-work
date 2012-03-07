#Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.


def biggest(a, b, c):
    if (a > b and a > c):
        return a
    if (b > a and b > c):
        return b
    return c

print biggest(12, 3, 5)
