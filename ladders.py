# https://www.acmicpc.net/problem/15684

from itertools import combinations

N, M, H = map(int, input().split())
lines = [tuple(map(int, input().split())) for _ in range(M)]

grid = [[False] * N for _ in range(H)]
for line in lines:
    h,n = line
    grid[h-1][n-1] = True

candidates = []
for h in range(H):
    for n in range(N):
        if grid[h][n] == False:
            if n == 0:
                if grid[h][n+1] == False:
                    candidates.append((h, n))
            elif 1 <= n < N - 1:
                if grid[h][n-1] == False and grid[h][n+1] == False:
                    candidates.append((h, n))
            elif n == N - 1:
                if grid[h][n-1] == False:
                    candidates.append((h, n))

odds = []
odds = odds + list(combinations(candidates, 0))
odds = odds + list(combinations(candidates, 1))
odds = odds + list(combinations(candidates, 2))
odds = odds + list(combinations(candidates, 3))


def evaluate(grid):
    def evaluate_line(line_num):
        h, n = 0, line_num

        while h < H:
            if n == 0:
                if grid[h][n] == True:
                    n += 1
            elif n == N - 1:
                if grid[h][n-1] == True:
                    n -= 1
            else:
                if grid[h][n] == True:
                    n += 1
                elif grid[h][n-1] == True:
                    n -= 1
            h += 1

        return n == line_num
    
    return all((evaluate_line(n) for n in range(N)))

def simulate(grid, odd):
    for h, n in odd:
        grid[h][n] = True

    works = evaluate(grid)

    for h, n in odd:
        grid[h][n] = False

    return works, len(odd)


min_adds = 5
for odd in odds:
    works, num_adds = simulate(grid, odd)

    if works:
        min_adds = min(num_adds, min_adds)

if min_adds > 3:
    result = -1
else:
    result = min_adds

print(result)
