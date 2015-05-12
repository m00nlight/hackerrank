from __future__ import division
from math import log
import cProfile

def larsson_sadakane(string):
    """
    Larsson sadakane suffix array construction algorithm
    Reference Paper: Faster suffix sorting
    Got Accept of 8/10 test case for the problem in python
    """
    n = len(string)
    g, b, v = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)

    for i in l2:
        v[i] = i
        g[i] = -1 if i == n else ord(string[i])

    cmp1 = lambda a, b: -1 if a == b else g[a] - g[b]

    cmp2 = lambda a, b: -1 if a == b else g[a] - g[b] if g[a] - g[b] != 0 else g[a + u] - g[b + u]

    v.sort(cmp = cmp1)
    h = 1

    while b[n] != n:
        u = h
        v.sort(cmp = cmp2)

        for i in xrange(n):
            b[i + 1] = b[i] + (1 if cmp2(v[i], v[i + 1]) < 0 else 0)

        for i in xrange(n + 1): 
            g[v[i]] = b[i]

        h = (h << 1)

    return v

def build_lcp(string, suffix_array):
    n, h = len(string), 0
    lcp, b = [0] * (n + 1), [0] * (n + 1)
    for i in xrange(n + 1): b[suffix_array[i]] = i
    for i in xrange(n + 1):
        if b[i] != 0:
            j = suffix_array[b[i] - 1]
            while j + h < n and i + h < n and string[j + h] == string[i + h]:
                h += 1
            lcp[b[i]] = h
        else:
            lcp[b[i]] = -1

        if h > 0: h -= 1
    return lcp

def main():
    t = int(input())
    for _ in xrange(t):
        string = raw_input().strip()
        sa = larsson_sadakane(string)
        lcp = build_lcp(string, sa)
        n = len(string) + 1
        ret = n
        for i in xrange(n):
            if sa[i] == 0:
                mx = 9999999
                for j in xrange(i, -1, -1):
                    mx = min(mx, lcp[j])
                    ret += mx
                mx = 9999999
                for j in range(i + 1, n):
                    mx = min(mx, lcp[j])
                    ret += mx
        print ret

if __name__ == '__main__':
    main()
    #cProfile.run('main()')

