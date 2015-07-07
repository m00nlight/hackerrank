from __future__ import division
from sys import stdin

def solve(arr, qs):
    ret = []
    acc = [0]
    for a in arr:
        acc.append(acc[-1] + a)

    for (l, r) in qs:
        if abs(acc[r] - acc[l - 1]) % 2 == 1:
            ret.append('Odd')
        else:
            ret.append('Even')
    return ret

if __name__ == '__main__':
    N, Q = map(int, stdin.readline().strip().split())
    qs = []
    arr = map(int, stdin.readline().strip().split())
    for _ in range(Q):
        a, b = map(int, stdin.readline().strip().split())
        qs.append((a, b))

    print '\n'.join(solve(arr, qs))