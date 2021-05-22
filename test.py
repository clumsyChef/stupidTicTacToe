import os
import copy
import random
import time

allPosis = {
    "T-L": " ",
    "T-M": " ",
    "T-R": " ",
    "C-L": " ",
    "C-M": " ",
    "C-R": " ",
    "B-L": " ",
    "B-M": " ",
    "B-R": " "
}

x = []
o = []

chance = 'X'
played = 0

def makeBox():
    print()
    print(f' {allPosis["T-L"]} | {allPosis["T-M"]} | {allPosis["T-R"]} ')
    print("___|___|___")
    print(f' {allPosis["C-L"]} | {allPosis["C-M"]} | {allPosis["C-R"]} ')
    print("___|___|___")
    print(f' {allPosis["B-L"]} | {allPosis["B-M"]} | {allPosis["B-R"]} ')
    print("   |   |   ")
    print()


def checkWin(bajji):
    global x, o
    allMoves = {}
    
    thisList = copy.deepcopy(x) if bajji == 'O' else copy.deepcopy(o)

    for i in thisList:
        first = i.split("-")[0]
        second = i.split("-")[1]
        allMoves.setdefault(first, 0)
        allMoves[first] += 1
        allMoves.setdefault(second, 0)
        allMoves[second] += 1
    

    won = False
    for j in list(allMoves.values()):
        if(j == 3):
            won = True
            break
    
    if(won == False):
        if('T-L' in thisList and 'C-M' in thisList and 'B-R' in thisList):
            won = True
        
        if('T-R' in thisList and 'C-M' in thisList and 'B-L' in thisList):
            won = True

    return won



def startGame():
    global chance, played, x, o
    while True:
        remains = []
        for k, v in allPosis.items():
            if(v == " "):
                remains.append(k)
       
        move = random.choice(remains)
        move = move.upper()
        hasMove = allPosis.get(move, 0)
        if(hasMove == 0):
            continue

        if(allPosis[move] != " "):
            continue
        
        allPosis[move] = chance
        played += 1

        if(chance == 'O'):
            o.append(move)
            chance = 'X'
        else:
            x.append(move)
            chance = 'O'
        

        if(played > 4):
            won = checkWin(chance)
            if(won):
                winner = 'X' if chance == 'O' else 'O'
                return 'X' if winner == 'X' else 'O'
                break

        if(played == 9):
            return "D"
            break


#startGame()

def makeBotsPlay():
    global x, o, played, chance, allPosis
    

    player_1 = 0
    player_2 = 0
    draw = 0
    
    for i in range(100000):
        x = []
        o = []
        chance = 'X'
        played = 0
        for j in allPosis.keys():
            allPosis[j] = ' '

        winner = startGame()
        if(i % 2 == 0):
            if (winner == 'X'):
                player_1 += 1
            elif (winner == 'O'):
                player_2 += 1
        else:
            if (winner == 'X'):
                player_2 += 1
            elif (winner == 'O'):
                player_1 += 1

        if (winner == "D"):
            draw += 1

    print(f'''\n----------------------------------------------------------------------
\n\t\t Player 1 : {player_1}
\t\t Player 2 : {player_2}
\t\t Draw : {draw}
\n----------------------------------------------------------------------\n''')



makeBotsPlay()





