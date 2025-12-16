from AoCUtilities import *

def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    startingNum = 50

    zeroCount = 0

    for fileLine in fileData:
        rowData = fileLine.strip()
        direction = rowData[0]
        count = int(rowData[1:])
        if direction == "R":
            startingNum += count
            while (startingNum > 99):
                startingNum -= 100
        else:
            startingNum -= count
            while (startingNum < 0):
                startingNum += 100
        if (startingNum == 0):
            zeroCount += 1

    return zeroCount

def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    startingNum = 50

    zeroCount = 0
    overCounts = 0

    for fileLine in fileData:
        rowData = fileLine.strip()
        direction = rowData[0]
        count = int(rowData[1:])
        if direction == "R":
            startingNum += count
            while (startingNum > 99):
                startingNum -= 100
                overCounts += 1
        else:
            startingNum -= count
            while (startingNum < 0):
                startingNum += 100
                overCounts += 1
        if (startingNum == 0):
            zeroCount += 1

    return overCounts

filePath = "C:\\dev\\AdventOfCode2025\\Input\\Day1.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))