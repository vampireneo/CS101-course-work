#Define a procedure, bigger, that takes in
#two numbers as inputs, and outputs the
#greater of the two inputs.

#bigger(2,7) => 7
#bigger(3,2) => 3
#bigger(3,3) => 3


def bigger(a, b):
    if a > b:
        return a
    return b

print bigger(3, 3)
