from __future__ import division
from sys import stdin

MOD = 10 ** 9 + 7

def solve(n):
	top = (pow(2, n, MOD - 1) - n + (MOD - 1)) % (MOD - 1)
	return pow(2, top, MOD)

if __name__ == '__main__':
	n = int(stdin.readline())
	for _ in range(n):
		n = int(stdin.readline())
		print solve(n)
