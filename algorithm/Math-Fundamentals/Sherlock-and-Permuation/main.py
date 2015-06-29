from __future__ import division
from math import factorial
from sys import stdin

def solve(N, K):
    return factorial(N + K - 1) // factorial(N ) // factorial(K - 1)

if __name__ == '__main__':
    n = int(stdin.readline())
    for _ in range(n):
        N, K = map(int, stdin.readline().strip().split())
        print solve(N, K) % (10 ** 9 + 7)

