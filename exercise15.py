"""
Write a program (using functions!) that asks the
user for a long string containing multiple words.
Print back to the user the same string, except
with the words in backwards order. For example,
say I type the string:

  My name is Michele
Then I would see the string:

  Michele is name My
shown back to me.

"""

def reverseString(str):
    #split String
    newStr = str.split(' ')
    #reverse list
    newStr.reverse()
    #join list
    newStr = ' '.join(newStr)
    #return
    return newStr

print(reverseString('done are we dude'))
print(reverseString('! here of out get let\'s scoob like'))
