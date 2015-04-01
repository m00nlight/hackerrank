from __future__ import division

def solve(row, col):
    if row % 2 is 0:
        start = (row // 2) * 10
    else:
        start = (row // 2) * 10 + 1

    return start + col * 2

if __name__ == '__main__':
    a, b = map(int, raw_input().strip().split())
    print solve(a - 1, b - 1)