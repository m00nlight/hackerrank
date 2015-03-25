from __future__ import division

def solve(arr):
    return sum(arr) / 2.0

if __name__ == '__main__':
    n = int(raw_input())
    arr = []
    for _ in range(n):
        arr.append(int(raw_input()))

    print solve(arr)