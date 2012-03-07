#Define a procedure, is_friend, that
#takes a string as its input, and
#outputs a Boolean indicating if
#the input string is the name of
#a friend. Assume I am friends with
#everyone whose name starts with D
#and no one else.

#print is_friend('Diane') => True
#print is_friend('Fred')  => False


def is_friend(n):
    return n.find('D') == 0

print is_friend('Diane')
print is_friend('Fred')
