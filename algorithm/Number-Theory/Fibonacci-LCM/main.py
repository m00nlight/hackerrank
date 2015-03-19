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
    
def exgcd(m, n):
    if n == 0:
        return (m, 1, 0)
    else:
        g, x1, y1 = exgcd(n, m % n)
        return (g, y1, x1 - y1 * (m // n))
        
def gcd(m, n):
    return exgcd(m, n)[0]
    
def modinv(a, m):
    g, x, y = exgcd(a, m)
    
    return (x + m) % m
    
def mlcm(a, b):
    g, x, y = exgcd(a, b)
    inv = modinv(g, MOD)
    return a * b * inv % MOD
    
def lcm(a, b):
    return a * b // gcd(a, b)
    
def test(times):
    for _ in range(times):
        arr = []
        for _ in range(3):
            arr.append(randrange(1, 20))
        farr = map(lambda x: fib(0, 1, x), arr)
        if reduce(lambda acc, x, : mlcm(acc, x), farr, farr[0]) != \
            reduce(lambda acc, x : lcm(acc, x), farr, farr[0]) % MOD:
            print 'mlcm = %d' % reduce(lambda acc, x, : mlcm(acc, x), farr, farr[0])
            print 'lcm = %d' % (reduce(lambda acc, x: lcm(acc, x), farr, farr[0]) % MOD)
            print arr
            print farr
            exit()
    return 'test pass'
            
    
    
if __name__ == '__main__':
    if debug:
        test()
    else:
        n = int(raw_input())
        arr = []
        for _ in range(n):
            arr.append(fib(0, 1, int(raw_input())))
        
        print '%d' % (reduce(lambda acc, x: lcm(acc, x), arr, arr[0]) % MOD)