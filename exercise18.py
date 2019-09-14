"""
What the if __name__=="__main__" statement from
above does is ensure that variables that are created,
functions that are called, operations that are done,
etc ONLY when you directly run the file, not when you
import it into another.

Instructions:
Create a program that will play the “cows and bulls” game with the user. The game works like this:

Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
For every digit that the user guessed correctly in the correct place, they
have a “cow”. For every digit the user guessed correctly in the wrong place
is a “bull.” Every time the user makes a guess, tell them how many “cows”
and “bulls” they have. Once the user guesses the correct number, the game
is over. Keep track of the number of guesses the user makes throughout
the game and tell the user at the end.

"""
import random
import time

ans = []
cows = 0
bulls = 0
attempts = 0

#1) Generate random #

def createRandomNumber(n):
    for i in range(0,n):
        ans.append(random.randint(0,9))
def checkCows(list1,list2):
    cows = 0
    a = list1
    b = list2
    for i in range(len(list1)):
        if(b[i]==a[i]):
            cows = cows + 1
    return cows
def checkBulls(list1,list2):
    bulls = 0
    cows = checkCows(list1,list2)
    for i in range(len(list1)):
        if(list1[i] in list2):
            bulls = bulls + 1
    return bulls - cows
def wonGame():
    win = True
    print('Congrats you are a true cowboy!')
    time.sleep(1)
    exit()

def numberGuess():
    attempts = 0
    #2) User guesses #
    user_num = input('Enter a 4 digit number: ')
    user_num = list(user_num)
    user_num = [int(i) for i in user_num]
    print(user_num)
    print(ans)
    #3)Check if any of the digits are the on the
    #same spot
    cows = checkCows(user_num,ans)
    #4)Check if we have any bulls
    bulls = checkBulls(user_num,ans)
    print('cows: {}'.format(cows))
    print('bulls: {}'.format(bulls))
    attempts += 1
    print('attempts: {}'.format(attempts))

    if(cows == 4):
        wonGame()





if __name__ == "__main__":
    print("Welcome to the Cows and Bulls Game!")
    print('''Rules: \n For every digit that the you guessed correctly in the correct place,
    you get a “cow”. For every digit that is guessed correctly in the wrong place is a “bull.”
    ''')
    print('Good luck cowboy!')
    createRandomNumber(4)

    x = 0
    while x < 100:
        numberGuess()
        x +=1
