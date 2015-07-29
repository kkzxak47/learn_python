# coding: utf-8
TARGET = 17.3
def ttry(arr):
    num = 1
    while arr:
        print num,' now: ',arr[0]
        num += 1
        x1 = round(arr[0]*1.2, 1)
        print 'x1',x1
        x2 = round(arr[0]*0.9, 1)
        print 'x2',x2
        if x1 == TARGET or x2 == TARGET:
            print 'done, progress:',arr
            break
        if x1 < TARGET:
        	arr.append(x1)
        if x2 < TARGET:
        	arr.append(x2)
        arr.pop(0)

arr = [10.0]
ttry(arr)
# for i in range(7):
#     arr.append(round(arr[0]*1.2, 1))
#     arr.append(round(arr[0]*0.9, 1))
#     arr.pop(0)
#     print arr