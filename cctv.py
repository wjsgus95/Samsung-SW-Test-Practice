# https://www.acmicpc.net/problem/15683

from copy import deepcopy

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

cctvs = []
for x in range(N):
    for y in range(M):
        if 1 <= grid[x][y] <= 5:
            cctvs.append([x, y, grid[x][y]])


def type1(x, y, direction, grid):
    if direction == 'N':
        y += 1
        while y < M and grid[x][y] != 6:
            if grid[x][y] == 0:
                grid[x][y] = '#'
            y += 1
    elif direction == 'E':
        x += 1
        while x < N and grid[x][y] != 6:
            if grid[x][y] == 0:
                grid[x][y] = '#'
            x += 1
    elif direction == 'S':
        y -= 1
        while y >= 0 and grid[x][y] != 6:
            if grid[x][y] == 0:
                grid[x][y] = '#'
            y -= 1
    elif direction == 'W':
        x -= 1
        while x >= 0 and grid[x][y] != 6:
            if grid[x][y] == 0:
                grid[x][y] = '#'
            x -= 1

def type2(x, y, direction, grid):
    if direction == 'N' or direction == 'S':
        type1(x, y, 'N', grid)
        type1(x, y, 'S', grid)
    elif direction == 'E' or direction == 'W':
        type1(x, y, 'E', grid)
        type1(x, y, 'W', grid)

def type3(x, y, direction, grid):
    if direction == 'N':
        type1(x, y, 'N', grid)
        type1(x, y, 'E', grid)
    elif direction == 'E':
        type1(x, y, 'E', grid)
        type1(x, y, 'S', grid)
    elif direction == 'S':
        type1(x, y, 'S', grid)
        type1(x, y, 'W', grid)
    elif direction == 'W':
        type1(x, y, 'W', grid)
        type1(x, y, 'N', grid)

def type4(x, y, direction, grid):
    if direction == 'N':
        type1(x, y, 'W', grid)
        type1(x, y, 'N', grid)
        type1(x, y, 'E', grid)
    elif direction == 'E':
        type1(x, y, 'N', grid)
        type1(x, y, 'E', grid)
        type1(x, y, 'S', grid)
    elif direction == 'S':
        type1(x, y, 'E', grid)
        type1(x, y, 'S', grid)
        type1(x, y, 'W', grid)
    elif direction == 'W':
        type1(x, y, 'N', grid)
        type1(x, y, 'W', grid)
        type1(x, y, 'S', grid)

def type5(x, y, direction, grid):
        type1(x, y, 'N', grid)
        type1(x, y, 'E', grid)
        type1(x, y, 'S', grid)
        type1(x, y, 'W', grid)


funcs = { 1 : type1, 2 : type2, 3 : type3, 4 : type4, 5 : type5 }

def dfs(i, _grid):
    if i == len(cctvs):
        #print()
        #for row in _grid:
        #    for i in row:
        #        print(i, end=' ')
        #    print()

        #print(f'count = {sum(row.count(0) for row in _grid)}')
        #print()
        return sum(row.count(0) for row in _grid)
    else:
        x, y, _type = cctvs[i]

        # Face north.
        grid = deepcopy(_grid)
        funcs[_type](x, y, 'N', grid)
        val_n = dfs(i+1, grid)

        # Face east.
        grid = deepcopy(_grid)
        funcs[_type](x, y, 'E', grid)
        val_e = dfs(i+1, grid)

        # Face south.
        grid = deepcopy(_grid)
        funcs[_type](x, y, 'S', grid)
        val_s = dfs(i+1, grid)

        # Face west.
        grid = deepcopy(_grid)
        funcs[_type](x, y, 'W', grid)
        val_w = dfs(i+1, grid)

        return min(val_n, val_e, val_s, val_w)

print(dfs(0, grid))
