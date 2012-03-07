# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and outputs the last position in the search string
# where the target string appears, or -1 if there
# are no occurences.
#
# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.


def find_last(s, t):
    r = s.find(t)
    while r != -1:
        tmp = s.find(t, r + 1)
        if tmp == -1:
            break
        r = tmp
    return r


print find_last('aaaa', 'aa')
print find_last('', '')
print find_last('', 'aa')
