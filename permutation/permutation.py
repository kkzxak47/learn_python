# coding: utf-8


def permutation1(arr, result=None, out=None):
    if result is None:
        result = []
    if out is None:
        out = []
    if len(arr) == 0:
        print(out)
        result.append(out[:])
    else:
        for i in range(len(arr)):
            out.append(arr[i])
            permutation1(arr[:i]+arr[(i+1):], result, out)
            out.remove(arr[i])
    return result


def findK(arr):
    result = -1
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            result = i
    return result


def findL(arr, k):
    result = k
    for i in range(k, len(arr)):
        if arr[k] < arr[i]:
            result = i
    return result


def reverse(arr, i, j):
    while(j > i):
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1


def permutation2(arr):
    result = []
    result.append(arr[:])
    k = findK(arr)
    while(k >= 0):
        lst = findL(arr, k)
        arr[k], arr[lst] = arr[lst], arr[k]
        reverse(arr, k+1, len(arr)-1)
        result.append(arr[:])
        k = findK(arr)
    return result


# result = permutation1([1,2,3,4])
# print(result)
arr = [1, 2, 3, 4]

# print(findK(arr))
# print(findL(arr, 2))
result = permutation2(arr)
for s in result:
    print(s)
