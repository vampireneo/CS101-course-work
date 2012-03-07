# Define a procedure, median, that takes three
# numbers as its inputs, and outputs the median
# of the three numbers.

# Make sure your procedure has a return statement.


def bigger(a, b):
    if a > b:
        return a
    return b


def biggest(a, b, c):
    return bigger(a, bigger(b, c))


def median(a, b, c):
    big = biggest(a, b, c)
    if a == big:
        return bigger(b, c)
    if b == big:
        return bigger(a, c)
    return bigger(a, b)

print median(1, 2, 3)
print median(10, 12, 30)
print median(100, 200, 30)
