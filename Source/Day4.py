from AoCUtilities import *
import re


def IsTooHeavy(strArray : list, x : int, y : int) -> bool:
    topLeft = x-1,y-1
    top = x,y-1
    topRight = x+1,y-1
    right = x+1,y
    bottomRight = x+1,y+1
    bottom = x,y+1
    bottomLeft = x-1,y+1
    left = x-1,y

    count = 0
    if IsValidCoordinateTuple(strArray, topLeft):
        if GetValAtCoordinate(strArray, topLeft) == '@':
            count += 1
    if IsValidCoordinateTuple(strArray, top):
        if GetValAtCoordinate(strArray, top) == '@':
            count += 1
    if IsValidCoordinateTuple(strArray, topRight):
        if GetValAtCoordinate(strArray, topRight) == '@':
            count += 1
    if IsValidCoordinateTuple(strArray, right):
        if GetValAtCoordinate(strArray, right) == '@':
            count += 1
    if IsValidCoordinateTuple(strArray, bottomRight):
        if GetValAtCoordinate(strArray, bottomRight) == '@':
            count += 1
    if IsValidCoordinateTuple(strArray, bottom):
        if GetValAtCoordinate(strArray, bottom) == '@':
            count += 1
    if IsValidCoordinateTuple(strArray, bottomLeft):
        if GetValAtCoordinate(strArray, bottomLeft) == '@':
            count += 1
    if IsValidCoordinateTuple(strArray, left):
        if GetValAtCoordinate(strArray, left) == '@':
            count += 1

    return count >= 4

def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    strArray = Make2DStrArray(fileData)
    goodRolls = 0

    for y in range(len(strArray)):
        strRow = strArray[y]
        for x in range(len(strRow)):
            if strRow[x] == '@':
                if not IsTooHeavy(strArray, x, y):
                    goodRolls += 1
    return goodRolls

def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    strArray = Make2DStrArray(fileData)
    goodRolls = 0

    for numTests in range(1000):
        for y in range(len(strArray)):
            strRow = strArray[y]
            for x in range(len(strRow)):
                if strRow[x] == '@':
                    if not IsTooHeavy(strArray, x, y):
                        goodRolls += 1
                        strArray[y][x] = '.'
    return goodRolls


filePath = "C:\\dev\\AdventOfCode2025\\Input\\Day4.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))