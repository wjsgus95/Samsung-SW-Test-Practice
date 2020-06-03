# https://www.acmicpc.net/problem/17822

from collections import deque

N, M, T = map(int, input().split())
numbers = [[0] * (M + 1) for _ in range(N+1)]
for i in range(1, N+1):
    row = list(map(int, input().split()))
    for j in range(1, M+1):
        numbers[i][j] = row[j-1]
        
actions = [list(map(int, input().split())) for _ in range(T)]

def get_adj(i, j):
    result = []
    if i == 1:
        result.append((2,j)) 
    elif 2 <= i <= N-1:
        result.append((i-1,j))
        result.append((i+1,j))
    else:
        result.append((N-1,j))

    if j == 1:
        result.append((i,2))
        result.append((i,M))
    elif j == M:
        result.append((i,M-1))
        result.append((i,1))
    else:
        result.append((i,j-1))
        result.append((i,j+1))

    return result
        

def rotate_cw(numbers, i, k):
    for _ in range(k):
        numbers[i].insert(1, numbers[i].pop())

def rotate_ccw(numbers, i, k):
    for _ in range(k):
        numbers[i].append(numbers[i].pop(1))

def bfs(numbers, i, j):
    queue = deque()
    queue.append((i,j))
    
    visited = [[False] * (M + 1) for _ in range(N+1)]
    visited[i][j] = True

    val = numbers[i][j]
    if val == -1:
        return []

    while queue:
        x, y = queue.popleft()

        for nx, ny in get_adj(x,y):
            if numbers[nx][ny] == val and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True

    result = []
    for i in range(1, N+1):
        for j in range(1, M+1):
            if visited[i][j]:
                result.append((i, j))

    return result


        

for x, d, k in actions:
    x0 = x
    while x <= N:
        if d == 0:
            rotate_cw(numbers, x, k)
        else:
            rotate_ccw(numbers, x, k)
        x += x0

    found_adjacents = False
    for i in range(1, N+1):
        for j in range(1, M+1):
            search = bfs(numbers, i, j)
            if len(search) > 1:
                found_adjacents = True
                for _i, _j in search:
                    assert numbers[_i][_j] != -1
                    numbers[_i][_j] = -1
    
    if not found_adjacents:
        summation = 0
        count = 0
        for i in range(1, N+1):
            for j in range(1, M+1):
                if numbers[i][j] > 0:
                    summation += numbers[i][j]
                    count += 1

        if count == 0:
            continue
        average = summation / count
        for i in range(1, N+1):
            for j in range(1, M+1):
                if numbers[i][j] > 0 and numbers[i][j] > average:
                    numbers[i][j] -= 1
                elif numbers[i][j] > 0 and numbers[i][j] < average:
                    numbers[i][j] += 1

result = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        if numbers[i][j] > 0:
            result += numbers[i][j]

print(result)





