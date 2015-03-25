from __future__ import division

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

def factor(n):
    """
    Type :: Int -> [(Int, Int)]
    Return the factorizatoin result of decompose number n
    >>> factor(12)
    [(2, 2), (3, 1)]

    >>> factor(10007)
    [(10007, 1)]
    """
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



if __name__ == '__main__':
    import doctest
    doctest.testmod()