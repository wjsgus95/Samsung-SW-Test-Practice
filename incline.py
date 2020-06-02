# https://www.acmicpc.net/problem/14890

N, L = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

def evaluate(array):
    i = 0
    inclined = [False] * N

    while i < N - 1:
        if array[i+1] - array[i] == 1:
            if 0 <= i - L + 1 and not any(inclined[i-L+1:i+1]) \
                    and all(x == array[i-L+1] for x in array[i-L+1:i+1]):
                for x in range(i-L+1, i+1):
                    inclined[x] = True
            else:
                return False
        elif array[i] - array[i+1] == 1:
            if i + L < N and not any(inclined[i+1:i+L+1]) \
                    and all(x == array[i+1] for x in array[i+1:i+L+1]):
                for x in range(i+1, i+L+1):
                    inclined[x] = True
            else:
                return False
        elif abs(array[i] - array[i+1]) > 1:
            return False

        i += 1

    return True

num_paths = 0
for x in range(N):
    row = grid[x]
    if evaluate(row):
        num_paths += 1

for y in range(N):
    column = [row[y] for row in grid]
    if evaluate(column):
        num_paths += 1

print(num_paths)
