# coding=utf-8

def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
     return s

power(5, 3)