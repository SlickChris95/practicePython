'''
Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user.

extra:
1)  If the number is a multiple of 4, print out a different message.
'''
print('Give me a number')
num = input()
num = int(num)

if(num % 4 ==0):
    print('divisible by 4')
elif(num % 2 == 0):
    print('even')
elif(num % 2 != 0):
    print('odd')
