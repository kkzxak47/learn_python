def sumPowers(n, k):
    if 0==n:
        return 0
    else:
        return n**k+sumPowers(n-1, k)

def palindrome(lst):
    if len(lst)<= 1:
        return True
    elif lst[0] != lst[-1]:
        return False
    else:
        return palindrome(lst[1:-1])