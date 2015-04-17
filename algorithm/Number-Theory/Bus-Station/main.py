from __future__ import division
from math import sqrt

def solve(arr):
	total = sum(arr)
	tmp = [[x, total // x] for x in range(1, int(sqrt(total) + 1)) if total % x == 0]
	divisors = set([item for x in tmp for item in x])
	
	def judge(n):
		acc = 0
		for a in arr:
			if acc + a < n:
				acc += a
			elif acc + a == n:
				acc = 0
			else:
				return False
		return True

	ret = []
	for d in divisors:
		if judge(d): ret.append(d)

	return sorted(ret)

if __name__ == '__main__':
	n = input()
	arr = map(int, raw_input().strip().split())
	print ' '.join(map(str, solve(arr)))
