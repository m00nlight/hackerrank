from __future__ import division
from sys import stdin

def solve(n, m):
	if n <= 6:
		return (10 ** n - 1) // 9 % m
	else:
		if n % 2 == 0:
			tmp = solve(n // 2, m)
			return (tmp * pow(10, n // 2, m) + tmp) % m
		else:
			tmp = solve(n // 2, m)
			return ((tmp * pow(10, n // 2, m) + tmp) * 10  + 1) % m
	

if __name__ == '__main__':
	t = int(stdin.readline())
	for _ in range(t):
		a, b = map(int, stdin.readline().strip().split())
		print solve(a, b)
