# coding: utf-8
import sys

def biSearch(key, s):

    if(len(s) == 0):
        return -1
    
    lo = 0
    hi = len(s)
    
    mid = len(s)//2
    
    while(lo < hi):
        if(key == s[mid]):
            return mid
        elif(key < s[mid]):
            hi = mid
        else:
            lo = mid + 1
        mid = (lo+hi)//2
    return -1

def main(args):
    vec = [2*i for i in range(1,19)]
    print(vec)
    index = biSearch(int(args[1]), vec)
    
    print(index)

if __name__ == "__main__":
    main(sys.argv)
