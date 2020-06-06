# https://www.acmicpc.net/problem/17144

R, C, T = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(R)]

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

ccw_start, cw_start = None, None
for r in range(R):
    if grid[r][0] == -1:
        if ccw_start == None:
            ccw_start = (r, 0)
        else:
            cw_start = (r, 0)

def get_ccw_routine(ccw_start):
    result = []
    r0, c0 = ccw_start

    for c in range(1, C):
        result.append((r0, c))

    for r in range(r0-1, 0, -1):
        result.append((r, C-1))

    for c in range(C-1, 0, -1):
        result.append((0, c))

    for r in range(r0+1):
        result.append((r, 0))

    return result

def get_cw_routine(cw_start):
    result = []
    r0, c0 = cw_start

    for c in range(1, C):
        result.append((r0, c))

    for r in range(r0+1, R-1):
        result.append((r, C-1))

    for c in range(C-1, 0, -1):
        result.append((R-1, c))

    for r in range(R-1, r0-1, -1):
        result.append((r, 0))

    return result

ccw_routine = get_ccw_routine(ccw_start)
cw_routine = get_cw_routine(cw_start)

ccw_routine.reverse()
cw_routine.reverse()


def spread(grid):
    # New grid for the next time step.
    ngrid = [[0] * C for _ in range(R)]

    # Copy air purifier location.
    r1, c1 = ccw_start
    r2, c2 = cw_start
    ngrid[r1][c1] = -1
    ngrid[r2][c2] = -1

    for r in range(R):
        for c in range(C):
            if grid[r][c] > 0:
                count = 0

                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]

                    if 0 <= nr < R and 0 <= nc < C:
                        if grid[nr][nc] >= 0:
                            # Spread if spreadable.
                            ngrid[nr][nc] += grid[r][c] // 5
                            # Count number of cells to spread.
                            count += 1
                
                # Put remaining finedust in the original cell.
                ngrid[r][c] += grid[r][c] - (grid[r][c] // 5) * count

    return ngrid

def circulate_ccw(grid):
    for i in range(1, len(ccw_routine) - 1):
        r, c = ccw_routine[i]
        nr, nc = ccw_routine[i+1]

        grid[r][c] = grid[nr][nc]

    # Last cell becomes zero after circulation.
    lr, lc = ccw_routine[-1]
    grid[lr][lc] = 0


def circulate_cw(grid):
    for i in range(1, len(cw_routine) - 1):
        r, c = cw_routine[i]
        nr, nc = cw_routine[i+1]

        grid[r][c] = grid[nr][nc]

    # Last cell becomes zero after circulation.
    lr, lc = cw_routine[-1]
    grid[lr][lc] = 0


def circulate(grid):
    circulate_ccw(grid)
    circulate_cw(grid)

#print(ccw_routine)
#print(cw_routine)
#test = spread(grid)
#circulate(test)
#for r in range(R):
#    print(test[r])
#exit()

# For given timesteps T.
for t in range(T):
    # Spread finedust.
    grid = spread(grid)

    # Circulate finedust.
    circulate(grid)

# Get remaining fine dust.
result = 0
for r in range(R):
    for c in range(C):
        if grid[r][c] > 0:
            result += grid[r][c]

print(result)
