from __future__ import division


def solve(n):
    x, y = 0, n
    ret = []
    while x < y:
        ret.append([x, y])
        ret.append([y, x])
        x, y = x + 1, y - 1
    if x == y: ret.append([x, y])
    return ret

if __name__ == '__main__':
    t = input()
    for _ in range(t):
        n = input()
        res = solve(n)
        for x in res:
            print ' '.join(map(str, x))