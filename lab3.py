# https://www.acmicpc.net/problem/17142

from itertools import combinations
from collections import deque

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

E, W, V = 0, 1, 2

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

candidates = []
num_walls = 0
for x in range(N):
    for y in range(N):
        if grid[x][y] == V:
            candidates.append((x,y))
        elif grid[x][y] == W:
            num_walls += 1


def bfs(odd):
    queue = deque()
    visited = [[False] * N for _ in range(N)]
    count = 0
    
    for x, y in odd:
        visited[x][y] = True
        queue.append((x,y, 0))

    max_t = 0
    while queue:
        x, y, t = queue.popleft()
        if grid[x][y] != V:
            max_t = max(max_t, t)
        count += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if grid[nx][ny] != W and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, t+1))

    for x in range(N):
        for y in range(N):
            if not visited[x][y] and grid[x][y] != W:
                return max_t, False

    return max_t, True
        
    

min_t = 0xFFFF_FFFF_FFFF
odds = combinations(candidates, M)
for odd in odds:
    t, flag = bfs(odd)
    if flag:
        min_t = min(t, min_t)

if min_t == 0xFFFF_FFFF_FFFF:
    min_t = -1
print(min_t)
