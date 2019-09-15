'''
Write a function that takes an ordered list of
numbers (a list where the elements are in order
from smallest to largest) and another number. The
function decides whether or not the given number
is inside the list and returns (then prints) an
appropriate boolean.

Extras:

-Use binary search

'''

def search(l,num):
    return num in l
def binarySearch(l,num):
    for i in range(len(l)):
        if(l[i] == num):
            return True
    return False

if __name__ == "__main__":
    print('Binary Search: ')
    print(binarySearch([1,2,3,4], 3))
    print(binarySearch([1,2,3,4], 5))
    print(binarySearch([1,2,3,4], '3'))
    print('\n')
    print('Search: ')
    print(search([1,2,3,4], 3))
    print(search([1,2,3,4], 5))
    print(search([1,2,3,4], '3'))
