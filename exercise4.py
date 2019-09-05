'''
Create a program that asks the user for a number
and then prints out a list of all the divisors
of that number.

'''
print('Give me a number pal')
num = input()
num = int(num)
#divisors 12, 6, 4 , 3, 2 ,1
dList = []

for i in range(1, num + 1):
    if(num % i == 0):
        dList.append(i)
print('These are the divisors:')
print(dList)
