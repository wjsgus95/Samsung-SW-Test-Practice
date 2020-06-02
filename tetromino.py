# https://www.acmicpc.net/problem/14500

import math

X,Y = 0,1

given_shapes = [[(0,0), (0,1), (0,2), (0,3)], [(0,0), (0,1), (1,0), (1,1)], \
                [(0,0), (0,1), (0,2), (1,2)], [(0,0), (1,0), (1,1), (2,1)], \
                [(0,0), (0,1), (0,2), (1,1)]]

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


def toOrigin(shape):
    min_x = min(shape, key=lambda coord: coord[X])[X]
    min_y = min(shape, key=lambda coord: coord[Y])[Y]

    org_shape = []
    for coord in shape:
        org_shape.append((coord[X] - min_x, coord[Y] - min_y))

    return org_shape

def rot90(shape):
    rot_shape = []
    for x, y in shape:
        rot_x, rot_y = y, x
        rot_shape.append((rot_x, rot_y))

    return rot_shape

def rot180(shape):
    rot_shape = []
    for x, y in shape:
        rot_x, rot_y = -x, -y
        rot_shape.append((rot_x, rot_y))

    return rot_shape

def rot270(shape):
    rot_shape = []
    for x, y in shape:
        rot_x, rot_y = y, -x
        rot_shape.append((rot_x, rot_y))

    return rot_shape

def rot360(shape):
    return shape

def invertX(shape):
    inv_shape = []
    for x, y in shape:
        inv_shape.append((x, -y))

    return inv_shape

def invertY(shape):
    inv_shape = []
    for x, y in shape:
        inv_shape.append((-x, y))

    return inv_shape

def isShapeFit(shape, x, y):
    min_x = min(shape, key=lambda coord: coord[X])[X]
    min_y = min(shape, key=lambda coord: coord[Y])[Y]

    max_x = max(shape, key=lambda coord: coord[X])[X]
    max_y = max(shape, key=lambda coord: coord[Y])[Y]

    return 0 <= min_x + x  and 0 <= min_y + y and \
           max_x + x < n and max_y + y < m

def getSum(shape, x, y):
    sum_val = 0
    for dx, dy in shape:
        sum_val += grid[x + dx][y + dy]

    return sum_val


transformations = [rot90, rot180, rot270, rot360]

shapes = []
for transform in transformations:
    for shape in given_shapes:
        shapes.append(toOrigin(transform(shape)))

        shapes.append(toOrigin(invertX(transform(shape))))
        shapes.append(toOrigin(invertY(transform(shape))))

max_val = 0
for x in range(n):
    for y in range(m):
        for shape in shapes:
            if isShapeFit(shape, x, y):
                val = getSum(shape, x, y)
                #if val > max_val:
                #    print('max at', x, y, 'val =', val)
                max_val = max(max_val, val)

print(max_val)
