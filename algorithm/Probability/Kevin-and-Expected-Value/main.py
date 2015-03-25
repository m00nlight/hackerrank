from __future__ import division
from math import sqrt

MAXN = 5000010
def y(x):
    if abs(x) <= 1e-5:
        return 0
    else:
        return 0.5 + 0.5 * sqrt(1 + 4 * x)

def integrate(a, b):
    a1 = 0.5 * (b - a + 1)
    f = lambda x: 2 * (x ** 1.5) / 3 + sqrt(x) / 4 + sqrt(1 / x) / 64 - \
        ((1 / x) ** 1.5) / 1536
    return a1 + f(b + 1) - f(a)

if __name__ == '__main__':
    t = int(raw_input())
    res = [y(x) for x in range(MAXN)]
    acc = [0.0] * MAXN
    for i in range(1, MAXN):
        acc[i] = acc[i - 1] + res[i]

    for _ in range(t):
        n = int(raw_input())
        if n < MAXN:
            print (acc[n - 1] / n)
        else:
            print '%.5lf' % ((acc[MAXN - 1] + integrate(MAXN, n)) / n)