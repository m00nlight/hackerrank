from __future__ import division
from sys import stdin


mod = 10 ** 9 + 7

def solve(n):
	return pow(2, n - 1, mod)

if __name__ == '__main__':
	t = int(stdin.readline())
	for _ in range(t):
		n = int(stdin.readline())
		print solve(n)