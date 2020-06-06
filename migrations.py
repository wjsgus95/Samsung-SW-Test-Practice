# https://www.acmicpc.net/problem/16234

from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

N, L, R = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

def open_borders(grid):
    for x in range(N):
        for y in range(N):
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < N and 0 <= ny < N:
                    if L <= abs(grid[x][y] - grid[nx][ny]) <= R:
                        return True
    
    return False

def form_alliances(grid):
    alliances = []
    visited = [[False] * N for _ in range(N)]

    def bfs(x, y):
        nonlocal visited

        if visited[x][y]:
            return None

        queue = deque()
        queue.append((x,y))
        visited[x][y] = True
        group = set()
        group.add((x,y))

        while queue:
            _x, _y = queue.popleft()
            
            for i in range(4):
                nx = _x + dx[i]
                ny = _y + dy[i]

                if 0 <= nx < N and 0 <= ny < N:
                    if not visited[nx][ny] and L <= abs(grid[_x][_y] - grid[nx][ny]) <= R:
                        queue.append((nx,ny))
                        visited[nx][ny] = True
                        group.add((nx,ny))

        return group
            
    for x in range(N):
        for y in range(N):
            group = bfs(x, y)
            if group:
                alliances.append(group)

    return alliances

def migrate(grid, alliance):
    total_population = sum(grid[x][y] for x,y in alliance)

    for x, y in alliance:
        grid[x][y] = total_population // len(alliance)


count = 0
while True:
    if open_borders(grid):
        count += 1
        alliances = form_alliances(grid)

        for alliance in alliances:
            migrate(grid, alliance)
    else: break

print(count)
