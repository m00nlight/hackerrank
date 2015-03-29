from __future__ import division
from bisect import bisect_right

MOD = 1000000007

def solve(arr):
    arr = sorted(arr)
    ret = 1
    for i in range(len(arr)):
        ret = ret * (bisect_right(arr, i) - i) % MOD
    return ret

if __name__ == '__main__':
    t = int(raw_input())
    for _ in range(t):
        n = int(raw_input())
        arr = map(int, raw_input().strip().split())
        print solve(arr)