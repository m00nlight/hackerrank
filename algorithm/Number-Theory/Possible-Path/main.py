from __future__ import division

def gcd(a, b):
    while b is not 0:
        a, b = b, a % b
    return a

def solve(a, b, c, d):
    if gcd(a, b) == gcd(c, d):
        return True
    return False
    
if __name__ == '__main__':
    t = int(raw_input())
    for _ in range(t):
        a, b, c, d = map(int , raw_input().strip().split())
        if solve(a, b, c, d):
            print 'YES'
        else:
            print 'NO'