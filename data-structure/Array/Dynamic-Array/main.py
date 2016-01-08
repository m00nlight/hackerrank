from __future__ import division
from sys import stdin

def solve(n, q, infos):
    lastans = 0
    data = [[] for _ in range(n)]
    ret = []
    for (op, x, y) in infos:
        if op == 1:
            data[(x^lastans) % n].append(y)
        else:
            x = (x^lastans) % n
            lastans = data[x][y % len(data[x])]
            ret.append(data[x][y % len(data[x])])

    return ret

if __name__ == '__main__':
    n, q = map(int, stdin.readline().strip().split())
    infos = []
    for _ in range(q):
        op, x, y = map(int, stdin.readline().strip().split())
        infos.append((op, x, y))

    result = solve(n, q, infos)
    print('\n'.join(map(str, result)))
