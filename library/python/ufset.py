from __future__ import division
from sys import stdin, maxint


class UFSet:
    def __init__(self, size):
        self.fa = [i for i in range(size + 1)]
        self.size = [1] * (size + 1)

    def find(self, idx):
        """ iterative path compression avoid python stack overflow"""
        fx = idx
        while fx != self.fa[fx]: fx = self.fa[fx]
        while idx != fx:
            fa, self.fa[idx] = self.fa[idx], fx
            idx = fa

        return self.fa[idx]

    def query_size(self, idx):
        return self.size[self.find(idx)]

    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx != fy:
            self.size[fx] = self.size[fx] + self.size[fy]
            self.fa[fy] = fx