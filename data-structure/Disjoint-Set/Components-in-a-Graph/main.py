from __future__ import division
from sys import stdin, maxint


class UFSet:
	def __init__(self, size):
		self.fa = [i for i in range(size + 1)]
		self.size = [1] * (size + 1)

	def find(self, idx):
		fx = idx
		while fx != self.fa[fx]: fx = self.fa[fx]
		while idx != fx:
			fa, self.fa[idx] = self.fa[idx], fx
			idx = fa

		return self.fa[idx]

	def query_size(self, idx):
		return self.size[self.find(idx)]

	def union(self, x, y):
		fx, fy = self.find(x), self.find(y)
		if fx != fy:
			self.size[fx] = self.size[fx] + self.size[fy]
			self.fa[fy] = fx


if __name__ == '__main__':
	n = int(stdin.readline())
	ufset = UFSet(2 * n)

	for _ in range(n):
		g, b = map(int, stdin.readline().strip().split())
		ufset.union(g, b)

	mi, mx = maxint, -maxint - 1

	for i in range(1, n + 1):
		size = ufset.query_size(i)
		if size is not 1:
			mi, mx = min(mi, size), max(mx, size)

	print('%d %d' % (mi, mx))