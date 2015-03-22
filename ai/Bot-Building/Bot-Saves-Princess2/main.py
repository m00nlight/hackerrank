from __future__ import division

def solve(n, r, c, grid):
    def find_index(ch):
        for i in xrange(n):
            for j in xrange(n):
                if grid[i][j] == ch:
                    return (i,j)
        return (None, None)

    p, q = find_index('p')

    if q < c: 
        return 'LEFT'
    elif q == c:
        if p < r: return 'UP'
        else: return 'DOWN'
    else:
        return 'RIGHT'

if __name__ == '__main__':
    n = int(raw_input())
    r, c = map(int, raw_input().strip().split())
    grid = []
    for _ in xrange(n):
        grid.append(raw_input().strip())

    print solve(n, r, c, grid)
