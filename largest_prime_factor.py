# coding=utf-8

import sys
primes = []
for i in range(1,10**6):
    for p in range(i-1,1,-1):
        if (i%p == 0):
            break
    else:
        primes.append(i)

print((primes), end=' ')
# print('\n')
# for i in range(2, len(primes)):
#     print(primes[i] - primes[i-1], end=' ')

def is_prime(n):

    # Divisibility rule check.
    # 2
    pass


