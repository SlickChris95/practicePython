'''
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock

'''

gameOver = False
player1Input = 0
player2Input = 0

rps = {
    0:  'Rock',
    1:  'Paper',
    2:  'Scissors'
}
def printDict(dict):
    for x, y in dict.items():
        print(x,y)

def printOptions():
    print('Player 1: choose a number')
    printDict(rps)
    global player1Input
    player1Input = input()
    print('p1 :' + str(player1Input))
    print('Player 2: choose a number')
    printDict(rps)
    global player2Input
    player2Input = input()
    print('p2 :' + str(player2Input))


def checkWinner(p1Input,p2Input):
    p1 = int(p1Input)
    p2 = int(p2Input)
    # print(type(p1))
    # print(type(p2))
    #player 1 wins
    if(p1 == 0 and p2 == 2):
        print('player1 wins')
    elif(p1 == 1 and p2 == 0):
        print('player1 wins')
    elif(p1 == 2 and p2 == 1):
        print('player1 wins')
    #player 2 wins
    elif(p2 == 0 and p1 == 2):
        print('player2 wins')
    elif(p2 == 1 and p1 == 0):
        print('player2 wins')
    elif(p2 == 2 and p1 == 1):
        print('player2 wins')
    else:
        print('Tie')

while (gameOver == False):
    printOptions()
    checkWinner(player1Input,player2Input)
    gameOver = True
