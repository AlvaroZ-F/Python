"""
    Create a small game where a set given number of players would throw
    3 dices, 2 times. The game would return the rest of the remaining
    combinations possible. Use lists by comprehension.
"""

import random
import time
from playDice import randomDice


numPlayers = int(input("Introduce number of players: "))
numRounds = int(input("Introduce the number of rounds (If you introduce 0, then by default there'd be 2 rounds): "))
players = {}

def throwPlayer(nplayers, playersdict): #Full round results
    result = []
    for j in range(1, nplayers+1):
        a = randomDice() #Generates 2 dice throws and saves them in variables
        b = randomDice()
        result.append((a,b)) #Adds those three results as a list, within the result list
        playersdict["Player"+str(j)].append((a,b))
    return result

def createPlayers(nplayers, playersdict):
    for i in range(1, nplayers+1):
        playersdict.update({"Player"+str(i):[]})
    time.sleep(2)
    print("Players created")

def assembleRounds(nplayers, nrounds, playersdict):
    dic_results = {}    
    createPlayers(nplayers, playersdict)
    for i in range(1, nrounds+1):
        ready = input("Hit Enter to Play the Round")
        roundname = "Round"+str(i)
        roundresults = throwPlayer(nplayers, playersdict)
        dic_results.update({ roundname: roundresults })
        print("Results of the Round: ")
        print(["Round"+str(i),roundresults])
    return dic_results

def resultsByPlayer(playersdict):
    for i in playersdict.keys():
        print(str(i)+" Results: ")
        print(playersdict[i])


if numRounds != 0:
    finalResults = assembleRounds(numPlayers, numRounds, players)
else:
    finalResults = throwPlayer(numPlayers)

time.sleep(5)
print("The final results of the game are: ")
print(finalResults)
print("Player1 Results: ")
resultsByPlayer(players)

