# -*- encoding: utf-8

from __future__ import division

def power_mod(a, b, m):
    if b == 0:
        return 1
    elif b == 1:
        return a % m
    else:
        tmp = power_mod(a, b // 2, m)
        return tmp * tmp % m if b % 2 == 0 else tmp * tmp * a % m
        


if __name__ == '__main__':
    t = int(raw_input())
    MOD = 1000000007
    for _ in range(t):
        a, b = map(int, raw_input().strip().split())
        # since b is extremely large, we need to use the Fermat's little 
        # theorem to accelerate the computation, since MOD is a prime
        # from Fermat's little theorem, we know that a^(p-1) = 1 (mod p)
        # for any prime number p and integer a
        b = b % (MOD - 1)
        print '%d' % power_mod(a, b, MOD)