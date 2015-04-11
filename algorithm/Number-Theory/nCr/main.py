from __future__ import division
from operator import add, mul
import cProfile

def memo(f):
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            result = cache[args] = f(*args)
            return result
        except TypeError:
            return f(*args)
    return _f

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



@memo
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
    for i in xrange(4, m + 1, 2): judge[i] = False
    for i in xrange(3, m + 1, 2):
        if judge[i]:
            ret.append(i)
            for j in xrange(i * i, m + 1, i): judge[j] = False
    return ret


MAXN = 1000

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

def euler_phi(n):
    """
    Type :: Int -> Int
    Calculate the Euler phi result of number n in around log(n) of time

    >>> euler_phi(12)
    4

    >>> euler_phi(17)
    16

    >>> euler_phi(33)
    20
    """
    facts = factor(n)
    return reduce(lambda acc, x: acc * (x[0] - 1) // x[0], facts, n)
    

def euler_phi2(n):
    """
    Type :: Int -> [Int]
    Generate the Euler phi result up to number n, and return the result
    as a list
    
    >>> euler_phi2(20) == [0] + [euler_phi(i) for i in range(1, 21)]
    True
    
    >>> euler_phi2(100) == [0] + [euler_phi(i) for i in range(1, 101)]
    True
    
    >>> euler_phi2(1000) == [0] + [euler_phi(i) for i in range(1, 1001)]
    True
    """
    ret = [i for i in range(n + 1)]
    for i in range(2, n + 1):
        if ret[i] == i:
            for j in range(i, n + 1, i): ret[j] = ret[j] // i * (i - 1)
    
    return ret


def gen_fact_mod_prime(p):
    """
    Type :: Int -> [Int]
    Generate the fact of i(mod p) for 1 <= i < p, p should be a prime number

    >>> gen_fact_mod_prime(3)
    [1, 1, 2]

    >>> gen_fact_mod_prime(7)
    [1, 1, 2, 6, 3, 1, 6]
    """
    ret = [1] * p
    for i in range(2, p): ret[i] = ret[i - 1] * i % p
    return ret

def fact_mod(n, p, facts):
    """
    Type :: (Int, Int, [Int]) -> (Int, Int)
    Suppose n! = a * p^e (mod p), then the function return (a mod p, e)
    facts is i!(mod p) for 0 <= i < p, use Lucas theory

    >>> facts = gen_fact_mod_prime(7)
    >>> fact_mod(5, 7, facts)
    (1, 0)

    >>> fact_mod(15, 7, facts)
    (2, 2)
    """
    if (n == 0): return (1, 0)
    (a, e) = fact_mod(n // p, p, facts)
    e += n // p

    if (n // p % 2 != 0): return (a * (p - facts[n % p]) % p, e)
    return (a * facts[n % p] % p, e)


def comb_mod(n, k, p):
    """
    Type :: (Int, Int, Int) -> Int
    Return C(n, k) mod p, p is a prime number.

    >>> comb_mod(5, 3, 7)
    3

    >>> comb_mod(6, 2, 7)
    1
    """

    if n < 0 or k < 0 or n < k: return 0
    facts = gen_fact_mod_prime(p)
    a1, e1 = fact_mod(n, p, facts)
    a2, e2 = fact_mod(k, p, facts)
    a3, e3 = fact_mod(n - k, p, facts)
    if (e1 > e2 + e3):
        return 0
    else:
        return a1 * modinv(a2 * a3 % p, p) % p


def chinese_remainder_theory_for2(x, a, y, b):
    """
    Type :: (Int, Int, Int, Int) -> Int
    Return z for z = a (mod x) and z = b (mod y). Here z is unique modulo 
    M = lcm(x, y), return (z, M). On failure return, M = -1
    """
    g, s, t = exgcd(x, y)
    if (a % g) != (b % g):
        return (0, -1)
    else:
        return (mod(s * b * x + t * a * y, x * y) // g, x * y // g)

def chinese_remainder_theory(xs, ass):
    """
    Type :: ([Int], [Int]) -> Int
    Return  : z that z[i] = a[i] (mod xs[i]) for 0 <= i < n
    Require : Require a[i] to be relative coprime to each other

    >>> chinese_remainder_theory([3, 5, 7], [2,3,2])
    (23, 105)
    """

    ret = (ass[0], xs[0])
    for i in xrange(1, len(xs)):
        ret = chinese_remainder_theory_for2(ret[1], ret[0], xs[i], ass[i])
        if ret[1] == -1: break

    return ret


def comb_mod2(n, r, m, pa, facts1):
    """
    Type :: (Int, Int, Int) -> Int
    m is of form p^a, and n is very large
    """
    p, a = pa

    def n_fact_fact(n):
        if n is 0 or n is 1:
            return 1
        elif n < m:
            return facts1[n] * n_fact_fact(n // p) % m
        else:
            a = facts1[m - 1]
            b = facts1[n % m]
            c = n_fact_fact(n // p)
            # print 'n = %d a = %d b = %d c = %d' % (n, a, b, c)
            return pow(a, n // m, m) * b * c % m

    def get_power(n, p):
        ret = 0
        while n > 0:
            ret += n // p
            n //= p
        return ret
    b = get_power(n, p) - get_power(r, p) - get_power(n - r, p)

    if b >= a: return 0

    m1 = n_fact_fact(n)
    m2 = n_fact_fact(r)
    m3 = n_fact_fact(n - r)


    return (p ** b) * m1 * modinv_table[(m2, m)] * modinv_table[(m3, m)] % m


def solve(n, r, fs1, fs2, xss):
    xs = [27, 11, 13, 37]
    ass = [comb_mod2(n, r, xs[i], xss[i], fs1[i]) for i in xrange(4)]

    return chinese_remainder_theory(xs, ass)

def init(xs):
    ret1, ret2 = [], []

    for i in xrange(len(xs)):
        p, a = xs[i]
        m = p ** a
        t1, t2 = [1],[1]
        for i in xrange(1, p):
            t2.append(t2[-1] * i % p)

        for i in xrange(1, m):
            if gcd(i, m) == 1:
                t1.append(t1[-1] * i % m)
            else:
                t1.append(t1[-1])
        ret1.append(t1)
        ret2.append(t2)
    return ret1, ret2

modinv_table = {}
modulo = 142857

for x in {27, 11, 13, 37}:
    for y in xrange(1, x):
        if gcd(x, y) == 1:
            modinv_table[(y, x)] = modinv(y, x)



def main():
    n = int(raw_input())
    xss = [(3,3), (11,1), (13, 1), (37, 1)]
    facts1, facts2 = init(xss)

    for _ in xrange(n):
        n, r = map(int, raw_input().strip().split())
        print solve(n, r, facts1, facts2, xss)[0]

if __name__ == '__main__':
    main()
    # cProfile.run('main()')
