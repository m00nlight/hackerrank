from __future__ import division
from math import factorial
from bisect import bisect_left
from sys import stdin

def genFibonacci(n):
    a, b = 1, 1
    ret = [1]

    while b < n:
        a, b = b, a + b
        ret.append(b)
    return ret

fibs = genFibonacci(10 ** 18)
    
def solve(nums):
    ans = 0
    for n in nums:
        upper = -1
        for i in range(len(fibs)):
            if fibs[i] > n:
                upper = i - 1
                break
        for i in range(upper, -1, -1):
            if n >= fibs[i]:
                n -= fibs[i]
                ans = ans ^ (1 << i)

    return ans % (10 ** 9 + 7)

if __name__ == '__main__':
    n = int(stdin.readline())
    arr = map(int, stdin.readline().strip().split())
    print solve(arr)