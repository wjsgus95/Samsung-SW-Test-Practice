# https://www.acmicpc.net/problem/12100

from collections import deque
from copy import deepcopy

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

queue = deque()

queue.append((grid, 0))

def merge(numbers):
    len_list = len(numbers)
    i = len_list - 1
    while i > 0:
        if numbers[i] == numbers[i-1]:
            numbers[i-1] += numbers.pop(i)
            i -= 1
        i -= 1

def moveRight(grid):
    for x in range(n):
        non_zeros = list(filter(lambda v: v != 0, grid[x]))

        merge(non_zeros)

        num_zeros = n - len(non_zeros)
        grid[x] = ([0] * num_zeros) + non_zeros

def moveLeft(grid):
    for x in range(n):
        non_zeros = list(filter(lambda v: v != 0, grid[x]))

        non_zeros.reverse()
        merge(non_zeros)
        non_zeros.reverse()

        num_zeros = n - len(non_zeros)
        grid[x] = non_zeros + ([0] * num_zeros)

def moveUp(grid):
    for y in range(n):
        non_zeros = []
        for x in range(n):
            if grid[x][y] != 0:
                non_zeros.append(grid[x][y])

        non_zeros.reverse()
        merge(non_zeros)
        non_zeros.reverse()

        num_zeros = n - len(non_zeros)
        new_column = non_zeros + ([0] * num_zeros)

        for x in range(n):
            grid[x][y] = new_column[x]

def moveDown(grid):
    for y in range(n):
        non_zeros = []
        for x in range(n):
            if grid[x][y] != 0:
                non_zeros.append(grid[x][y])

        merge(non_zeros)

        num_zeros = n - len(non_zeros)
        new_column = ([0] * num_zeros) + non_zeros

        for x in range(n):
            grid[x][y] = new_column[x]



def move(grid, dx, dy):
    if dx == 1: moveRight(grid)
    if dx == -1: moveLeft(grid)
    if dy == 1: moveUp(grid)
    if dy == -1: moveDown(grid)

def turn(i, _grid):
    if i == 5:
        # Find max value.
        max_val = 0
        for x in range(n):
            max_in_row = max(_grid[x])
            max_val = max(max_val, max_in_row)
        return max_val
    else:
        max_list = []
        for j in range(4):
            grid_copy = deepcopy(_grid)
            move(grid_copy, dx[j], dy[j])
            max_list.append(turn(i+1, grid_copy))
        return max(max_list)

print(turn(0, grid))
