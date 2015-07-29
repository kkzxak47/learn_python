def catalan(n):
    ans = 1
    for i in range(1, n+1):
        ans = ans * 2 * (2*i-1) / (i+1)
    return ans

num=int(raw_input("input n: "))
while(num) >= 0:
    print "catalan number of %s:" % num,catalan(num)
    num=int(raw_input("input n: "))