from __future__ import division

def prop_mod(a, m):
    return (a % m + m) % m

def exgcd(a, b):
    if b is 0:
        return (a, 1, 0)
    else:
        g, x, y = exgcd(b, a % b)
        return (g, y, x - (a // b) * y)


def power_mod(a, b, m):
    if b is 0:
        return 1
    else:
        tmp = power_mod(a, b // 2, m)
        return tmp * tmp % m if b % 2 is 0 else tmp * tmp * a % m

def modinv(a, m):
    if exgcd(a, m)[0] is not 1: raise Exception("Not coprime")
    _, x, y = exgcd(a, m)
    return (m + x % m) % m

def power_series(base, n, m):
    "return (base^0 + base^1 + ... + base^n) mod m"
    if n is 0:
        return 1
    elif n is 1:
        return (1 + base) % m
    else:
        ret = power_series(base, (n - 1) // 2, m)
        tmp = power_mod(base, (n + 1) // 2, m)
        if n % 2 is 0:
            return (ret * (1 + tmp) % m + power_mod(base, n, m)) % m
        else:
            return (ret * (1 + tmp)) % m

def solve(a, n, m):
    l = len(str(a))
    base = 10 ** l
    return a * power_series(base, n - 1, m) % m

if __name__ == '__main__':
    n = int(raw_input())
    for _ in range(n):
        a, n, m = map(int, raw_input().strip().split())
        print solve(a, n, m)