from __future__ import division
from math import pi, sin, cos

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
    facts is i!(mod p) for 0 <= i < p, use Lucas Theory

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
    if a % g != b % g:
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
    for i in range(1, len(xs)):
        ret = chinese_remainder_theory_for2(ret[1], ret[0], xs[i], ass[i])
        if ret[1] == -1: break

    return ret

# miller rabin primiarility test from rosetta code

def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite
 
def miller_rabin(n, _precision_for_huge_n=16):
    if n in _known_primes or n in (0, 1):
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467: 
        if n == 3215031751: 
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383: 
        return not any(_try_composite(a, d, n, s) \
                        for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321: 
        return not any(_try_composite(a, d, n, s) \
                        for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s) 
                   for a in _known_primes[:_precision_for_huge_n])
 
_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if miller_rabin(x)]


def baby_step(a, b, g):
    """
    Baby Step Giant step :: calculate a^x == b (mod g) for gcd(a, g) == 1
    Type :: (Int, Int, Int) -> Int
    Return :: Return minimum positive x for a^x == b (mod g)
    Complexity :: O(Sqrt(g))

    >>> baby_step(3, 2, 5)
    3
    >>> baby_step(2, 5, 11)
    4
    >>> baby_step(233529, 184091, 329746)
    57897
    >>> baby_step(26161, 23893, 62356)
    223
    >>> baby_step(126995, 142647, 270599)
    204
    """
    q = int(g ** 0.5) + 1
    aq = pow(a, q, g)
    ai = modinv(a, g)

    assert a * ai % g == 1

    l = map(lambda i: pow(aq, i, g), xrange(q + 1))
    r = map(lambda i: (b * pow(ai, i, g)) % g, xrange(q + 1))
    xs = set()
    for y in set(l) & set(r):
        i = l.index(y)
        j = r.index(y)
        xs.add(i * q + j)

    if not xs:
        return -1
    x = min(xs)
    assert pow(a, x, g) == b
    return x


def fft(xs):
    """
    Fast Fourier transform, algorithm
    Type :: [Complex] -> [Complex]
    Return :: A complex array of the transform
    Complexity :: O(n * log(n)), n is the length of xs
    Pre Require :: length of xs should be power of 2

    >>> fft(ifft([complex(1, 0), complex(2, 0)])) == [complex(1, 0), complex(2, 0)]
    True
    """
    if len(xs) == 1:
        return xs
    else:
        n = len(xs)
        wn = complex(cos(2 * pi / n), sin(2 * pi / n))
        w = complex(1, 0)
        a0 = [x[1] for x in filter(lambda x: x[0] % 2 == 0, zip(range(n), xs))]
        a1 = [x[1] for x in filter(lambda x: x[0] % 2 == 1, zip(range(n), xs))]
        y0 = fft(a0)
        y1 = fft(a1)
        ys = [complex(0, 0)] * n
        for k in range(n // 2):
            ys[k] = y0[k] + w * y1[k]
            ys[k + n // 2] = y0[k] - w * y1[k]
            w = w * wn
        return ys


def ifft(xs):
    """
    Inverse Fast Fourier transform algorithm
    Type :: [Complex] -> [Complex]
    Return :: A complex array of the inverse of fft
    Complexity :: O(n * log(n)), n is the length of xs
    Pre Require :: length of xs should be power of 2

    >>> ifft(fft([complex(1, 0), complex(2, 0)])) == [complex(1, 0), complex(2, 0)]
    True
    """
    if len(xs) == 1:
        return xs
    else:
        n = len(xs)
        wn = complex(cos(-2 * pi / n), sin(-2 * pi / n))
        w = complex(1, 0)
        a0 = [x[1] for x in filter(lambda x: x[0] % 2 == 0, zip(range(n), xs))]
        a1 = [x[1] for x in filter(lambda x: x[0] % 2 == 1, zip(range(n), xs))]
        y0 = fft(a0)
        y1 = fft(a1)
        ys = [complex(0, 0)]  * n
        for k in range(n // 2):
            ys[k] = y0[k] + w * y1[k]
            ys[k + n // 2] = y0[k] - w * y1[k]
            w = w * wn

        return map(lambda x: complex(x.real / n, x.imag), ys)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
