# coding: utf-8

import math

def bestPlan(quantityList_orig, targetNum, composeNum):
    quantityList = quantityList_orig[:]
    length = len(quantityList)
    # print quantityList
    quantityListHistory = quantityList[:]
    for i in range(length-1):
        quantityList[i+1] += quantityList[i] / composeNum
        quantityListHistory[i+1] = quantityList[i+1]
        quantityList[i] %= composeNum
    # print quantityList
    # print quantityListHistory
    
    steps = int(math.ceil(float(targetNum - sum(quantityList)) / (composeNum-1)))
    # print "steps:",steps
    
    #为了种够一百棵
    while steps > 0:
        # print "current quantityList:",quantityList
        for i in range(1, length):
            if quantityList[i] > 0 and quantityList[i-1]+composeNum <= quantityList_orig[i-1]:
                quantityList[i] -= 1
                quantityList[i-1] += composeNum
                steps -= 1
                break

    # print quantityList
    result = []
    while targetNum > 0 and quantityList:
        curNum = quantityList.pop()
        if targetNum > curNum:
            result.insert(0, curNum)
        else:
            result.insert(0, targetNum)
        targetNum -= curNum

    while len(result) < length:
        result.insert(0, 0)

    return result

def absNum(nList):
    std = [1, 3, 9, 27, 81] # quantity standard
    return sum([x*y for x,y in zip(nList, std)])

def score(qList):
    std = [1, 5, 25, 125, 625] # score standard
    return sum([x*y for x,y in zip(qList, std)])

tgtNum = 100 # target number
cpNum = 3 # compose number

s1 = [5000, 50, 1, 50, 13]
score1 = score(s1)
num1 = absNum(s1)
print "original score of s1:",score1
print "original abs number of s1:",num1

result1 = bestPlan(s1, tgtNum, cpNum)
optScore1 = score(result1)
absnum1 = absNum(result1)

print "best plan for " + str(s1) + " is " + str(result1)
print "opt score:",optScore1
print "opt absNum:",absnum1
print "------"


s2 = [20, 20, 20, 20, 20]
score2 = score(s2)
num2 = absNum(s2)
print "original score of s2:",score2
print "original abs number of s2:",num2

result2 = bestPlan(s2, tgtNum, cpNum)
optScore2 = score(result2)
absnum2 = absNum(result2)

print "best plan for " + str(s2) + " is " + str(result2)
print "opt score:",optScore2
print "opt absNum:",absnum2