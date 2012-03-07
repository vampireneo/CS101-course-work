#Define a procedure, factorial, that
#takes one number as its input
#and returns the factorial of
#that number.


def factorial(n):
    i = 0
    f = 1
    while i < n:
        i += 1
        f = f * i
    return f

print factorial(3)
