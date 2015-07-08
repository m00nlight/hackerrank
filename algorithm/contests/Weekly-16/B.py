from __future__ import division
from sys import stdin
from collections import Counter, defaultdict
from itertools import groupby

def memo(f):
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except Exception:
            cache[args] = f(*args)
            return cache[args]
    return _f

mod = 10 ** 9  + 7

def preprocessing():
    four, five, six = [0] * 105, [0] * 105, [0] * 105
    base = 4
    for i in range(1, 101):
        four[i] = (four[i- 1] + base) % mod
        base = base * 10 % mod

    base = 5
    for i in range(1, 101):
        five[i] = (five[i - 1] + base) % mod
        base = base * 10 % mod

    base = 6
    for i in range(1, 101):
        six[i] = (six[i- 1] + base) % mod
        base = base * 10 % mod

    return (four, five, six)

four, five, six = preprocessing()

@memo
def solve(x, y, z, last_digit):
    if x == 0 and y == 0 and z == 0:
        return (1, 0)
    else:
        if last_digit == 4:
            if x > 0 and y == 0 and z == 0:
                return (1, four[x])
            elif x > 0:
                (n1, a1) = solve(x - 1, y, z, 4)
                (n2, a2) = solve(x - 1, y, z, 5)
                (n3, a3) = solve(x - 1, y, z, 6)
                nn = (n1 + n2 + n3) % mod
                aa = (a1 + a2 + a3) % mod
                return (nn, (aa * 10 + 4 * nn) % mod)
            else:
                return (0, 0)
        elif last_digit == 5:
            if y > 0 and x == 0 and z == 0:
                return (1, five[y])
            elif y > 0:
                (n1, a1) = solve(x, y - 1, z, 4)
                (n2, a2) = solve(x, y - 1, z, 5)
                (n3, a3) = solve(x, y - 1, z, 6)
                nn = (n1 + n2 + n3) % mod
                aa = (a1 + a2 + a3) % mod
                return (nn, (aa * 10 + 5 * nn) % mod)
            else:
                return (0, 0)
        else:
            if z > 0 and x == 0 and y == 0:
                return (1, six[z])
            elif z > 0:
                (n1, a1) = solve(x, y, z - 1, 4)
                (n2, a2) = solve(x, y, z - 1, 5)
                (n3, a3) = solve(x, y, z - 1, 6)
                nn = (n1 + n2 + n3) % mod
                aa = (a1 + a2 + a3) % mod
                return (nn, (aa * 10 + 6 * nn) % mod)
            else:
                return (0, 0)


if __name__ == '__main__':
    x, y, z = map(int, stdin.readline().strip().split())
    ans = 0
    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                for last_digit in [4,5,6]:
                    (nn, aa) = solve(i, j, k, last_digit)
                    #print 'i = %d j = %d k = %d last_digit = %d: (%d %d)' % (i, j, k, last_digit, nn, aa)
                    ans = (ans + aa) % mod

    print ans