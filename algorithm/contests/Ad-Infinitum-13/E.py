from __future__ import division
from math import pi, sin, cos
from sys import stdin
from collections import defaultdict
from copy import copy

mmod = 1000000007

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper

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


MAXN = 1010

primes = sieve(MAXN)
primes_set = set(primes)


def factor_all(n):
    ret = [None for _ in xrange(n + 1)]
    ret[1] = []
    ret[2] = [(2, 1)]
    ret[3] = [(3, 1)]
    ret[4] = [(2, 2)]
    ret[5] = [(5, 1)]

    for i in range(6, n + 1):
        is_prime_flag = True
        tmp = None
        for p in primes:
            if i % p == 0:
                is_prime_flag = False
                tmp = ret[i // p][0:]
                j = 0
                while j < len(tmp) and tmp[j][0] < p:
                    j += 1
                if j < len(tmp) and tmp[j][0] == p:
                    tmp[j] = (tmp[j][0], tmp[j][1] + 1)
                else:
                    tmp.insert(j, (p, 1))

                break
        if is_prime_flag:
            ret[i] = [(i, 1)]
        else:
            ret[i] = tmp

    return ret


def solve1(factors):
    ret = 1
    for p in factors:
        a = factors[p]
        ret = ret * (pow(p, a + 1, mmod) + mmod - 1) % mmod * modinv(p - 1, mmod) % mmod
    return ret

def solve(init, nums):
    facts = factor(init)
    ret = []
    for n in nums:
        tfact = factor(n)
        for p in tfact:
            facts[p] += tfact[p]

        ret.append(solve1(facts))
    return ret


if __name__ == '__main__':
    n, q = map(int, stdin.readline().strip().split())
    nums = []
    ans = None
    factors_table = factor_all(1000000)
    tmp = factors_table[n]
    facts = defaultdict(int)
    for (p, a) in tmp:
        facts[p] += a

    for _ in range(q):
        nums.append(int(stdin.readline()))

    ans = solve1(facts)
    for num in nums:
        tmp = factors_table[num]
        for (p, a) in tmp:
            prev = facts[p]
            ans = ans * (p - 1) * modinv(pow(p, prev + 1, mmod) + mmod - 1, mmod) % mmod
            facts[p] += a
            ans = ans * (pow(p, facts[p] + 1, mmod) + mmod - 1) % mmod * modinv(p - 1, mmod) % mmod
        print(ans)

