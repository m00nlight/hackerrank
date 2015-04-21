from __future__ import division

def gcd(a, b):
    """
    Type :: (Int, Int) -> Int
    Return :: Greatest Common divisor
    """
    while b is not 0:
        a, b = b, a % b
    return a


def solve(arr, k):
    tmp = []
    for n in arr:
        if n % k == 0: tmp.append(n // k)

    if not tmp: return 'NO'
    if reduce(lambda acc, x: gcd(acc, x), tmp, tmp[0]) == 1:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    t = input()
    for _ in range(t):
        _, k = map(int, raw_input().strip().split())
        arr = map(int, raw_input().strip().split())
        print solve(arr, k)