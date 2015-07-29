def SubMax_beauty(arr):
    Start = arr[0]
    MAX = 0
    for i in range(1,len(arr)-1):
        #print i
        if Start < 0:
            Start = 0
        Start += arr[i]
        if Start > MAX:
            MAX = Start
    return MAX

A = [1, -2, 3, 5, -3, 2]

print SubMax_beauty(A)