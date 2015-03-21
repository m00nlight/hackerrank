from __future__ import division

def gcd(a, b):
    while b is not 0:
        a, b = b, a % b
    return a

def solve(a, b, c):
    g = gcd(a, b)
    if c % g == 0:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    t = int(raw_input())
    for _ in range(t):
        a, b, c = map(int, raw_input().strip().split())
        print solve(a, b, c)