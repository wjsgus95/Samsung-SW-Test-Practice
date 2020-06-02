# https://www.acmicpc.net/problem/14502

from itertools import combinations
from copy import deepcopy
from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# Empty / Wall / Virus
E, W, V = 0, 1, 2

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

candidates = []
virus_points = []
num_walls = 3

for n in range(N):
    for m in range(M):
        if grid[n][m] == E:
            candidates.append((n,m))
        elif grid[n][m] == W:
            num_walls += 1
        else:
            virus_points.append((n,m))

def simulate(grid, odd):
    grid = deepcopy(grid)

    queue = deque(virus_points)

    visited = [[False] * M for _ in range(N)]
    for n, m in virus_points:
        visited[n][m] = True 

    for n, m in odd:
        grid[n][m] = W

    while queue:
        n, m = queue.popleft()

        for i in range(4):
            nn = n + dx[i]
            nm = m + dy[i]

            if 0 <= nn < N and 0 <= nm < M:
                if grid[nn][nm] != W and not visited[nn][nm]:
                    visited[nn][nm] = True
                    queue.append((nn,nm)) 
                    grid[nn][nm] = V

    return sum(row.count(True) for row in visited), grid

max_safe_zone = 0

odds = list(combinations(candidates, 3))
for odd in odds:
    num_virus_points, debug = simulate(grid, odd)

    safe_zone = N * M - num_walls - num_virus_points

    # DEBUG
    #if safe_zone > max_safe_zone:
    #    print(num_virus_points)
    #    for n in range(N):
    #        print(debug[n])

    max_safe_zone = max(safe_zone, max_safe_zone)

print(max_safe_zone)
    
