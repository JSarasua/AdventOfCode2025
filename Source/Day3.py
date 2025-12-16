from AoCUtilities import *
import re



def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    maxJolts = 0
    for fileLine in fileData:
        bank = fileLine.strip()
        bestNum = 0
        for i in range(len(bank)-1):
            firstNum = int(bank[i])
            for j in range(i+1, len(bank)):
                secondNum = int(bank[j])
                num = int(str(firstNum) + str(secondNum))
                if num > bestNum:
                    bestNum = num
        maxJolts += bestNum
    return maxJolts

def GetBestJolt(remainingJolts : str, startingIndex : int, numDigits : int) -> tuple[int, int]:
    bestNum = int(remainingJolts[startingIndex])
    bestIndex = startingIndex
    for i in range(startingIndex + 1, len(remainingJolts) - numDigits + 1):
        numToCheck = int(remainingJolts[i])
        if numToCheck > bestNum:
            bestNum = numToCheck
            bestIndex = i
    return bestNum, bestIndex


def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    maxJolts = 0
    for fileLine in fileData:
        bank = fileLine.strip()

        bestNumDigits = ""
        numDigits = 12
        currentIndex = 0
        for remainingDigits in range(numDigits,0,-1):
            bestCurrentDigit, currentIndex = GetBestJolt(bank, currentIndex, remainingDigits)
            bestNumDigits += str(bestCurrentDigit)
            currentIndex += 1

        maxJolts += int(bestNumDigits)
    return maxJolts




filePath = "C:\\dev\\AdventOfCode2025\\Input\\Day3.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))