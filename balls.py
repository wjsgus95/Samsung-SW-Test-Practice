# https://www.acmicpc.net/problem/13460

from copy import deepcopy
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

R, C = map(int, input().split())
grid = [list(input()) for _ in range(R)]

# Visited[R][C][R][C]
visited = [[[[False] * C for _ in range(R)] for __ in range(C)] for ___ in range(R)]

for r in range(R):
    for c in range(C):
        if grid[r][c] == 'R':
            red = r, c
        if grid[r][c] == 'B':
            blue = r, c
        if grid[r][c] == 'O':
            end = r, c

queue = deque()
queue.append((red, blue, 0))

rx, ry = red
bx, by = blue
visited[rx][ry][bx][by] = True

def move(x, y, dx, dy):
    travel = 0
    while grid[x+dx][y+dy] != '#' and grid[x][y] != 'O':
        x += dx
        y += dy
        travel += 1
    return x, y, travel

answer = -1
found = False

while queue:
    (rx, ry), (bx, by), count = queue.popleft()

    if count == 10:
        break
   
    for i in range(4):
        nrx, nry, r_travel = move(rx, ry, dx[i], dy[i])
        nbx, nby, b_travel = move(bx, by, dx[i], dy[i])

        if (nbx, nby) == end:
            continue

        if (nrx, nry) == end:
            if not found:
                answer = count + 1
                found = True

        if nrx == nbx and nry == nby:
            if r_travel > b_travel:
                nrx -= dx[i]
                nry -= dy[i]
            else:
                nbx -= dx[i]
                nby -= dy[i]
        
        if not visited[nrx][nry][nbx][nby]:
            queue.append(((nrx, nry), (nbx, nby), count+1))
            visited[nrx][nry][nbx][nby] = True

print(answer)
