from __future__ import division
from collections import defaultdict
from math import sqrt

def solve(n, k):
	nums = defaultdict(int)
	for i in range(1, k):
		nums[i] = n // k + (1 if n % k >= i else 0)

	nums[0] = n // k

	ret = 0
	for i in range(1, (k + 1) // 2):
		ret += nums[i] * nums[k - i]

	if k % 2 is 0: ret += nums[k // 2] * (nums[k // 2] - 1) // 2
	ret += nums[0] * (nums[0] - 1) // 2
	return ret


if __name__ == '__main__':
	t = input()
	for _ in range(t):
		n, k = map(int, raw_input().strip().split())
		print solve(n, k)