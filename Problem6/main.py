# coding=utf-8

for _ in range(int(raw_input())):
    n = int(raw_input().strip())
    sum_till_n = int(n * (n + 1) * 0.5)
    sum_of_squares = (n * (n + 1) * (2*n + 1)) / 6
    print (sum_till_n**2) - sum_of_squares


