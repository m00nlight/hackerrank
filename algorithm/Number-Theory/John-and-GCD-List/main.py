from __future__ import division

def gcd(a, b):
    while b is not 0:
        a, b = b, a % b
        
    return a
    
def lcm(arg):
    return arg[0] * arg[1] // gcd(arg[0], arg[1])
    
def solve(arr):
    return map(lambda x: lcm(x), zip(arr + [1], [1] + arr))
    
if __name__ == '__main__':
    t = int(raw_input())
    for _ in range(t):
        _ = raw_input()
        arr = map(int, raw_input().strip().split())
        print ' '.join(map(str, solve(arr)))