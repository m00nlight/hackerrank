from __future__ import division
from sys import stdin

def solve(n):
    ret = []
    if (n % 2 == 0):
        for i in range(n // 2, 0, -1):
            ret.append(i)
            ret.append(n + 1 - i)
    else:
        ret.append((n + 1) // 2)
        for i in range(n // 2, 0, -1):
            ret.append(i)
            ret.append(n + 1 - i)

    return ret

if __name__ == '__main__':
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        print(' '.join(map(str, solve(n))))
