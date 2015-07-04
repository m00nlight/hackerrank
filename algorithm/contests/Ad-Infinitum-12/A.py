from __future__ import division
from sys import stdin

def solve(arr, n):
	return (-1) * arr[-2] // arr[-1], ((-1) ** n) * arr[0] // arr[-1]


if __name__ == '__main__':
	n = int(stdin.readline())
	arr = map(int, stdin.readline().strip().split())
	print ' '.join(map(str, solve(arr, n)))