"""
    Create a small game where a set given number of players would throw
    3 dices, 2 times. The game would return the rest of the remaining
    combinations possible. Use lists by comprehension.
"""

import random


def allResults(): #Creates by comprehension all combinations possible for a 3 dices throw
    return [(i,j) for i in range(1,7) for j in range(1,7)]

def checkResult(result):
    allRe = allResults()
    for i in result: #Runs through the players results list
        for k in i: #Runs through each round inside the list
            for j in allRe: #Runs through all combinations possible, deleting any coincidences
                if k == j:
                    allRe.remove(j)
    return allRe #Returns the edited combinations list

def randomDice():
    return random.randint(1,6) #Generates a dice throw result (1 - 6)

def throwPlayer(nplayers): #Number of rounds can be edited but by default will be 2
    result = []
        for j in range(nplayers):
            a = randomDice() #Generates 3 dice throws and saves them in variables
            b = randomDice()
            result.append((a,b)) #Adds those three results as a list, within the result list
    return result

numPlayers = int(input("Introduce a number of players"))
numRounds = int(input("Introduce the number of rounds (If you introduce 0, then by default there'd be 2 rounds): "))
if numRounds != 0:
    finalResults = throwPlayer(numPlayers, numRounds)
else:
    finalResults = throwPlayer(numPlayers)
print("The players results are: ")
print(finalResults)
print("The remaining combinations possible are: ")
print(checkResult(finalResults))
