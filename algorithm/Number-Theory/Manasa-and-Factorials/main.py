from __future__ import division

def fractorial_zero(n):
    base, ret = 5, 0
    while base <= n:
        ret += n // base
        base *= 5
    return ret

# lower_bound function
def solve(n):
    l, r = 0, 10 ** 30
    while l <= r:
        mid = (l + r) // 2
        if fractorial_zero(mid) >= n:
            r = mid - 1
        else:
            l = mid + 1
    return l


if __name__ == '__main__':
    t = int(raw_input())
    for _ in range(t):
        n = int(raw_input())
        print solve(n)