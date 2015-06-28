from __future__ import division
from collections import defaultdict, deque
from heapq import heappush, heappop
from sys import stdin

class UnionFindSet:
    def __init__(self, nodes):
        self.fa = {}
        for n in nodes:
            self.fa[n] = n

    def find(self, x):
        if self.fa[x] == x:
            return x
        else:
            self.fa[x] = self.find(self.fa[x])
            return self.fa[x]

    def union(self, x, y):
        fx = self.find(x)
        fy = self.find(y)
        if fx == fy:
            return fx
        else:
            self.fa[fx] = fy
            return fy


"""
Data definition:
graph is a hash
graph["nodes"] is a list of all nodes in the graph
graph["edges"] is a list of all edges in the graph in (x, y, w) form
  - x is the first nodes
  - y is the second nodes
  - w is the weight of the edges
graph["relation"] is the graph relation of the graph
"""

def kruscal(graph):
    "kruscal minimum spanning tree algorithm"
    ufset = UnionFindSet(graph["nodes"])

    ret = 0

    for (x, y, w) in sorted(graph["edges"], key = lambda x: x[-1]):
        fx = ufset.find(x)
        fy = ufset.find(y)
        if fx != fy:
            ret += w
            ufset.union(fx, fy)
        else:
            pass
    return ret


def dijkstra(graph, root):
    "dijkstra algorithm for single source shortest algorithm"
    dis, vis = {}, {}
    for n in graph["nodes"]:
        dis[n] = 10 ** 9
        vis[n] = False

    heap = []
    dis[root] = 0
    heappush(heap, (0, root))

    while heap:
        _, n = heappop(heap)
        vis[n] = True
        for (y, w) in graph["adj"][n]:
            if not vis[y] and dis[n] + w < dis[y]:
                dis[y] = dis[n] + w
                heappush(heap, (dis[y], y))

    return dis

def belmanFord(graph, root):
    "belman ford algorithm for graph with negative edges"
    dis = {}
    for n in graph["nodes"]:
        dis[n] = 10 ** 9

    dis[root] = 0

    # update for n - 1 times
    for _ in range(len(graph["nodes"]) - 1):
        for (x, y, w) in graph["edges"]:
            if dis[x] + w < dis[y]:
                dis[y] = dis[x] + w

    # try to find the component which can be reached by the source
    connect = set([root])
    que = deque([root])

    while que:
        n = que.popleft()
        for (y, _) in graph["adj"][n]:
            if not y in connect:
                connect.add(y)
                que.append(y)

    dis["negcicle"] = False
    for (x, y, w) in graph["edges"]:
        if dis[x] + w < dis[y] and x in connect:
            dis["negcicle"] = True

    dis["con"] = connect
    return dis

def floyd(graph):
    n = len(graph["nodes"])
    dis = [[10 ** 20 for _ in range(n)] for _ in range(n)]
    for i in range(n): dis[i][i] = 0

    for x in graph["nodes"]:
        for (y, w) in graph["adj"][x]:
            dis[x][y] = w


    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dis[i][k] < 10 ** 20 and dis[k][j] < 10 ** 20:
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

    return dis


if __name__ == '__main__':
    V, E= map(int, stdin.readline().strip().split())
    graph = {}
    graph["nodes"] = [i for i in range(V)]
    graph["edges"] = []
    graph["adj"] = defaultdict(list)
    for _ in range(E):
        x, y, w = map(int, stdin.readline().strip().split())
        graph["edges"].append((x, y, w))
        graph["adj"][x].append((y, w))

    dis = floyd(graph)

    negcycle = False

    for i in range(len(graph["nodes"])):
        if dis[i][i] < 0:
            negcycle = True

    if negcycle:
        print "NEGATIVE CYCLE"
    else:
        for row in dis:
            print ' '.join(map(lambda x: str(x) if x < 10 ** 20 else "INF", row))



