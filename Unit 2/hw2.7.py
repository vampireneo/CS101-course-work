#2 GOLD STARS

#Define a procedure,
#print_multiplication_table,
#that takes as input a positive whole
#number, and prints out a multiplication,
#table showing all the whole number
#multiplications up to and including the
#input number. The order in which the
#equations are printed must match exactly.

#print_multiplication_table(2)
#1 * 1 = 1
#1 * 2 = 2
#2 * 1 = 2
#2 * 2 = 4


def print_multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print str(i) + " * " + str(j) + " = " + str(i * j)

print_multiplication_table(2)
