from __future__ import division
from operator import add, mul

def mod(a, b):
    return (a % b + b) % b

def gcd(a, b):
    while b is not 0:
        a, b = b, a % b
    return a

def exgcd(a, b):
    if b is 0:
        return (a, 1, 0)
    else:
        g, x, y = exgcd(b, a % b)
        return (g, y, x - (a // b) * y)


def modinv(a, m):
    if gcd(a, m) is not 1: raise Exception("Not coprime")
    _, x, y = exgcd(a, m)
    return (m + x % m) % m


def sieve(m):
    ret, judge = [], [True] * (m + 1)
    judge[0] = judge[1] = False
    ret.append(2)
    for i in range(4, m + 1, 2): judge[i] = False
    for i in range(3, m + 1, 2):
        if judge[i]:
            ret.append(i)
            for j in range(i * i, m + 1, i): judge[j] = False
    return ret


MAXN = 1450

primes = sieve(MAXN)
primes_set = set(primes)

def factor(n):
    
    if n is 0: raise Exception("Should be nonzero number")
    
    ret, i = [], 0
    while n is not 1 and i < len(primes):
        if n % primes[i] == 0:
            c = 0
            while n % primes[i] == 0:
                c += 1
                n //= primes[i]
            ret.append((primes[i], c))
        i += 1
    if n is not 1: ret.append((n, 1))
    return ret

def is_prime(n):
    if n in primes_set: return True
    elif n < primes[-1]: return False   

    for x in primes_set:
        if n % x == 0:
            return False
    return True

def init():
    ret = [0, 1, 2]
    for i in range(3, 2000005):
        if is_prime(i):
            ret.append(i)
        else:
            for x in primes:
                if i % x == 0:
                    ret.append(x + ret[i // x])
                    break
    return ret


if __name__ == '__main__':
    lookup = init()
    t = input()
    ans = 0
    arr = []
    for _ in range(t): arr.append(int(raw_input()))
    for n in arr: ans += lookup[n]
    
    print ans