"""
Write a program (function!) that takes a list and
returns a new list that contains all the elements
of the first list minus all the duplicates.
"""
#sets do not have duplicates
def listToSet(l):
    return set(l)

list1 = [1,2,3,4,4,4,5,5,5,5,5,6,6,6,6,7,6,7]
print(listToSet(list1))
