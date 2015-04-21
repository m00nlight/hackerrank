from __future__ import division
from collections import defaultdict
from itertools import groupby, count
from math import sqrt

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

MAXN = 10 ** 5 + 10
lookup, indexes = None, None

def init(arr):
    ret = defaultdict(set)
    for i in range(1, MAXN):
        for j in range(1, int(sqrt(i) + 1)):
            if i % j == 0:
                ret[j].add(i)
                ret[i // j].add(i)
        ret[i].add(i)

    idxes = {}
    for idx, a in enumerate(arr):
        idxes[a] = idx

    return ret, idxes

@memo
def query(k):
    idxes = []
    for num in lookup[k]:
        if num in indexes:
            idxes.append(indexes[num])

    idxes = sorted(idxes)
    
    def ar(g):
        l = list(g)
        return l[0], l[-1]

    idxes = [ar(g) for _, g in groupby(idxes, \
                key=lambda n, c=count(): n-next(c))]
    ret = 0

    for a, b in idxes:
        tmp = b - a + 1
        ret += tmp * (tmp + 1) // 2
    return ret

if __name__ == '__main__':
    n = input()
    arr = map(int, raw_input().strip().split())
    lookup, indexes = init(arr)
    q = input()
    for _ in range(q):
        k = input()
        print query(k)