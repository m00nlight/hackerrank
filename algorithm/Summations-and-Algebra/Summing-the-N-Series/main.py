from __future__ import division

MOD = 10 ** 9 + 7

def solve(n):
    return (n ** 2) % MOD

if __name__ == '__main__':
    t = int(raw_input())
    for _ in range(t):
        n = int(raw_input())
        print solve(n)