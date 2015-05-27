
from __future__ import division


def solve(n, lhs):
    maxn = 300001
    seg = [(0, 0, 0, 0) for _ in range(5 * maxn + 10)]
    def build(l, r, num):
        mid = (l + r) // 2
        seg[num] = (l, r, mid, 0)
        if l + 1 != r:
            build(l, mid, 2 * num)
            build(mid, r, 2 * num + 1)

    def insert(l, r, num):
        left, right, mid, cover = seg[num]
        if l == left and r == right:
            seg[num] = (left, right, mid, cover + 1)
            return

        if r <= mid:
            insert(l, r, num * 2)
        elif l >= mid:
            insert(l, r, num * 2 + 1)
        else:
            insert(l, mid, num * 2)
            insert(mid, r, num * 2 + 1)

    def query(idx):
        ret, num = 0, 1
        while seg[num][0] != idx or seg[num][1] != idx + 1:
            ret += seg[num][-1]
            if idx < seg[num][-2]:
                num = num * 2
            else:
                num = num * 2 + 1
        ret += seg[num][-1]
        return ret

    build(0, maxn, 1)

    for (l, h) in lhs:
        insert(l, h + 1, 1)


    for i in range(n, -1, -1):
        if query(i) >= i:
            return i
    return 0


if __name__ == '__main__':
    n = int(raw_input())
    lhs = []
    for _ in range(n):
        l, h = map(int, raw_input().strip().split())
        lhs.append((l + 1,h + 1))

    print solve(n, lhs)
