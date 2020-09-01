import random

def createList(length):
    newList = []
    for i in range(length):
        newList.append(random.randint(0,1000))

    return newList