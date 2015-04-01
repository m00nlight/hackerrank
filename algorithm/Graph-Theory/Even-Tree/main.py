from __future__ import division
from collections import deque

MAXN = 105

def build_graph(edges):
    graph = [[] for _ in range(MAXN)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    return graph
    
def count_node(graph, a, b):
    def helper(x, y):
        vis = [False] * MAXN
        vis[y] = True
        que = deque()
        
        que.append(x)
        vis[x] = True
        count = 1
        while que:
            node = que.popleft()
            for v in graph[node]:
                if not vis[v]: 
                    que.append(v)
                    count += 1
                    vis[v] = True
        return count
        
    return (helper(a, b), helper(b, a))
    
def solve(graph, edges):
    ret = 0
    for a, b in edges:
        n1, n2 = count_node(graph, a, b)
        if n1 % 2 is 0 and n2 % 2 is 0:
            ret += 1
    return ret
    
if __name__ == '__main__':
    n, m = map(int, raw_input().strip().split())
    edges = []
    for _ in range(m):
        a, b = map(int, raw_input().strip().split())
        edges.append((a, b))
    
    graph = build_graph(edges)
    print solve(graph, edges)