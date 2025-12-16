from AoCUtilities import *

def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    freshNums = 0
    freshRanges = []
    numsToCheck = []
    for fileline in fileData:
        fileLine = fileline.strip()
        if fileLine.find("-") != -1:
            rangeList = fileLine.split("-")
            freshRanges.append((int(rangeList[0]),int(rangeList[1])))
        elif fileLine == "":
            continue
        else:
            numsToCheck.append(int(fileLine))

    for num in numsToCheck:
        for freshRange in freshRanges:
            if num >= freshRange[0] and num <= freshRange[1]:
                freshNums += 1
                break

    return freshNums

def MergeRanges(start1, end1, start2, end2) -> tuple[bool,int,int]:
    start = max(start1, start2)
    end = min(end1, end2)
    if start <= end:
        newStart = min(start1, start2)
        newEnd = max(end1, end2)
        return True, newStart, newEnd
    return False, -1, -1

def MergeIntoAllRanges(ranges : list[tuple[int, int]], rangeToAdd : tuple[int,int]) -> list[tuple[int, int]]:
    newRanges = ranges.copy()

    didOverlap = False
    for curRangeIndex in range(len(ranges)):
        curRange = ranges[curRangeIndex]
        result = MergeRanges(curRange[0], curRange[1], rangeToAdd[0], rangeToAdd[1])
        if result[0]:
            newRanges[curRangeIndex] = result[1],result[2]
            newRanges = CollapseRanges(newRanges)
            didOverlap = True
            break
    if not didOverlap:
        newRanges.append(rangeToAdd)
    return newRanges

def CollapseRanges(ranges : list[tuple[int, int]]) -> list[tuple[int, int]]:
    newRanges = ranges.copy()

    if len(newRanges) <= 1:
        return newRanges
    elementRemoved = False
    for firstRangeIndex in range(len(newRanges)):
        for secondRangeIndex in range(firstRangeIndex+1, len(newRanges)):
            start1 = newRanges[firstRangeIndex][0]
            start2 = newRanges[secondRangeIndex][0]
            end1 = newRanges[firstRangeIndex][1]
            end2 = newRanges[secondRangeIndex][1]
            mergeResult = MergeRanges(start1, end1, start2, end2)
            if mergeResult[0]:
                newRanges[firstRangeIndex] = mergeResult[1],mergeResult[2]
                del newRanges[secondRangeIndex]
                elementRemoved = True
                break
        if elementRemoved:
            break
    if elementRemoved:
        return CollapseRanges(newRanges)
    return newRanges

def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    freshRanges = []
    for fileline in fileData:
        fileLine = fileline.strip()
        if fileLine.find("-") != -1:
            rangeList = fileLine.split("-")
            firstNum = int(rangeList[0])
            secondNum = int(rangeList[1])
            freshRanges = MergeIntoAllRanges(freshRanges, (firstNum, secondNum))

        else:
            continue


    freshNums = 0
    for freshRange in freshRanges:
        freshNums += abs(freshRange[1] - freshRange[0]) + 1

    return freshNums

filePath = "C:\\dev\\AdventOfCode2025\\Input\\Day5.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))