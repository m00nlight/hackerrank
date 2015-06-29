from __future__ import division
from math import factorial
from sys import stdin

def solve(N, K):
    return factorial(N + K - 1) // factorial(N - 1) // factorial(K)

if __name__ == '__main__':
    n = int(stdin.readline())
    for _ in range(n):
        N = int(stdin.readline())
        K = int(stdin.readline())
        print solve(N, K) % (10 ** 9)