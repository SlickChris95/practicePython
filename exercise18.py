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
#1) Generate random #
ans = []
cows = 0
bulls = 0
def createRandomNumber(n):
    for i in range(0,n):
        ans.append(random.randint(0,10))
def checkCows(list1,list2):
    cows = 0
    a = list1
    b = list2
    for i in range(len(list1)):
        if(b[i]==a[i]):
            cows +=1
createRandomNumber(4)
# user_num = input('Enter a 4 digit number: ')
# user_num = list(user_num)
# print(user_num)
x = 0
while x < 3:
    user_num = input('Enter a 4 digit number: ')
    user_num = list(user_num)
    print(user_num)
    print(ans)
    checkCows(user_num,ans)
    print('cows: {}'.format(cows))

    x +=1
#2) User guesses #

#3)Check if any of the digits are the on the
#same spot

#4)Check if we have any bulls






#for every guess the user guessed in
# the correct place they get a "cow"

#for every digit the user guessed in the wrong
#place is a "bull"



#
# if __name__ == "__main__":
#     print("Welcome to the Cows and Bulls Game!")
#     user_num = input('Enter a 4 digit number: ')
