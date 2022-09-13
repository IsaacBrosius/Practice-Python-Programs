import random

pickers = [
    ["Person 1: Group 1"],
    ["Person 2: Group 2", "Person 3: Group 2", "Person 4: Group 2"],
    ["Person 5: Group 3", "Person 6: Group 3"],
    ["Person 7: Group 4", "Person 8: Group 4", "Person 9: Group 4", "Person 10: Group 4"]
]

trashCan1 = []

trashCan2 = []

pickNum = 0

totalPersonCount = 0

for i in range(len(pickers)):
    totalPersonCount += len(pickers[i])

failTimes = 0

def checkList(list, value):
    for x in list:
        if x == value:
            return True
    return False

def cleanList(listName):
    for x in listName:
        listName.remove(x)

while pickNum < totalPersonCount:

    if failTimes >= 1000:
        cleanList(trashCan1)
        cleanList(trashCan2)
        failTimes = 0

    groupPick1 = pickers[random.randint(0, (len(pickers) - 1))]
    groupPick2 = pickers[random.randint(0, (len(pickers) - 1))]

    if groupPick1 != groupPick2:
        personPick1 = groupPick1[random.randint(0, (len(groupPick1) -1))]
        personPick2 = groupPick2[random.randint(0, (len(groupPick2) -1))]

        if pickNum == 0:
            trashCan1.append(personPick1)
            trashCan2.append(personPick2)
            pickNum += 1
            failTimes = 0
            
        elif (checkList(trashCan1, personPick1) == False) and (checkList(trashCan2, personPick2) == False) :
            trashCan1.append(personPick1)
            trashCan2.append(personPick2)
            pickNum += 1
            failTimes = 0

        else: failTimes += 1

    else: failTimes +=1

    if pickNum >= totalPersonCount:
        
        for i in range(totalPersonCount):
            print(str(trashCan1[i]) + " has " + str(trashCan2[i]))