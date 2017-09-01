#!/bin/python

import sys


def is_prime(n):
    """Returns True if n is prime."""
    """ Based on fact that primes are of 6k + 1 or 6k - 1 """
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True


def range_generator(start, stop, step=1):
    """ Just realized range() isn't a generator. Quickly writing my own generator """
    val = start - step
    while val < stop:
        val += step
        yield val


if __name__ == '__main__':
    primes = {1: 2, 2: 3}
    max_n = 2
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n = int(raw_input().strip())
        if n < max_n:
            print primes[n]
        else:
            latest = primes[max_n]
            for test_num in range_generator(latest + 2, 10**20, 2):
                if is_prime(test_num):
                    primes.update({max_n + 1: test_num})
                    max_n += 1
                if max_n == n:
                    print primes[max_n]
                    break
