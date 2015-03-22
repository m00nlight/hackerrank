# Can use to accept Bot Clean and Bot Clean 2
from __future__ import division

def next_move(r, c, grid):
    n = len(grid)
    def nearest_dirty_position():
        diff = 2 * n
        nr, nc = -1, -1
        for i in xrange(n):
            for j in xrange(n):
                if grid[i][j] == 'd' and \
                    abs(i - r) + abs(j - c) < diff:
                    diff = abs(i - r) + abs(j - c)
                    nr, nc = (i, j)
        return (nr, nc)

    nr, nc = nearest_dirty_position()
    if nr < r:
        return 'UP'
    elif nr == r:
        if nc < c: return 'LEFT'
        elif nc == c: return 'CLEAN'
        else: return 'RIGHT'
    else:
        return 'DOWN'

if __name__ == '__main__':
    r, c = map(int, raw_input().strip().split())
    grid = []
    for _ in xrange(5):
        grid.append(raw_input().strip())

    print next_move(r, c, grid)