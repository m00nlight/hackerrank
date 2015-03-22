from __future__ import division

def solve(n, grid):
    sz = n // 2
    if grid[0][0] == 'p':
        return ['LEFT'] * sz + ['UP'] * sz
    elif grid[n - 1][0]  == 'p':
        return ['DOWN'] * sz + ['LEFT'] * sz
    elif grid[0][n - 1] == 'p':
        return ['RIGHT'] * sz + ['UP'] * sz
    else:
        return ['RIGHT'] * sz + ['DOWN'] * sz

if __name__ == '__main__':
    n = int(raw_input())
    grid = []
    for _ in range(n):
        grid.append(raw_input().strip())

    print '\n'.join(solve(n, grid))