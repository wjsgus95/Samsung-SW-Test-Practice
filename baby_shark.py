# https://www.acmicpc.net/problem/16236

from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
count, size = 0, 2

# Get starting location.
for i in range(N):
    for j in range(N):
        if grid[i][j] == 9:
            sx, sy = i, j

# Get shark size from eaten fish count.
def get_size(count):
    size = 2
    while count - size >= 0:
        count -= size
        size += 1

    return size

# Get the list of edible fish.
def get_edibles(grid, size):
    edibles = []

    queue = deque()
    visited = [[False] * N for _ in range(N)]
    visited[sx][sy] = True
    queue.append((sx,sy, 0))

    while queue:
        x, y, d = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and grid[nx][ny] <= size:
                    visited[nx][ny] = True
                    queue.append((nx,ny, d+1))
                    if 0 < grid[nx][ny] < size:
                        edibles.append((nx,ny,d+1))

    return edibles


# Get the closest fish from list of edibles.
def get_closest_edible(grid, edibles):
    _, __, min_distance = min(edibles, key=lambda v: v[2])
    candidates = list(filter(lambda v: v[2] == min_distance, edibles))

    # Get uppermost, if many then leftmost among them.
    candidates.sort(key=lambda v:(v[0],v[1]))
    return candidates[0]
    

# Move shark to the target and return time taken.
def move_shark(grid, target):
    global sx, sy

    grid[sx][sy] = 0
    sx, sy, d = target
    grid[sx][sy] = 9
    return d


total_time = 0
target = None
while True:
    edibles = get_edibles(grid, size)
    if len(edibles) > 1:
        target = get_closest_edible(grid, edibles)
    elif len(edibles) == 1:
        target = edibles[0]
    else:
        break

    total_time += move_shark(grid, target)

    count += 1
    size = get_size(count)

print(total_time)
