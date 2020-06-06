# https://www.acmicpc.net/problem/16235

dx = [0, 0, -1, 1, 1, -1, -1, 1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
init_trees = [list(map(int, input().split())) for _ in range(M)]
nutritions = [[5] * N for _ in range(N)]

trees = [[0] * N for _ in range(N)]
dead_trees = [[0] * N for _ in range(N)]

for x in range(N):
    for y in range(N):
        trees[x][y] = list()
        dead_trees[x][y] = list()

for x, y, z in init_trees:
    trees[x-1][y-1].append(z)


for k in range(K):
    # Spring
    for x in range(N):
        for y in range(N):
            if len(trees[x][y]):
                trees[x][y].sort()

                i = 0
                while i < len(trees[x][y]) and nutritions[x][y] - trees[x][y][i] >= 0:
                    nutritions[x][y] -= trees[x][y][i]
                    trees[x][y][i] += 1
                    i += 1

                for _ in range(i, len(trees[x][y])):
                    dead_trees[x][y].append(trees[x][y].pop(i))


    # Summer
    for x in range(N):
        for y in range(N):
            while len(dead_trees[x][y]):
                z = dead_trees[x][y].pop()
                nutritions[x][y] += z // 2




    # Fall
    for x in range(N):
        for y in range(N):
            for z in trees[x][y]:
                if z % 5 == 0:
                    for i in range(8):
                        nx = x + dx[i]
                        ny = y + dy[i]

                        if 0 <= nx < N and 0 <= ny < N:
                            trees[nx][ny].append(1)


    # Winter
    for x in range(N):
        for y in range(N):
            nutritions[x][y] += A[x][y]

num_trees = sum(sum(len(x) for x in row) for row in trees)
print(num_trees)
