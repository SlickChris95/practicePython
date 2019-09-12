"""
Write a program that asks the user how many
Fibonnaci numbers to generate and then generates
them. Take this opportunity to think about how
you can use functions. Make sure to ask the user
to enter the number of numbers in the sequence to
generate

"""

def fibo(n):
    fiboList = [0,1]
    seq = 1
    if n == 0:
        return [0]
    if n == 1:
        return fiboList
    for i in range(2,n):
        fiboList.append(fiboList[i-1] + fiboList[i-2])
        print('i: {}'.format(i))
    return fiboList

print(fibo(0))
print(fibo(1))
print(fibo(3))
print(fibo(4))
print(fibo(5))
print(fibo(6))
print(fibo(7))
print(fibo(8))
