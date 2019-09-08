'''
Take two lists, say for example these two:

	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the
elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.
'''
import random

a = [ random.randint(1,20) for i in range(10) ]
b = [ random.randint(1,20) for i in range(10) ]

print('list a : %s' % a)
print('list b : %s' % b)
c = [x for x in b if x in a]
print(c)
