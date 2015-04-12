# -.- encoding: utf-8
# Finbonacci number matrix form
from operator import mul
from random import randrange
from sys import exit

MOD = 1000000007

debug = False

class Matrix:
    def __init__(self, rows, m, n):
        self.m = m
        self.n = n
        self.rows = [[item for item in row] for row in rows]
        
    def __mul__(self, other):
        assert self.n == other.m
        ret = [[0 for _ in range(other.n)] for _ in range(self.m)]
        for i in range(self.m):
            for j in range(other.n):
                for k in range(self.n):
                    ret[i][j] += self.rows[i][k] * other.rows[k][j]
                    ret[i][j] %= MOD
        return Matrix(ret, self.m, other.n)
    
    def __rmul__(self, other):
        return other * self
        
        
    # only for square matrix
    def __pow__(self, n):
        if n == 0:
            ret = [[0 for _ in range(self.m)] for _ in range(self.n)]
            for i in range(self.m): ret[i][i] = 1
            return Matrix(ret, self.m, self.m)
        elif n == 1:
            return self
        else:
            tmp = self ** (n // 2)
            return tmp * tmp if n % 2 is 0 else tmp * tmp * self

def fib(A, B, N):
    row = Matrix([[A, B]], 1, 2)
    mat = Matrix([[0,1], [1,1]], 2,2)
    mat = mat ** N
    return (row * mat).rows[0][0]
    
def gcd(a, b):
    """
    Type :: (Int, Int) -> Int
    Return :: Greatest Common divisor
    """
    while b != 0:
        a, b = b, a % b
    return a

def exgcd(a, b):
    """
    Type :: (Int, Int) -> (Int, Int, Int)
    Return :: (g, x, y), g is gcd of a and b and
    x * a + y * b = g
    """
    if b == 0:
        return (a, 1, 0)
    else:
        g, x, y = exgcd(b, a % b)
        return (g, y, x - (a // b) * y)
    
def modinv(a, m):
    """
    Type :: (Int, Int) -> Int
    Return :: Return module inverse of a * x = 1 (mod m)
    """
    if gcd(a, m) != 1: 
        raise Exception("Not coprime")
    _, x, y = exgcd(a, m)
    return (m + x % m) % m
    
def lcm(a, b):
    print 'gcd(a, b) = %d modinv = %d' %(gcd(a, b), modinv(gcd(a, b), MOD))
    return a * b * modinv(gcd(a, b), MOD) % MOD

    
if __name__ == '__main__':
    n = input()
    arr = []
    for _ in range(n):
        arr.append(int(raw_input()))
    print arr
    print '%d' % reduce(lambda acc, x: )