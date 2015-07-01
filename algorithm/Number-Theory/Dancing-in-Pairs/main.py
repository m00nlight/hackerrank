from __future__ import division
from collections import defaultdict, deque
from heapq import heappush, heappop
from sys import stdin
from math import sqrt

def sqrtInt(n):
    l, r = 1, n + 1
    while r - l > 1:
        mid = (l + r) // 2
        if mid * mid > n:
            r = mid
        else:
            l = mid
    return l

if __name__ == '__main__':
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        sq = sqrtInt(n)
        print 'odd' if sq % 2 == 1 else 'even'