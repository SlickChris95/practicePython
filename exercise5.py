import random
'''
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains
only the elements that are common between the lists
(without duplicates). Make sure your program works on two lists of different sizes.

Extras:

1)Randomly generate two lists to test this

'''
def createRandomList(list,number):
    for i in range(number):
        list.append(random.randint(0,50))
    list.sort()

def numbersInCommon(a,b):
    for i in range(len(a)):
        if(b[i] in a):
            common.append(b[i])

a =[]
b =[]
common = []

createRandomList(a,7)
print('list a:')
print(a)
createRandomList(b,7)
print('list b:')
print(b)

numbersInCommon(a,b)
print(common)
