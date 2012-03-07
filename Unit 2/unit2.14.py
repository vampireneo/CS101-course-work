#Define a procedure, abbaize, that takes
#two strings as its inputs, and outputs
#a string that is the first input,
#followed by two repetitions of the second input,
#followed by the first input.

#abbaize('a','b') => 'abba'
#abbaize('dog','cat') => 'dogcatcatdog'


def abbaize(a, b):
    return a + b + b + a

print abbaize('a', 'b')
print abbaize('dog', 'cat')
