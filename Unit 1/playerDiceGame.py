"""
    Create a small game where a set given number of players would throw
    3 dices, 2 times. The game would return the rest of the remaining
    combinations possible. Use lists by comprehension.
"""

import random
import time


numPlayers = int(input("Introduce number of players: "))
numRounds = int(input("Introduce the number of rounds (If you introduce 0, then by default there'd be 2 rounds): "))


def allResults(): #Creates by comprehension all combinations possible for a 3 dices throw
    return [(i,j) for i in range(1,7) for j in range(1,7)]


def checkResult(result):
    allRe = allResults()
    for i in result: #Runs through the players results list
        for k in i: #Runs through each round inside the list
            for j in allRe: #Runs through all combinations possible, deleting any coincidences
                if k[1] == j:
                    allRe.remove(j)
    return allRe #Returns the edited combinations list


def randomDice():
    return random.randint(1,6) #Generates a dice throw result (1 - 6)


def throwPlayer(nplayers): #Full round results
    result = []
    for j in range(1, nplayers+1):
        a = randomDice() #Generates 2 dice throws and saves them in variables
        b = randomDice()
        result.append(["Player"+str(j),(a,b)]) #Adds those three results as a list, within the result list
    return result


def assembleRounds(nplayers, nrounds):
    dic_results = {}
    for i in range(1, nrounds+1):
        ready = input("Hit Enter to Play the Round")
        roundname = "Round"+str(i)
        roundresults = throwPlayer(nplayers)
        dic_results.update({ roundname: roundresults })
        print("Results of the Round: ")
        print(["Round"+str(i),roundresults])
    return dic_results


if numRounds != 0:
    finalResults = assembleRounds(numPlayers, numRounds)
else:
    finalResults = throwPlayer(numPlayers)

time.sleep(5)
print("The final results of the game are: ")
print(finalResults)
print("The remaining combinations possible are: ")
print(checkResult(finalResults))

