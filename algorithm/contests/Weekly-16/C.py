from __future__ import division
from sys import stdin

def get_min_max(pos, n):
    mink = max(pos[0] - 1, n - pos[-1])
    maxk = max(pos[-1] - 1, n - pos[0])
    l = [-1] * (n + 1)
    for i in range(len(pos) - 1):
        mink = max(mink, (pos[i + 1] - pos[i]) // 2)
        maxk = min(maxk, max(pos[i + 1] - 1, n - pos[i + 1]))
        for j in range(pos[i], pos[i + 1]):
            l[j] = pos[i]

    for j in range(pos[-1], n + 1):
        l[j] = pos[-1]

    return mink, maxk, l

def greedy(expand, l, n):
    idx = 1
    nodes = []
    while idx <= n:
        nx = l[min(idx + expand, n)]
        nodes.append(nx)
        idx = nx + expand + 1

    return nodes

def solve(n, m, s, q, pos):
    mink, maxk, l = get_min_max(pos, n)
    cost = 10 ** 10
    install = []
    best_expand = -1

    for expand in range(mink, maxk + 1):
        ns = greedy(expand, l, n)
        if s * len(ns) + q * expand < cost:
            cost = s * len(ns) + q * expand
            install, best_expand = ns, expand

    print str(len(install)) + ' ' + str(best_expand)
    print ' '.join(map(str, install))

if __name__ == '__main__':
    t = int(stdin.readline())
    for _ in range(t):
        n, m, s, q = map(int, stdin.readline().strip().split())
        pos = map(int, stdin.readline().strip().split())
        solve(n, m, s, q, pos)