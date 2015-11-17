from __future__ import division
from sys import stdin
import cmath
import math

"""
This problem can be formalized with the following mathematica formula follow 
the following link:

https://en.wikipedia.org/wiki/Trace_%28linear_algebra%29#Eigenvalue_relationships

    x1 + x2 + x3 + ... + xn = a1 + b1 * 1j
    x1^2 + x2^2 + x3^3 + ... + xn^2 = a2 + b2 * 1j
    x1^3 + x2^3 + x3^3 + ... + xn^3 = a3 + b3 * 1j
                ......
    x1^(m-1) + x2^(m - 1) + ... + xn^(m - 1) = am-1 + bm-1 * 1j
    x1^m + x2^m + x3^m + ... + xn^m = n

What we need to solve is to find one solution(if there are multiple) for 
the above formulas.

"""
def solve(coefs, n, m):
    for i in range(m):
        base = cmath.exp(2 * math.pi * i / m * 1j)
        val = 0.0 + 0.0 * 1j
        for (j, coef) in enumerate(coefs):
            val = val + coef * cmath.exp(-2 * math.pi * i * j / m * 1j)
        count = int(round(val.real)) // m
        for _ in xrange(count):
            print('%.9f %.9f' % (base.real, base.imag))

if __name__ == '__main__':
    n, m = map(int, stdin.readline().strip().split())
    coefs = []
    for _ in range(m):
        a, b = map(float, stdin.readline().strip().split())
        coefs.append(a + b * 1j)

    solve(coefs, n, m)