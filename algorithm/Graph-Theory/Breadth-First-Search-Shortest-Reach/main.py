from __future__ import division
from sys import stdin, stdout
from collections import deque

def solve(n, edges, s):
    def build_graph(n, edges):
        graph = [[] for _ in range(n)]
        for (a, b) in edges:
            a, b = a - 1, b - 1
            graph[a].append(b)
            graph[b].append(a)
        return graph

    graph = build_graph(n, edges)
    dis , que = [-1] * n, deque()
    dis[s] = 0
    que.append(s)

    while que:
        node = que.popleft()
        for adj in graph[node]:
            if dis[adj] == -1:
                dis[adj] = dis[node] + 6
                que.append(adj)

    del dis[s]
    return dis


if __name__ == '__main__':
    t = int(stdin.readline())
    for _ in range(t):
        edges = []
        n, m = map(int, stdin.readline().strip().split())
        for _ in range(m):
            a, b = map(int, stdin.readline().strip().split())
            edges.append((a, b))
        s = int(stdin.readline())

        print ' '.join(map(str, solve(n, edges, s - 1)))