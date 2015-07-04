from __future__ import division
from sys import stdin
from math import sqrt

mod = 10 ** 9 + 7

def euler(n):
	ret = n
	for i in range(2, n + 1):
		if n % i == 0:
			ret = ret // i * (i - 1)
			while (n % i) == 0: n //= i
	if n > 1: ret = ret // n * (n - 1)
	return ret

def gcd(a, b):
    """
    Type :: (Int, Int) -> Int
    Return :: Greatest Common divisor
    """
    while b != 0:
        a, b = b, a % b
    return a

def exgcd(a, b):
    """
    Type :: (Int, Int) -> (Int, Int, Int)
    Return :: (g, x, y), g is gcd of a and b and
    x * a + y * b = g
    """
    if b == 0:
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

def solve(n, c):
	ret, i = 0, 1
	while i * i < n:
		if n % i == 0:
			ret = (ret + euler(n // i) * pow(c, i - 1, mod)) % mod
			ret = (ret + euler(i) * pow(c, n // i - 1, mod)) % mod
		i += 1
	if i * i == n:
		ret = (ret + euler(i) * pow(c, i - 1, mod)) % mod
	return ret

def solve2(n, c):
	if n == 0: return 0;
	ret = 0
	for i in range(1, n + 1):
		ret += pow(c, gcd(n, i), mod)
		ret %= mod

	return ret * modinv(n, mod) % mod


if __name__ == '__main__':
	n, c = map(int, stdin.readline().strip().split())
	print solve2(n, c)