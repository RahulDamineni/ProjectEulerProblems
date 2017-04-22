# coding=utf-8

def is_prime(n):
    """"pre-condition: n is a nonnegative integer
    post-condition: return True if n is prime and False otherwise."""
    if n < 2:
         return False;
    if n % 2 == 0:
         return n == 2  # return False
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    return True

def smallest_multiple(t):
    """ Returns smallest multiple of t | t <= 40 """
    for prime in range(2, t):
        if not (t % prime):
            return prime
    return t

if __name__ == '__main__':
    terms = {1: 1}
    n = 6700
    t = 1
    ret = terms[t]
    for i in range(2, n+1):
        if terms[i-1] % i != 0:
            if is_prime(i):
                ret *= i
            else:
                ret *= smallest_multiple(i)
        terms.update({i: ret})
    print ret


# # Sequence generator
# if __name__ == '__main__':
#     for i in range(2, 100):
#         flag = True
#         num = 1
#         while True:
#             for div in range(1, i+1):
#                 if num % div != 0:
#                     break
#             else:
#                 print "For %d to %d, largest N is %d" % (1, i, num)
#                 break
#
#             num += 1

