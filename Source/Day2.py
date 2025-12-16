from AoCUtilities import *

def TestNum( num : int ) -> bool:
    numStr = str(num)
    if numStr[0] == "0":
        return False

    length = len(numStr)
    if length % 2 != 0:
        return True

    firstStr = numStr[0:length//2]
    secondStr = numStr[length//2:]
    if firstStr == secondStr:
        return False

    return True

def TestNumB( num : int ) -> bool:
    numStr = str(num)
    if numStr[0] == "0":
        return False

    length = len(numStr)
    if length <= 1:
        return True


    for i in range(2, length + 1):
        if length % i != 0:
            continue

        numParts = length//i
        numChunks = [numStr[index:index+numParts] for index in range(0, length, numParts)]
        if len(set(numChunks)) == 1:
            return False
    return True

def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    ranges = []
    for fileLine in fileData:
        ranges += fileLine.strip().split(',')

    invalidSums = 0
    for rangeVals in ranges:
        if '-' not in rangeVals:
            continue
        min = int(rangeVals.split('-')[0])
        max = int(rangeVals.split('-')[1])

        for i in range(min,max+1):
            if not TestNum(i):
                invalidSums += i

    return invalidSums

def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    ranges = []
    for fileLine in fileData:
        ranges += fileLine.strip().split(',')

    invalidSums = 0
    for rangeVals in ranges:
        if '-' not in rangeVals:
            continue
        min = int(rangeVals.split('-')[0])
        max = int(rangeVals.split('-')[1])

        for i in range(min,max+1):
            if not TestNumB(i):
                invalidSums += i

    return invalidSums

filePath = "C:\\dev\\AdventOfCode2025\\Input\\Day2.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))