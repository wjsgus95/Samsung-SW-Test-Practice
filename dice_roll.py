# https://www.acmicpc.net/problem/14499

sides = { 'T' : 0, 'B' : 0, 'E' : 0, 'W' : 0, 'N' : 0, 'S' : 0 }

n, m, x, y, k = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

num2symbol = {'1' : 'E', '2' : 'W', '3' : 'N', '4' : 'S'}
actions = [num2symbol[x] for x in input().split()]

def isOutOfBound(x, y, action):
    if action == 'E':
        return not(0 <= x < n and 0 <= y + 1 < m)
    elif action == 'W':
        return not(0 <= x < n and 0 <= y - 1 < m)
    elif action == 'N':
        return not(0 <= x - 1 < n and 0 <= y < m)
    else:
        return not(0 <= x + 1 < n and 0 <= y < m)

# Handle number transfer between dice and board.
def handleTransfer(sides, num):
    if num == 0:
        return sides['B']
    else:
        sides['B'] = num
        return 0

def rollEast(sides, num):
    # Roll the affected sides.
    sides['E'], sides['B'], sides['W'], sides['T'] = \
            sides['T'], sides['E'], sides['B'], sides['W']
    
    return handleTransfer(sides, num)

def rollWest(sides, num):
    # Roll the affected sides.
    sides['T'], sides['E'], sides['B'], sides['W'] = \
            sides['E'], sides['B'], sides['W'], sides['T']
    
    return handleTransfer(sides, num)

def rollNorth(sides, num):
    # Roll the affected sides.
    sides['N'], sides['B'], sides['S'], sides['T'] = \
            sides['T'], sides['N'], sides['B'], sides['S']
    
    return handleTransfer(sides, num)

def rollSouth(sides, num):
    # Roll the affected sides.
    sides['T'], sides['N'], sides['B'], sides['S'] = \
            sides['N'], sides['B'], sides['S'], sides['T']
    
    return handleTransfer(sides, num)


for action in actions:
    if isOutOfBound(x, y, action):
        continue

    if action == 'E':
        grid[x][y+1] = rollEast(sides, grid[x][y+1])
        y += 1
    elif action == 'W':
        grid[x][y-1] = rollWest(sides, grid[x][y-1])
        y -= 1
    elif action == 'N':
        grid[x-1][y] = rollNorth(sides, grid[x-1][y])
        x -= 1
    else:
        grid[x+1][y] = rollSouth(sides, grid[x+1][y])
        x += 1

    # DEBUG
    #print((x,y),action, grid[x][y], sides)
    #for _ in range(n):
    #    print(grid[_])

    print(sides['T'])
