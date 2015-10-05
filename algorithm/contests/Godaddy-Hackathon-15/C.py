from sys import stdin
import sys
import itertools

class RMQ:
    def __init__(self, n):
        self.sz = 1
        self.inf = 0
        while self.sz <= n: self.sz = self.sz << 1
        self.dat = [self.inf] * (2 * self.sz - 1)
    
    def update(self, idx, x):
        idx += self.sz - 1
        self.dat[idx] = x
        while idx > 0:
            idx = (idx - 1) >> 1
            self.dat[idx] = max(self.dat[idx * 2 + 1], self.dat[idx * 2 + 2])
            
    def query(self, a, b):
        return self.query_help(a, b, 0, 0, self.sz)
            
    def query_help(self, a, b, k, l, r):
        if r <= a or b <= l:
            return 0
        elif a <= l and r <= b:
            return self.dat[k]
        else:
            return max(self.query_help(a, b, 2 * k + 1, l, (l + r)>>1),
                       self.query_help(a, b, 2 * k + 2, (l + r) >> 1, r))

    def rmq_print(self):
        print('sz = %d' % self.sz)
        print(self.dat)



def solve(infos):
    xs = sorted(set(map(lambda (y, x, w) : x, infos)))
    xsInverse = {}
    for i in range(len(xs)):
        xsInverse[xs[i]] = i


    rmq = RMQ(len(xs))
    for info in infos:
        idx = xsInverse[info[1]]
        val = rmq.query(0, idx) + info[-1]
        rmq.update(idx, val)

    print("%d" % rmq.query(0, len(xs)))

    
    
if __name__ == '__main__':
    n = int(stdin.readline().strip())
    infos = []
    for _ in range(n):
        x, y, w = map(int, stdin.readline().strip().split())
        infos.append((y, x, w))

    infos = sorted(infos)
    if infos[0][0] != 0 or infos[0][1] != 0:
        infos = [(0, 0, 0)] + infos

    solve(infos)