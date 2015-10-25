from __future__ import division
from math import pi, sin, cos, sqrt
from sys import stdin, exit
from collections import defaultdict
from random import randint

mmod = 1234567891

def mod(a, b):
    """
    Type :: (Int, Int) -> Int
    Return modulo of a over b, make sure to return an positive number
    when b is great than zero
    """
    return (a % b + b) % b

def gcd(a, b):
    """
    Type :: (Int, Int) -> Int
    Return :: Greatest Common divisor
    """
    while b is not 0:
        a, b = b, a % b
    return a

def exgcd(a, b):
    """
    Type :: (Int, Int) -> (Int, Int, Int)
    Return :: (g, x, y), g is gcd of a and b and
    x * a + y * b = g
    """
    if b is 0:
        return (a, 1, 0)
    else:
        g, x, y = exgcd(b, a % b)
        return (g, y, x - (a // b) * y)


def modinv(a, m):
    """
    Type :: (Int, Int) -> Int
    Return :: Return module inverse of a * x = 1 (mod m)
    """
    if gcd(a, m) is not 1: raise Exception("Not coprime")
    _, x, y = exgcd(a, m)
    return (m + x % m) % m


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


MAXN = 400

primes = sieve(MAXN)
primes_set = set(primes)

def factor(n):
    """
    Type :: Int -> [(Int, Int)]
    Return the factorizatoin result of decompose number n
    >>> factor(12)
    [(2, 2), (3, 1)]

    >>> factor(10007)
    [(10007, 1)]
    
    >>> factor(0)
    Traceback (most recent call last):
        ...
    Exception: Should be nonzero number
    """
    
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

def all_divisor(n):
    ret = []
    for i in xrange(2, int(sqrt(n) + 1)):
        if n % i == 0:
            ret.append(i)
            if n // i != i:
                ret.append(n // i)
    ret.append(n)
    return ret

divisor_table = [[]] + [all_divisor(i) for i in range(1, 100001)]

def preprocess(xs):
    divisor_count = defaultdict(int)
    for x in xs:
        divisors = divisor_table[x]
        for d in divisors:
            divisor_count[d] += 1

    return divisor_count


def solve(xs, bs):
    cc = preprocess(xs)
    #print(cc)
    for p in cc:
        cc[p] = cc[p] * (cc[p] - 1) // 2

    #print(cc)
    for p in sorted(cc.keys())[::-1]:
        divisors = divisor_table[p]
        for d in divisors:
            if d != p:
                cc[d] -= cc[p]
    
    count, ans = 0, 0

    #print(cc)

    def calc_bs(x):
        ret = 0
        for k in range(len(bs)):
            ret = ret + bs[k] * pow(x, k, mmod)
            ret = ret % mmod
        return ret

    for p in cc:
        ans = ans + calc_bs(p) * cc[p]
        ans = ans % mmod
        count += cc[p]

    l = len(xs) * (len(xs) - 1) // 2 - count

    #print('l = %d' % l)
    ans = ans + calc_bs(1) * l
    return ans % mmod

def solve_naive(xs, bs):
    ret = 0
    for i in range(len(xs)):
        for j in range(i + 1, len(xs)):
            g = gcd(xs[i], xs[j])
            for k in range(len(bs)):
                ret = ret + pow(g, k, mmod) * bs[k]
                ret = mod(ret, mmod)
    return ret

def generate(n, m):
    xs = []
    ys = []
    for _ in range(n):
        xs.append(randint(1, 200))

    for _ in range(m):
        ys.append(randint(-10, 10))

    ys.append(1)
    return (xs, ys)

if __name__ == '__main__':
    n, m = map(int, stdin.readline().strip().split())
    xs = map(int, stdin.readline().strip().split())
    bs = map(int, stdin.readline().strip().split())
    res = solve(xs, bs)
    print(res)

    # res = solve([6, 8, 1, 8, 3], [-2, -2, 0, -6,  1])
    # print('res = %d' % res)

    # for _ in range(100):
    #     xs, bs = generate(100, 20)
    #     res1 = solve(xs, bs)
    #     res2 = solve_naive(xs, bs)
    #     if res1 == res2:
    #         print('one test pass')
    #     else:
    #         print(xs)
    #         print(bs)
    #         print('res1 = %d res_naive = %d' % (res1, res2))
    #         exit(-1)
