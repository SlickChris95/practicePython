'''
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low,
too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.

'''



import random as r
import sys


answer = r.randint(1,10)
print(answer)
correct = False
counter = 1

while correct == False:
    print('guess a number between 1 - 9')
    guess = input()
    if(guess == 'exit'):
        sys.exit()
    if(int(guess) == answer):
        print('Nice, you got it!')
        print('took ya %d try/s!' % (counter))
        correct = True
    else:
        print('Sorry bud, keep trying!')
    counter +=1
