'''
Ask the user for a number and determine whether
the number is prime or not. (For those who have
forgotten, a prime number is a number that has no
divisors.). You can (and should!) use your answer
to Exercise 4 to help you. Take this opportunity
to practice using functions, described below.

'''

def isPrime(n):
    if(len(divisors(n)) < 2):
        return True
    else:
        return False

def divisors(n):
    return [i for i in range(1,n) if(n % i == 0)]

# print('Type in a number')
# num = int(input())
#
#
# print(type(num))
print(isPrime(10))
