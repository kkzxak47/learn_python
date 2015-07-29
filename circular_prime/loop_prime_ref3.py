# coding: utf-8


def primes(max_n):
    numbers = range(3, max_n + 1, 2)
    half = (max_n) // 2
    initial = 4
    for step in xrange(3, max_n + 1, 2):
        for i in xrange(initial, half, step):
            numbers[i - 1] = 0
        initial += 2 * (step + 1)

        if initial > half:
            return [2] + filter(None, numbers)


def rotate(S_list):
    S = []
    for i in range(len(S_list)):
        S.append(int(S_list[i:] + S_list[:i]))
    return set(S)


def circularPrime(limit):
    All_primes_in_limit = primes(limit)
    circular_prime = []
    reject_list = ['0', '2', '4', '5', '6', '8']
    All_primes_in_limit = [i for i in All_primes_in_limit if not any(
        j in reject_list for j in set(str(i)))]
    while All_primes_in_limit:
        ShufleSet = rotate(str(All_primes_in_limit[-1]))
        PrimesSet = set(All_primes_in_limit)
        if not ShufleSet - PrimesSet:
            circular_prime += list(ShufleSet)
        All_primes_in_limit = list(PrimesSet - ShufleSet)
    circular_prime.sort()
    return circular_prime


# for limit value 1000000
# print circularPrime(1000000)
print len(circularPrime(1000000))+2
