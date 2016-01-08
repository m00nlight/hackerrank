from __future__ import division
from sys import stdin


class UFSet:
    def __init__(self, size):
        self.fa = [i for i in range(size + 1)]
        self.size = [1] * (size + 1)

    def find(self, idx):
        if idx != self.fa[idx]:
            self.fa[idx] = self.find(self.fa[idx])

        return self.fa[idx]

    def query_size(self, idx):
        return self.size[self.find(idx)]

    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx != fy:
            self.size[fx] = self.size[fx] + self.size[fy]
            self.fa[fy] = fx


if __name__ == '__main__':
    n, q = map(int, stdin.readline().strip().split())
    ufset = UFSet(n)
    for _ in range(q):
        arr = stdin.readline().strip().split()
        if arr[0] == 'M':
            ufset.union(int(arr[1]), int(arr[2]))
        else:
            print(ufset.query_size(int(arr[1])))