# https://www.acmicpc.net/problem/17143

R, C, M = map(int, input().split())

up, down, right, left = 0, 1, 2, 3
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

grid = [[0] * C for _ in range(R)]
for i in range(R):
    for c in range(C):
        grid[i][c] = list()

sharks = [list(map(int, input().split())) for _ in range(M)]
for r, c, s, d, z in sharks:
    grid[r-1][c-1].append((s, d-1, z))


def move_sharks(grid):
    result = []

    def turn_around(d):
        if d == up: return down
        if d == down: return up
        if d == right : return left
        if d == left : return right

    sharks = []
    for r in range(R):
        for c in range(C):
            if len(grid[r][c]):
                assert len(grid[r][c]) == 1
                sharks.append((r, c, *(grid[r][c].pop())))

    while len(sharks):
        r, c, s, d, z = sharks.pop()

        for _ in range(s):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < R and 0 <= nc < C:
                r, c = nr, nc
            else:
                d = turn_around(d)
                r, c = r + dr[d], c + dc[d]

        result.append((r, c, s, d, z))

    for r, c, s, d, z in result:
        grid[r][c].append((s, d, z))

def eat_up(grid):
    for r in range(R):
        for c in range(C):
            if len(grid[r][c]):
                max_shark = max(grid[r][c], key=lambda v: v[2])
                new_cell =[]
                new_cell.append(max_shark)
                grid[r][c] = new_cell


score = 0
for c in range(C):
    # Catch closest shark.
    for r in range(R):
        if len(grid[r][c]):
            score += grid[r][c].pop()[2]
            #print(f'Catch: [{r}][{c}]')
            break

    # Move sharks.
    move_sharks(grid)

    # Eat up smaller ones.
    eat_up(grid)

print(score)

