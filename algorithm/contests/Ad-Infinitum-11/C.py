from __future__ import division
from math import sqrt, ceil

def gcd(a, b):
    while b is not 0:
        a, b = b, a % b
    return a

def exgcd(a, b):
    if b is 0:
        return (a, 1, 0)
    else:
        g, x, y = exgcd(b, a % b)
        return (g, y, x - (a // b) * y)


def modinv(a, m):
    if gcd(a, m) is not 1: raise Exception("Not coprime")
    _, x, y = exgcd(a, m)
    return (m + x % m) % m

def baby_step(a, b, g):
    """
    Baby Step Giant step :: calculate a^x == b (mod g) for gcd(a, g) == 1
    Type :: (Int, Int, Int) -> Int
    Return :: Return minimum positive x for a^x == b (mod g)
    """
    q = int(g ** 0.5) + 1
    aq = pow(a, q, g)
    ai = modinv(a, g)

    assert a * ai % g == 1

    l = map(lambda i: pow(aq, i, g), xrange(q + 1))
    r = map(lambda i: (b * pow(ai, i, g)) % g, xrange(q + 1))
    xs = set()
    for y in set(l) & set(r):
        i = l.index(y)
        j = r.index(y)
        xs.add(i * q + j)

    if not xs:
        return -1
    x = min(xs)
    assert pow(a, x, g) == b
    return x

if __name__ == '__main__':
    t = input()
    for _ in range(t):
        a, b, g = map(int, raw_input().strip().split())
        print baby_step(a, b, g)