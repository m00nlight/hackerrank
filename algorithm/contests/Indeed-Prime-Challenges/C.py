import sys
import itertools

def cis(s1, e1, s2, e2):
    "combine interval [s1, e1], with [s2, e2]"
    if e1 + 1 == s2:
        return (s1, e2)
    else:
        return (s1, e1)

def cie(s1, e1, s2, e2):
    if e1 + 1 == s2:
        return (s1, e2)
    else:
        return (s2, e2)

def helper(info1, info2):
    (m1, l1, r1, s11, e11, s12, e12) = info1
    (m2, l2, r2, s21, e21, s22, e22) = info2

    if m1 < m2:
        return (m1,) + cis(l1, r1, s21, e21) + cis(s11, e11, s21, e21) + cie(s12, e12, s22, e22)
    elif m2 < m1:
        return (m2,) + cie(s12, e12, l2, r2) + cis(s11, e11, s21, e21) + cie(s12, e12, s22, e22)
    else: # m1 == m2
        (p1, q1) = cis(l1, r1, s21, e21)
        (p2, q2) = cie(s12, e12, l2, r2)
        (p3, q3) = cis(s12, e12, s21, e21)

        if m1 != 1:
            if (q1 - p1 >= p2 - q2):
                return (m1,) + (p1, q1) + cis(s11, e11, s21, e21) + cie(s12, e12, s22, e22)
            else:
                return (m1,) + (p2, q2) + cis(s11, e11, s21, e21) + cie(s12, e12, s22, e22)
        else: # m1 == 1
            if (q3 - p3 > q1 - p1) and (q3 - p3 > q2 - p2):
                return (m1,) + (p3, q3) + cis(s11, e11, s21, e21) + cie(s12, e12, s22, e22)
            elif (q1 - p1 > q3 - p3) and (q1 - p1 > q2 - p2):
                return (m1,) + (p1, q1) + cis(s11, e11, s21, e21) + cie(s12, e12, s22, e22)
            elif (q2 - p2 > q3 - p3) and (q2 - p2 > q1 - p1):
                return (m1,) + (p2, q2) + cis(s11, e11, s21, e21) + cie(s12, e12, s22, e22)
            else:
                if p3 == -2:
                    tmp = sorted([(p2 - q2, p2, q2), (p1 - q1, p1, q1)])
                else:
                    tmp = sorted([(p3 - q3, p3, q3), (p2 - q2, p2, q2), (p1 - q1, p1, q1)])
                return (m1,) + tmp[0][1:3] + cis(s11, e11, s21, e21) + cie(s12, e12, s22, e22)



class RMQ:
    def __init__(self, n):
        self.sz = 1
        self.inf = sys.maxint
        while self.sz < n: self.sz = self.sz << 1
        self.dat = [(self.inf, -2, -2, -2, -2, -2, -2)] * (2 * self.sz - 1)

    def update(self, idx, x):
        tmp = idx
        idx += self.sz - 1
        if x == 1:
            self.dat[idx] = (x, tmp, tmp, tmp, tmp, tmp, tmp)
        else:
            self.dat[idx] = (x, tmp, tmp, -2, -2, -2, -2)

        while idx > 0:
            idx = (idx - 1) >> 1
            self.dat[idx] = helper(self.dat[idx * 2 + 1], self.dat[idx * 2 + 2])
                
            
    def query(self, a, b):
        return self.query_help(a, b, 0, 0, self.sz)
            
    def query_help(self, a, b, k, l, r):
        if r <= a or b <= l:
            return (sys.maxint, -2, -2, -2, -2, -2, -2)
        elif a <= l and r <= b:
            return self.dat[k]
        else:
            info1 = self.query_help(a, b, 2 * k + 1, l, (l + r) >> 1)
            info2 = self.query_help(a, b, 2 * k + 2, (l + r) >> 1, r)
            return helper(info1, info2)

    
if __name__ == '__main__':
    n , q = map(int, raw_input().strip().split())
    arr = map(int, raw_input().strip().split())
    rmq = RMQ(n)
    for idx, a in enumerate(arr):
        rmq.update(idx, a)


    for _ in range(q):
        op, a, b = map(int, raw_input().strip().split())
        if op == 1:
            a , b = a - 1, b - 1
            v, l, r = rmq.query(a, b + 1)[0:3]
            if v == 0:
                print '%d %d %d' %(0, a + 1, b + 1)
            else:
                print '%d %d %d' % (v, l + 1, r + 1)
        else:
            a = a - 1
            arr[a] = b
            rmq.update(a, b)
