from __future__ import division

def solve(a, m):
    if a < m:
        return a * (a + 1) // 2
    else:
        return (m * (m - 1) // 2 * (a // m) + solve(a % m, m)) 

if __name__ == '__main__':
    t = int(raw_input())
    for _ in range(t):
        a, m = map(int, raw_input().strip().split())
        print solve(a, m)