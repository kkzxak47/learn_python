# coding: utf-8

def find_min_steps(target):
    """find the minimum steps to go from 1 to target by +1 or *2"""
    count = 0
    while target > 1:
        if target%2:
            target -= 1
        else:
            target /= 2
        print target
        count += 1
    if target == 1:
        return count
    return -1

def main():
    """main"""
    TARGET = 2015
    print find_min_steps(TARGET)

if __name__ == '__main__':
    main()
