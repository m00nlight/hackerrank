from __future__ import division 
import sys
from operator import mul


def h1(a, b):
	for i in range(a, b + 1):
		yield(i)

def solve(arr, a, b):
	ans = sys.maxint
	l = -1
	ret = (b, b)
	for i in h1(a, b):
		for j in h1(i, b):
			tmp = reduce(mul, arr[i:j + 1])
			if tmp < ans:
				ans, l = tmp, j - i + 1
				ret = (i, j)
			else:
				if tmp == ans and j - i + 1 > l:
					ret = (i, j)
					l = j - i + 1
				else:
					if j - i + 1 == l and i < ret[0]:
						ret = (i, j)

	return (ans,) + ret


if __name__ == '__main__':
	n, q = map(int, raw_input().strip().split())
	arr = map(int, raw_input().strip().split())
	for _ in range(q):
		op, a, b = map(int, raw_input().strip().split())
		if op == 2:
			arr[a - 1] = b
		else:
			v, l, r = solve(arr, a - 1, b - 1)
			print '%d %d %d' % (v, l + 1, r + 1)