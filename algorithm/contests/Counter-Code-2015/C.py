from __future__ import division
from sys import stdin

def solve(n, m):
    if n % 2 == 0:
        if m % n == 0:
            return n // 2 + 1
        elif m % n % 2 == 1:
            return (m % n + 1) // 2
        else:
            return n + 1 - m % n // 2
    else:
        idx = m % (2 * n)
        if idx == 0:
            return (n + 1) // 2
        else:
            if idx <= (n + 1):
                if idx == n:
                    return (n + 1) // 2
                elif idx == n + 1:
                    return n
                else:
                    if idx % 2 == 1:
                        return (idx + 1) // 2
                    else:
                        return (n + 1 - idx // 2)
            else:
                idx = idx - (n + 1)
                if idx % 2 == 1:
                    return (idx + 1) // 2
                else:
                    return (n  - idx // 2)

        

if __name__ == '__main__':
    t = int(stdin.readline())
    for _ in range(t):
        n, m = map(int, stdin.readline().strip().split())
        ans = solve(n, m)
        print(str(ans) + ' ' + str(m // n - (1 if m % n == 0 else 0)))