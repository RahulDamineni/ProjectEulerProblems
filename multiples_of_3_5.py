# # coding=utf-8
#
# if __name__ == '__main__':
#     su =0
#     for i in range(100):
#         if (i%3 == 0) and (i%5 == 0):
#             su = su+i;
#             print(i, end=' ')
#     print(su)

# !/bin/python3

import sys

t = int(input().strip())


def closest_multiple_N(n, p, q=1):
    for i in range(n, 0, -1):
        if (i % p == 0) and (i % q == 0):
            return int(i)
    else:
        return int(0)


for a0 in range(t):
    n = int(input().strip())
    last_term_5ap = closest_multiple_N(n-1, 5)
    last_term_3ap = closest_multiple_N(n-1, 3)
    last_term_35ap = closest_multiple_N(n-1, 5, 3)
    n3 = int(last_term_3ap / 3);
    n5 = int(last_term_5ap / 5);
    n35 = int(last_term_35ap / 15);
    print(n3, n5, n35)
    print(int((3 * (n3 ** 2 + n3) / 2) + (5 * (n5 ** 2 + n5) / 2) - (15 * (n35 ** 2 + n35) / 2)))