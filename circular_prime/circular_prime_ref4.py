# coding: utf-8
import math
import time


def prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def cycle(num):
    strNum = str(num)
    length = len(strNum)
    cycle_all = []
    for i in range(length):
        number = int(strNum[i:] + strNum[:i])
        cycle_all.append(number)
    return cycle_all


def main(inNum):
    count = 0
    for i in range(2, inNum):
        judge = True
        for num in cycle(i):
            if not prime(num):
                judge = False
                break
        if judge:
            count += 1
    print count

if __name__ == '__main__':
    justnow = time.time()
    n = int(raw_input())
    main(n)
    print time.time() - justnow
