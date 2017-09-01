
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


def is_prime_v2(n, known_primes):
    """ I thought, the basis(composition) of every odd number must
        be a prime number. So if a prime can't divide it, no other odd can.
        Also, if we include 2 to list, no other number can.
        That list is precisely `known_primes`"""

    for prime in known_primes.values():

        if n % prime == 0:
            return False

    return True


def range_generator(start, stop, step=1):
    """ Just realized range() isn't a generator. Writing my own generator """
    val = start - step
    while val < stop:
        val += step
        yield val


if __name__ == '__main__':
    primes = {1: 2, 2: 3}
    max_n = 2
    t = int(raw_input().strip())
    # The approach got a little lamer here, so it passes test#1
    # To save unnecessary comparaisions, I am calculating the master list once,
    # and printing all given inputs (max 10^3) by reference.
    n = 10001
    if n < max_n:
        # print primes[n]
        pass
    else:
        latest = primes[max_n]
        for test_num in range_generator(latest + 2, 10**20, 2):
            if is_prime_v2(test_num, primes):
                primes.update({max_n + 1: test_num})
                max_n += 1
            if max_n == n:
                # print primes[max_n]
                break

    for _ in range(t):
        n = int(raw_input().strip())
        print primes[n]
