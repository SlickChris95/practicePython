"""
Write a password generator in Python. Be creative
with how you generate passwords - strong passwords
have a mix of lowercase letters, uppercase letters,
numbers, and symbols. The passwords should be
random, generating a new password every time the
user asks for a new password. Include your run-time
code in a main method.

Extra:

Ask the user how strong they want their password to
be. For weak passwords, pick a word or
two from a list.

"""
import random

def randomPassGenerator(difficulty):
    newPassWord = []
    passStr = difficulty.upper()
    def alphaAppend(nums,l):
        a = ['a','w','e','r','t','y','u','i','o','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
        for i in range(0,nums):
            l.insert(random.randint(0,len(a)) ,a[random.randint(0,len(a) - 1)])

    def charAppend(nums,l):
        s = ['!','@','#','$','%','^','&','*']
        for i in range(0,nums):
            l.insert(random.randint(0,len(l)) ,s[random.randint(0,len(s) - 1)])

    def numAppend(nums,l):
        n = ['1','2','3','4','5','6','7','8','9','0']
        for i in range(0,nums):
            l.insert(random.randint(0,len(l)) ,n[random.randint(0,len(n) - 1)])
    def randomCapitalize(l):
        for i in range(0,len(l)//2):
            r = random.randint(0,len(l)-1)
            temp = l[r].upper()
            l[r] = temp

    def convert(s):
        if(passStr == 'HARD'):
            print(s)
            randomCapitalize(s)
        new = ""
        for x in s:
            new += x
        return new
#if easy, 4 chars and 1 number
    if(passStr == 'EASY'):
        alphaAppend(4,newPassWord)
        charAppend(1,newPassWord)
        return convert(newPassWord)
    elif(passStr == 'MEDIUM'):
        alphaAppend(6,newPassWord)
        charAppend(2,newPassWord)
        numAppend(2,newPassWord)
        return convert(newPassWord)
    else:
        alphaAppend(8,newPassWord)
        charAppend(3,newPassWord)
        numAppend(2,newPassWord)
        return convert(newPassWord)

#if hard 8 chars with 2 numbers 3 symbols and random capitalization


print('Easy, medium, hard?')
passStrength = input()
print(randomPassGenerator(passStrength))
