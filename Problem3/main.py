# coding=utf-8

# Finds largest prime factor of a given number


def is_prime(number):
    """ Checks if a number is prime """
    "It uses the fact that a prime (except 2 and 3) is of"
    " form 6k - 1 or 6k + 1 and looks only at divisors of this form"
    "Developed by Alexandru"
    if round(number) != number:
        return False
    if number == 2:
        return True
    if number == 3:
        return True
    if number % 2 == 0:
        return False
    if number % 3 == 0:
        return False
    m = 5
    w = 2
    while m * m <= number:
        if number % m == 0:
            return False
        m += w
        w = 6 - w
    return True


no_of_cases = int(raw_input().strip())
for _ in range(no_of_cases):
    n = int(raw_input().strip())

    prime = 40
    even = 2.
    odd = 1.
    if n % 2 == 0:
        while not is_prime(prime):
            prime = n / even
            even += 2
    else:
        while not is_prime(prime):
            prime = n / odd
            odd += 2
    print int(prime)

