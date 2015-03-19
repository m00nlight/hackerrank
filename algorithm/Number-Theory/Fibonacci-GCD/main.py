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
    while b != 0:
        a, b = b, a % b
    return a
    
if __name__ == '__main__':
    n = int(raw_input())
    idx = []
    for _ in range(n):
        idx.append(int(raw_input()))
    g = reduce(lambda acc, x: gcd(acc, x), idx, idx[0])
    print '%d' % fib(0, 1, g)