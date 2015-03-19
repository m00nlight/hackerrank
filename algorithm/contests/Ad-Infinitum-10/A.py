from __future__ import division
from math import sqrt 

def solve(s1, s2, q, L):
    side = L * sqrt(2) - sqrt(2.0 * q)
    return side / abs(s2 - s1)
    
if __name__ == '__main__':
    L, s1, s2 = map(int, raw_input().strip().split())
    Q = int(raw_input())
    for _ in range(Q):
        q = int(raw_input())
        print '%.4lf' % solve(s1, s2, q, L)