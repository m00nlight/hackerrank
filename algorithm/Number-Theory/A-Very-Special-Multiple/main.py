from __future__ import division
from math import sqrt

def sieve(m):
    """
    Type :: Int -> [Int]
    Generate primes number up to m, and return a list
    """
    ret, judge = [], [True] * (m + 1)
    judge[0] = judge[1] = False
    ret.append(2)
    for i in range(4, m + 1, 2): judge[i] = False
    for i in range(3, m + 1, 2):
        if judge[i]:
            ret.append(i)
            for j in range(i * i, m + 1, i): judge[j] = False
    return ret


MAXN = 10**6

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

def euler_phi(n):
    facts = factor(n)
    return reduce(lambda acc, x: acc * (x[0] - 1) // x[0], facts, n)

def divisor(n):
    ret = set()
    for d in range(1, int(sqrt(n)) + 1):
        if n % d == 0:
            ret.add(d)
            ret.add(n // d)

    return sorted(list(ret))

def f1(n):
    if n % 4 == 0:
        return f2(n // 4)
    elif n % 2 == 0:
        return f2(n // 2)
    else:
        return f2(n)

def f2(n):
    a = b = 0
    while n % 2 == 0:
        n = n // 2
        a += 1

    while n % 5 == 0:
        n = n // 5
        b += 1

    return f3(n), max(a, b)

def f3(n):
    n = n * 9
    for d in divisor(euler_phi(n)):
        if pow(10, d, n) == 1:
            return d

if __name__ == '__main__':
    n = int(raw_input())
    for _ in range(n):
        num = int(raw_input())
        a, b = f1(num)
        print 2 * a + b