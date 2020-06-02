# https://www.acmicpc.net/problem/15686

from itertools import combinations

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

chicken_distances = {}
chickens = []

for r in range(N):
    for c in range(N):
        if grid[r][c] == 1:
            chicken_distances[(r,c)] = []
        elif grid[r][c] == 2:
            chickens.append((r,c))

for key in chicken_distances:
    hr, hc = key
    for cr, cc in chickens:
        chicken_distances[key].append(abs(cr - hr) + abs(cc - hc))

odds = combinations(range(len(chickens)), M)

result = 0xFFFF_FFFF
for odd in odds:
    houses = {}
    for num in odd:
        for key in chicken_distances:
            hr, hc = key
            houses[key] = min(houses.get(key, 0xFFFF_FFFF), chicken_distances[key][num])

        total_distance = sum(houses.values())
        result = min(total_distance, result)

print(result)
    
    
    
