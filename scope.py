player1Input = 0
player2Input = 0

def printOptions():
    print('Player 1: choose a number')
    # printDict(rps)
    player1Input = input()
    print('p1 :' + str(player1Input))
    print('Player 2: choose a number')
    # printDict(rps)
    player2Input = input()
    print('p2 :' + str(player2Input))


def checkWinner(p1Input,p2Input):
    #player 1 wins
    if(p1Input == 0 and p2Input == 2):
        print('player1 wins')
    elif(p1Input == 1 and p2Input == 0):
        print('player1 wins')
    elif(p1Input == 2 and p2Input == 1):
        print('player1 wins')
    #player 2 wins
    elif(p2Input == 0 and p1Input == 2):
        print('player2 wins')
    elif(p2Input == 1 and p1Input == 0):
        print('player2 wins')
    elif(p2Input == 2 and p1Input == 1):
        print('player2 wins')

printOptions()
print(player1Input)
print(player2Input)
