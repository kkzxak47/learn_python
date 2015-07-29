def max(l):
    m = l[0]
    m2 = m - 1
    for i in l:
        if (i > m):
            m2 = m
            m = i
        elif (i > m2):
            m2 = i
    return m, m2

def fib(n):
    return n if (2 > n) else fib(n-1) + fib(n-2)
xl = [7,5,3,9,8,11,3,0,2,10]
print(max(xl))
print(fib(9))