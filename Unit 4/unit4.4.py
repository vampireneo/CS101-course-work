#Define a procedure, lookup,
#that takes two inputs:

#   - an index
#   - keyword

#The output should be a list
#of the urls associated
#with the keyword. If the keyword
#is not in the index, the output
#should be an empty list.

index = [['udacity', ['http://udacity.com', 'http://npr.org']],
         ['computing', ['http://acm.org']]]

#lookup(index,'udacity') => ['http://udacity.com','http://npr.org']


def lookup(index, keyword):
    for i in index:
        if i[0] == keyword:
            return i[1]
    return []

print lookup(index, 'udacity')
