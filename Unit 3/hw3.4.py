#Define a procedure, greatest,
#that takes as input a list
#of positive numbers, and
#returns the greatest number
#in that list. If the input
#list is empty, the output
#should be 0.

#greatest([4,23,1]) => 23
#greatest([]) => 0


def greatest(n):
    result = 0
    for i in range(len(n)):
        if n[i] > result:
            result = n[i]
    return result


print greatest([4, 23, 1])
print greatest([])
