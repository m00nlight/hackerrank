from __future__ import division
from sys import stdin, stdout

def solve(n, m, ops):
    track = [0] * (n + 2)
    for (a, b, k) in ops:
        track[a], track[b + 1] = track[a] + k, track[b + 1] - k

    ans, x = 0, 0
    for i in range(1, n + 1):
        x = x + track[i]
        ans = max(ans, x)

    return ans

if __name__ == '__main__':
    n, m = map(int, stdin.readline().strip().split())
    ops = []
    for _ in range(m):
        a, b, k = map(int, stdin.readline().strip().split())
        ops.append((a, b, k))

    print(solve(n, m, ops))