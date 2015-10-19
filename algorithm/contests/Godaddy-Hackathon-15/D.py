from __future__ import division
from sys import stdin, maxint
from itertools import groupby
from collections import defaultdict

def solve(n, xs, ys, zs):
    xsmap = defaultdict(list)
    ysmap = defaultdict(list)
    zsmap = defaultdict(list)

    for idx, x in enumerate(xs):
        xsmap[x].append(idx + 1)

    for idx, y in enumerate(ys):
        ysmap[y].append(idx + 1)

    for idx, z in enumerate(zs):
        zsmap[z].append(idx + 1)


    ts = []

    for t in range(1, n + 1):
        for xidx in xsmap[t]:
            for yidx in ysmap[t]:
                for zidx in zsmap[t]:
                    ts.append((xidx, yidx, zidx, 1))

    ts = sorted(ts)

    ans = 0

    for i in range(len(ts)):
        for j in range(i):
            if ts[i][0] > ts[j][0] and ts[i][1] > ts[j][1] and ts[i][2] > ts[j][2]:
                ts[i] = (ts[i][0], ts[i][1], ts[i][2], max(ts[i][3], ts[j][3] + 1))
        ans = max(ans, ts[i][3])

    return ans

if __name__ == '__main__':
    tc = int(stdin.readline())
    for _ in range(tc):
        n = int(stdin.readline())
        xs = map(int, stdin.readline().strip().split())
        ys = map(int, stdin.readline().strip().split())
        zs = map(int, stdin.readline().strip().split())

        print(solve(n, xs, ys, zs))
