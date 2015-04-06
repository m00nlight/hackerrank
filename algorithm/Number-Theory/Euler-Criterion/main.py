from __future__ import division

def solve(a, p):
    if p == 2 or a == 0:
        return 'YES'
    else:
        if pow(a, (p - 1) // 2, p) == 1:
            return 'YES'
        else:
            return 'NO'

if __name__ == '__main__':
    t = int(raw_input())
    for _ in range(t):
        a, p = map(int, raw_input().strip().split())
        print solve(a, p)