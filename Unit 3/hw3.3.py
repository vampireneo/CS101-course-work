#Define a procedure, product_list,
#takes as input a list of numbers,
#and returns a number that is
#the result of multiplying all
#those numbers together.

#product_list([9]) => 9
#product_list([1,2,3,4]) => 24


def product_list(n):
    result = 1
    for i in range(len(n)):
        result = result * n[i]
    return result

print product_list([9])
print product_list([1, 2, 3, 4])
