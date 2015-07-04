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

def solve(d, k, h):
	if d == 1:
		return (k + 1) % mod
	else:
		return (pow(d, k + 1, mod) - 1) * modinv(d - 1, mod) % mod

if __name__ == '__main__':
	t = int(stdin.readline())
	for _ in range(t):
		d, k, h = map(int, stdin.readline().strip().split())
		print solve(d, k, h)