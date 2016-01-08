from __future__ import division
from sys import stdin
from collections import deque

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(grid, a, b, c, d):

    que = deque()
    que.append((a, b))
    n = len(grid)
    ret = 0
    grid[a][b] = 0

    def help(nx, ny,  update_fn, judge_fn):
        while judge_fn(nx, ny) and grid[nx][ny] != 'X':
            if grid[nx][ny] == '.':
                grid[nx][ny] = grid[x][y] + 1
                que.append((nx, ny))
            if isinstance(grid[nx][ny], int):
                grid[nx][ny] = min(grid[x][y] + 1, grid[nx][ny])
            nx, ny = update_fn(nx, ny)

    while grid[c][d] == '.':
        x, y = que.popleft()
        nx, ny = x - 1, y
        help(nx, ny, lambda nx, ny: (nx - 1, ny), lambda nx, ny: nx >= 0)

        nx, ny = x + 1, y
        
        help(nx, ny, lambda nx, ny: (nx + 1, ny), lambda nx, ny: nx < n)

        nx, ny = x, y - 1
        
        help(nx, ny, lambda nx, ny: (nx, ny - 1), lambda nx, ny: ny >= 0)

        nx, ny = x, y + 1
        
        help(nx, ny, lambda nx, ny: (nx, ny + 1), lambda nx, ny: ny < n)

    return(grid[c][d])

if __name__ == '__main__':
    n = int(stdin.readline())
    grid = []
    for _ in range(n):
        grid.append(list(stdin.readline().strip()))

    a, b, c, d = map(int, stdin.readline().strip().split())
    print(bfs(grid, a, b, c, d))