from __future__ import division

def upper_bound(X):
    l, r = 0, X
    while l <= r:
        mid = l + (r - l) // 2
        if mid * (1 + mid) * (1 + 2 * mid) // 6 > X:
            r = mid - 1
        else:
            l = mid + 1

    return l

def solve(X):
    ub = upper_bound(X)
    return ub - 1

if __name__ == '__main__':
    t = input()
    for _ in range(t):
        X = input()
        print solve(X)