from __future__ import division
from collections import deque

def solve(grid):
    m, n = len(grid), len(grid[0])
    vis = [[False for _ in range(n)] for _ in range(m)]
    dir = [(-1, 0),(1, 0),(0, -1), (0, 1),(-1, -1), (-1, 1), (1, -1), (1, 1)]

    bound = lambda x, y: x >= 0 and x < m and y >= 0 and y < n

    def bfs(x, y):
        que = deque()
        que.append((x, y))
        vis[x][y] = True
        ret = 1
        while que:
            cx, cy = que.popleft()
            for dx, dy in dir:
                nx, ny = cx + dx, cy + dy
                if bound(nx, ny) and grid[nx][ny] == 1 and not vis[nx][ny]:
                    ret += 1
                    que.append((nx, ny))
                    vis[nx][ny] = True
        return ret


    ans = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and not vis[i][j]:
                ans = max(ans, bfs(i, j))

    return ans

if __name__ == '__main__':
    m = int(raw_input())
    n = int(raw_input())
    grid = []
    for _ in range(m):
        row = map(int, raw_input().strip().split())
        grid.append(row)

    print solve(grid)