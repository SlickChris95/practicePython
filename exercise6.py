'''
Ask the user for a string and print out whether
this string is a palindrome or not. (A palindrome
is a string that reads the same forwards and
backwards.)

ex: aabaa, aba, aaa
'''
#get the halfway mark of the string.
#compare one side to the other

test = 'aba'
mid = len(test)//2


def palindromeCheck(str):
    mid = len(str) // 2
    last = len(str) - 1
    if(len(str) == 1 or len(str) == 0):
        return True
    for i in range(mid):
        if(str[i] != str[last - i]):
            return False
    return True

if(palindromeCheck('racecar')):
    print('True')
else:
    print('False')
