from __future__ import division
from collections import defaultdict, deque

def toplogic(n, graph):
	indeg = defaultdict(int)
	outdeg = defaultdict(int)
	res = {}
	que = deque()

	for u in graph:
		for v in graph[u]:
			indeg[v] += 1
			outdeg[u] += 1

	for node in range(n):
		if indeg[node] == 0:
			que.append(node)
			res[node] = 1

	while que:
		node = que.popleft()
		for v in graph[node]:
			indeg[v] -= 1
			if indeg[v] == 0:
				que.append(v)
				res[v] = res[node] + 1

	ans = -1
	for node in range(n):
		if outdeg[node] == 0 and node in res and res[node] > ans:
			ans = res[node]

	if len(res) == n and ans != -1:
		return str(ans) + " semester(s)"
	else:
		return "Never Ends"

if __name__ == '__main__':
	t = int(raw_input())
	for case in range(t):
		graph = defaultdict(list)
		n, r = map(int, raw_input().strip().split())
		for _ in range(r):
			a, b = map(int, raw_input().strip().split())
			graph[b].append(a)

		print 'Case %d: %s' %(case + 1, toplogic(n, graph))



