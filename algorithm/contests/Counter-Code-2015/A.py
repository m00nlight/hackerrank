from __future__ import division
from sys import stdin

def work(n, sniper):
	sniper = sorted(sniper)
	ret = set(sniper)
	minValue, maxValue = sniper[0], sniper[-1]

	for i in xrange(minValue, 0, -1):
		if (not i in ret) and (not (i + 1) in ret):
			ret.add(i)

	for i in xrange(maxValue, n + 1):
		if (not i in ret) and (not (i - 1) in ret):
			ret.add(i)

	for i in xrange(minValue + 1, maxValue):
		if (not i in ret) and (not (i - 1) in ret) and (not (i + 1) in ret):
			ret.add(i)

	return len(ret)

if __name__ == '__main__':
	n, k = map(int, stdin.readline().strip().split())
	arr = map(int, stdin.readline().strip().split())
	print(work(n, arr))
