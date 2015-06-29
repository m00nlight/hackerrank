from __future__ import division
from math import factorial
from sys import stdin

def solve(a, b):
    seen = {}
    start, end = (None, None)
    for i in range(b + 1):
        rem = pow(2, i, b)
        if rem in seen:
            start, end = (seen[rem], i)
            break
        else:
            seen[rem] = i


    if start == 0:
        top = pow(2, a, end - start)
        return pow(2, top, b)
    else:
        top = start +  (pow(2, a) - start) % (end - start)
        return pow(2, top, b)

if __name__ == '__main__':
    a, b = map(int, stdin.readline().strip().split())
    print solve(a, b)