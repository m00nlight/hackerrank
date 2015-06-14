from __future__ import division
from collections import defaultdict
from heapq import heappush, heappop

class UFSet:
	def __init__(self, n):
		self.fa = [i for i in range(n)]

	def find(self, idx):
		if self.fa[idx] == idx:
			return idx
		else:
			self.fa[idx] = self.find(self.fa[idx])
			return self.fa[idx]

	def union(self, x, y):
		fx = self.find(x)
		fy = self.find(y)
		self.fa[fx] = fy


def init():
	n, e, k = map(int, raw_input().strip().split())
	edge = []
	deg = defaultdict(int)

	for i in range(n - 1):
		a, b, w = map(int, raw_input().strip().split())
		edge.append((w, a - 1, b - 1, 1))
		deg[a - 1] , deg[b - 1] = deg[a - 1] + 1, deg[b - 1] + 1

	for i in range(e):
		a, b, w = map(int, raw_input().strip().split())
		edge.append((w, a - 1, b - 1, 2))

	return (n, k, deg, edge)

def kruscal(n, k, edges):
	uf = UFSet(n)
	res = []
	c1, c2 = 0, 0

	edges = sorted(edges)

	for (w, a, b, category) in sorted(edges):
		if c1 == n - 1: break
		fa, fb = uf.find(a), uf.find(b)
		if fa != fb:
			if category == 2:
				if c2 < k:
					c1, c2 = c1 + 1, c2 + 1
					res.append((w, a, b, category))
					uf.union(fa, fb)
				else:
					pass
			else:
				res.append((w, a, b, category))
				c1 += 1
				uf.union(fa, fb)

	return res

def build_graph(kru):
	graph = defaultdict(list)

	for (w, a, b, t) in kru:
		graph[a].append((b, w, t))
		graph[b].append((a, w, t))

	return graph

def solve(n, k, deg, graph):
	for i in range(n):
		if deg[i] == 1:
			graph[n].append((i, 0, 0))

	return dijkstra(n, k, graph)


def dijkstra(n, k, graph):
	cc = 0
	q, seen = [(0, n, 0, 0)], set()
	#print graph
	dis = defaultdict(int)
	while q:
		(cost, node, t, curcc) = heappop(q)

		if node not in seen:
			seen.add(node)
			dis[node] = cost

			for (v, weight, t) in graph[node]:
				if v not in seen:
					if t != 2:
						heappush(q, (cost + weight, v, t, curcc))
					else:
						if curcc < k:
							heappush(q, (cost + weight, v, t, curcc + 1))

	return dis


if __name__ == '__main__':
	n, k, deg, edges = init()
	#kru = kruscal(n, k, edges)
	graph = build_graph(edges)
	dis = solve(n, k, deg, graph)

	for i in range(n):
		print dis[i]
