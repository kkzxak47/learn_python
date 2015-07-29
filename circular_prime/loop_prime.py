# coding: utf-8

from math import sqrt, log10


def primes(n):
    """ Returns a set of primes < n """
    sieve = [True] * n
    for i in xrange(3, int(sqrt(n)) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) / (2 * i) + 1)
    return set([2]) | set([i for i in xrange(3, n, 2) if sieve[i]])


def primes2(n):
    sieve = [True] * n
    for i in xrange(3, int(sqrt(n)) + 1, 2):
        if sieve[i]:
            for j in xrange(i + i, n, i):
                sieve[j] = False
    return set([2]) | set([i for i in xrange(3, n, 2) if sieve[i]])


def isLoopPrime(n, set_p):
    """接收一个素数和素数表，判断其是否为循环素数
    example: 197 -> True
    """
    digits = int(log10(n))
    for _ in range(digits):
        n = n / 10 + (n % 10) * (10 ** digits)
        if n not in set_p:
            return False
    return True


def main():
    n = 1000000
    set_p = primes2(n)
    count = 0

    for prime in set_p:
        if isLoopPrime(prime, set_p):
            count += 1
    print count


if __name__ == '__main__':
    main()
