# https://www.acmicpc.net/problem/15685

CCW = 3

N = int(input())
dragon_curves = [tuple(map(int, input().split())) for _ in range(N)]

def translate(coords, dx, dy):
    return [(x+dx,y+dy) for x, y in coords]

def rotate(coords, direction):
    new_coords = []
    
    for x, y in coords:
        new_x, new_y = x, y

        if direction == 3:
            new_x = -y
            new_y = x
        elif direction == 2:
            new_x = -x
            new_y = -y
        elif direction == 1:
            new_x = y
            new_y = -x
        
        new_coords.append((new_x, new_y))
    return new_coords


def getDragonCurveCoords(gen:int) -> list:
    coords = [(0, 0), (1, 0)]

    for _ in range(gen):
        end_x, end_y = coords[-1]

        new_coords = translate(coords, -end_x, -end_y)
        new_coords = rotate(new_coords, CCW)
        new_coords = translate(new_coords, end_x, end_y)

        new_coords.reverse()

        coords = coords + new_coords[1:]

    return coords


grid = [[False] * 101 for _ in range(101)]

for line in dragon_curves:
    x, y, d, g = line

    coords = getDragonCurveCoords(g)
    coords = rotate(coords, d)
    coords = translate(coords, x, y)

    for x, y in coords:
        grid[x][y] = True

square_count = 0
for x in range(100):
    for y in range(100):
        if grid[x][y] == True and grid[x][y+1] == True and grid[x+1][y] == True and grid[x+1][y+1] == True:
            square_count += 1

print(square_count)


