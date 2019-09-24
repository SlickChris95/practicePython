'''
This time, we’re going to do exactly the opposite.
You, the user, will have in your head a number
between 0 and 100. The program will guess a number,
and you, the user, will say whether it is too high,
too low, or your number.

At the end of this exchange, your program should
print out how many guesses it took to get your number.

As the writer of this program, you will have to
choose how your program will strategically guess.
A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number. But that’s not an optimal guessing strategy. An alternate strategy might be to guess 50 (right in the middle of the range), and then increase / decrease by 1 as needed. After you’ve written the program, try to find the optimal strategy! (We’ll talk about what is the optimal one next week with the solution.)

'''

#prompt user to think of a number

#guess the number from 0 - 100
#guess random number

#if too high look only at numbers that are lower than that numbers
#so we are shortening our numbers to look from

import random

randomNum = random.randint(0,100)

def checkWin(str,randomNum):
    s = str
    s = s.upper()
    if s == 'YES':
        return True
    else:
        print('Too high or Too low?')
        UserR = input().upper()
        if(UserR == 'LOW'):
            rNum = random.randint(randomNum,100)
            print(rNum)
            return rNum

        elif(UserR == 'HIGH'):
            rNum = random.randint(0,randomNum)
            print(rNum)
            return rNum

# def guessNumber():


print('Think of a number and i\'ll guess it')
print('Is it %d ?' % randomNum)
userResponse = input()

# guessNumber()

if(checkWin(userResponse,randomNum)):
    print('Nice')
else:
    print('keep guessing')
    randomNum = checkWin(userResponse,randomNum)


print(randomNum)
