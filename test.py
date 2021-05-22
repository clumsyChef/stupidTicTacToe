import os
import copy

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

gameOn = True
played = 0

winnings = [

]

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
        moveLength = len(list(allMoves.keys()))
        if moveLength == 6:
            won = True


    return won


while gameOn:
    remains = []
    for k, v in allPosis.items():
        if(v == " "):
            remains.append(k)

    makeBox()
    remainingPosis = ', '.join(remains)
    dashes = "-"*(len(remainingPosis) + 26 + 8 + 8) 
    
    print(f'''\n|{dashes}|
|{" "*len(dashes)}|
\tRemaining positions are : {remainingPosis}\t
|{" "*len(dashes)}|
|{dashes}|\n''')
    
    move = input(f"'{chance}' goes to :  ")
    move = move.upper()
    hasMove = allPosis.get(move, 0)
    if(hasMove == 0):
        print('''|------------------------------------------|
|\t\t\t\t\t   |
|\t Try again with valid value \t   |
|\t\t\t\t\t   |
|------------------------------------------|''')
        continue

    if(allPosis[move] != " "):
      
        print('''|---------------------------|
|                           |
|   Already in use andhe!   |
|                           |
|---------------------------|''')
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
            os.system('clear') 
            makeBox()

            print(f'''\t\t|------------------------------------------|
\t\t|                                          |
\t\t|              '{winner}' JEET GAYA               |    
\t\t|                                          |
\t\t|------------------------------------------|''')


            break

    
    if(played == 9):
        print("No one won, both are fucking idiots")
        makeBox()
        break
    
