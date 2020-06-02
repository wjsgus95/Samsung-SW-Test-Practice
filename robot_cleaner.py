
# Utils
int2string = { 0 : 'N', 1 : 'E', 2 : 'S', 3 : 'W' }
rotate = { 'N' : 'W', 'W' : 'S', 'S' : 'E', 'E' : 'N' }
delta = { 'N' : (-1, 0), 'W' : (0, -1), 'S' : (1, 0), 'E' : (0, 1) }

N, M = map(int, input().split())
r, c, d = map(int, input().split())

# Remember prevs
prev_r, prev_c = r, c
count = 0

direction = int2string[d]
grid = [list(map(int, input().split())) for _ in range(N)]

cleaned = [[False] * M for _ in range(N)]

is_over = False

def step1():
    cleaned[r][c] = True

def isCleanLeft():
    left = rotate[direction]
    dr, dc = delta[left]

    if 0 <= r + dr < N and 0 <= c + dc < M:
        if grid[r+dr][c+dc] != 1:
            if cleaned[r+dr][c+dc]:
                return True
            else:
                return False
        else:
            return True
    else:
        return True

def isCleanOrWallFourWays():
    for direction in delta:
        dr, dc = delta[direction]
        
        if 0 <= r + dr < N and 0 <= c + dc < M:
            if grid[r+dr][c+dc] != 1 and not cleaned[r+dr][c+dc]:
                return False

    return True

def cannotRetreat():
    dr, dc = delta[direction]
    if 0 <= r - dr < N and 0 <= c - dc < M:
        if grid[r-dr][c-dc] == 1:
            return True
        else:
            return False
    else:
        return True

def step2():
    global direction, is_over, r, c, prev_r, prev_c, count

    if isCleanOrWallFourWays():
        if cannotRetreat():
            is_over = True
            return False
        else:
            dr, dc = delta[direction]
            r, c = r - dr, c - dc
            return True

    if not isCleanLeft():
        # Rotate and advance robot
        direction = rotate[direction]
        dr, dc = delta[direction]
        r, c = r + dr, c + dc

        return False
    else:
        # Rotate robot
        direction = rotate[direction]
        step_b = True
        return True


"""
    if not isCleanLeft():
        # Rotate and advance robot
        direction = rotate[direction]
        dr, dc = delta[direction]
        r, c = r + dr, c + dc

        return False
    else:
        # Rotate robot
        direction = rotate[direction]
        step_b = True

    if isCleanOrWallFourWays() and cannotRetreat():
        is_over = True
        return False
    else:
        # Keep direction and retreat robot.
        if not step_b:
            dr, dc = delta[direction]
            r, c = r - dr, c - dc
        return True
"""

"""
    step_b = False

    if not isCleanLeft():
        # Rotate and advance robot
        direction = rotate[direction]
        dr, dc = delta[direction]
        r, c = r + dr, c + dc

        return False
    elif cnt < 4:
        if(prev_r == r and prev_c == c):
            cnt += 1
        # Rotate robot
        direction = rotate[direction]
        step_b = True

    elif isCleanOrWallFourWays() and cannotRetreat():
        cnt = 0
        is_over = True
        return False
    else:
        # Keep direction and retreat robot.
        if not step_b:
            dr, dc = delta[direction]
            r, c = r - dr, c - dc
        return True
"""

while not is_over:
    step1()
    while step2(): pass

print(sum(row.count(True) for row in cleaned))



