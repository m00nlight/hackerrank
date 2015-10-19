from __future__ import division
from collections import deque
from sys import stdin

def solve(n, moves):
    dirs = [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0)]

    broad = [[-2 for _ in range(n)] for _ in range(n)]
    flag = 1

    for move in moves:
        broad[move[0] - 1][move[1] - 1] = flag
        flag  = flag * -1

    def roman_win():
        que = deque()
        vis = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            if broad[i][0] == 1:
                que.append((i, 0))
                vis[i][0] = True

        while que:
            (cx, cy) = que.popleft()
            if cy == n -1:
                return True
            for dx, dy in dirs:
                nx, ny = cx + dx, cy + dy
                if  nx >= 0 and nx < n and ny >= 0 and ny < n and (not vis[nx][ny]) and broad[nx][ny] == 1:
                    que.append((nx, ny))
                    vis[nx][ny] = True

        return False

    def persian_win():
        que = deque()
        vis = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            if broad[0][i] == -1:
                que.append((0, i))
                vis[0][i] = True

        while que:
            (cx, cy) = que.popleft()
            if cx == n -1:
                return True
            for dx, dy in dirs:
                nx, ny = cx + dx, cy + dy
                if nx >= 0 and nx < n and ny >= 0 and ny < n and (not vis[nx][ny]) and broad[nx][ny] == -1:
                    que.append((nx, ny))
                    vis[nx][ny] = True

        return False


    
    rw , pw = False, False
    rw = roman_win()
    pw = persian_win()


    if rw:
        print("ROMANS")
    elif pw:
        print("PERSIANS")
    else:
        print("NEITHER")

if __name__ == '__main__':
    n, m = map(int, stdin.readline().strip().split())
    moves = []
    for _ in range(m):
        a, b = map(int, stdin.readline().strip().split())
        moves.append((a, b))

    solve(n, moves)
