#!/usr/bin/env python
from sys import argv

def parse(inputText):
    with open(inputText, "r") as f:
        return list(map(int, f.read().split("\n")[:-1]))

def countSums(inputList):
    sumTable = set()
    ret = 0
    for elem in inputList:
        sumTable.add(elem)
    for num in range(-10000, 10001):
        print(num, ret)
        for elem in inputList:
            if num - elem in sumTable:
                ret += 1
                break
    return ret

if __name__ == "__main__":
    if len(argv) != 2:
        print("usage: ./2-sum.py list.txt")
        exit()
    inputList = parse(argv[1])
    finalCount = countSums(inputList)
    print("Final count: " + str(finalCount))
