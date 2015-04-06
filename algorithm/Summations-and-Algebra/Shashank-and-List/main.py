from __future__ import division

MOD = 10 ** 9 + 7

def solve(arr):
    ret = 1
    for a in arr:
        ret = ret * (pow(2, a, MOD) + 1) % MOD

    return (ret - 1 + MOD) % MOD

if __name__ == '__main__':
    _ = raw_input()
    arr = map(int, raw_input().strip().split())
    print solve(arr)