from __future__ import division
from sys import stdin

mod = 10 ** 9 + 7

def gcd(a, b):
    """
    Type :: (Int, Int) -> Int
    Return :: Greatest Common divisor
    """
    while b is not 0:
        a, b = b, a % b
    return a

def exgcd(a, b):
    """
    Type :: (Int, Int) -> (Int, Int, Int)
    Return :: (g, x, y), g is gcd of a and b and
    x * a + y * b = g
    """
    if b is 0:
        return (a, 1, 0)
    else:
        g, x, y = exgcd(b, a % b)
        return (g, y, x - (a // b) * y)


def modinv(a, m):
    """
    Type :: (Int, Int) -> Int
    Return :: Return module inverse of a * x = 1 (mod m)
    """
    if gcd(a, m) is not 1: raise Exception("Not coprime")
    _, x, y = exgcd(a, m)
    return (m + x % m) % m

def solve(xs, ys, n):
    P , Q = 1, 1
    for i in range(n):
        for j in range(i + 1, n):
            P = P * (xs[i] - xs[j]) % mod
            P = P * (ys[i] - ys[j]) % mod
    for i in range(n):
        for j in range(n):
            Q = Q * (xs[i] + ys[j]) % mod

    return P * modinv(Q, mod) % mod

if __name__ == '__main__':
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        xs = map(int, stdin.readline().strip().split())
        ys = map(int, stdin.readline().strip().split())
        print solve(xs, ys, n)