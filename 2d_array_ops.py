# https://www.acmicpc.net/problem/17140

r, c, k = map(int, input().split())
r, c = r-1, c-1

A = [[0] * 100 for _ in range(100)]
for i in range(3):
    row = list(map(int, input().split()))
    for j in range(3):
        A[i][j] = row[j]

def is_op_C(A):
    max_x, max_y = 0, 0
    for x in range(100):
        for y in range(100):
            if A[x][y] != 0:
                if x > max_x:
                    max_x = x
                if y > max_y:
                    max_y = y

    if max_y > max_x:
        return True
    else:
        return False


def op_R(A, x):
    row = []
    i = 0
    while i < 100:
        if A[x][i] != 0:
            row.append(A[x][i])
        i += 1

    new_row = op(row)
    #if len(new_row):
    #    print(row, new_row)
    for i in range(min(len(new_row), 100)):
        A[x][i] = new_row[i]
    for i in range(len(new_row), 100):
        A[x][i] = 0

def op_C(A, y):
    col = []
    i = 0
    while i < 100:
        if A[i][y] != 0:
            col.append(A[i][y])
        i += 1

    new_col = op(col)
    #if len(new_col):
    #    print(col, new_col)
    for i in range(min(len(new_col), 100)):
        A[i][y] = new_col[i]
    for i in range(len(new_col), 100):
        A[i][y] = 0

def op(line):
    new_line = []
    count = {}

    for n in line:
        count[n] = count.get(n, 0) + 1

    for n in count:
        new_line.append((n, count[n]))

    new_line.sort(key=lambda v: (v[1], v[0]))
    result = []
    for number, count in new_line:
        result.append(number)
        result.append(count)
    return result


t = 0
flag = False
while t <= 100:
    # Check if A[r][c] == k
    if A[r][c] == k:
        flag = True
        break

    # Perform op for time step.
    if is_op_C(A):
        #print('op C')
        for y in range(100):
            op_C(A, y)
    else:
        #print('op R')
        for x in range(100):
            op_R(A, x)

    # Advance time step.
    t += 1

print(t if flag else -1)
