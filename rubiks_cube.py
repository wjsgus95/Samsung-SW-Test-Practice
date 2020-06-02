# https://www.acmicpc.net/problem/5373

from collections import OrderedDict
from copy import deepcopy

# Each side's grid size constant
SIDE_GRID_SIZE = 3
# Each side's initial status (side repr : color)
SIDE_INIT = {'U' : 'w', 'D' : 'y', 'F' : 'r', 'B' : 'o', 'L' : 'g', 'R' : 'b'}

# Rotation definitions
CW, CCW = '+', '-'

# Other sides given in clockwise rotation order. (from top-view)
# Tuple(side, correlated coordinates in clockwise order)
ADJ_SIDES_INIT = OrderedDict({
    'U' : [('F', [(2,2), (2,1), (2,0)]), ('L', [(2,2), (2, 1), (2, 0)]), ('B', [(2,2), (2,1), (2,0)]), ('R', [(2,2), (2,1), (2,0)])], #
    'D' : [('F', [(0,0), (0,1), (0,2)]), ('R', [(0,0), (0, 1), (0, 2)]), ('B', [(0,0), (0,1), (0,2)]), ('L', [(0,0), (0,1), (0,2)])], #
    'F' : [('U', [(0,0), (0,1), (0,2)]), ('R', [(2,0), (1, 0), (0, 0)]), ('D', [(2,0), (2,1), (2,2)]), ('L', [(0,2), (1,2), (2,2)])], #
    'B' : [('U', [(2,2), (2,1), (2,0)]), ('L', [(2,0), (1, 0), (0, 0)]), ('D', [(0,2), (0,1), (0,0)]), ('R', [(0,2), (1,2), (2,2)])], #
    'R' : [('U', [(0,2), (1,2), (2,2)]), ('B', [(2,0), (1, 0), (0, 0)]), ('D', [(0,0), (1,0), (2,0)]), ('F', [(0,2), (1,2), (2,2)])], #
    'L' : [('U', [(2,0), (1,0), (0,0)]), ('F', [(2,0), (1, 0), (0, 0)]), ('D', [(2,2), (1,2), (0,2)]), ('B', [(0,2), (1,2), (2,2)])], #
})

class RubiksSide:
    def __init__(self, which):
        color = SIDE_INIT[which]
        self.grid = [[color] * SIDE_GRID_SIZE for _ in range(SIDE_GRID_SIZE)]
        self.adj_sides = OrderedDict()
        self.which = which

    def __repr__(self):
        return self.which

    def __getitem__(self, key):
        return self.grid[key]

    def setAdjSides(self, others:list):
        for other in others:
            side, correlated = other
            self.adj_sides[side] = correlated

    def print(self):
        for r in range(SIDE_GRID_SIZE-1, -1, -1):
            print("".join(self.grid[r]))

    def _rotateSides(self, rotation):
        sides = None
        if rotation == CW:
            sides = self.adj_sides
        elif rotation == CCW:
            # ADJ_SIDES_INIT defaults to CW rotation.
            sides = OrderedDict()
            for side in reversed(self.adj_sides):
                sides[side] = deepcopy(self.adj_sides[side])
                sides[side].reverse()

        rotating_cells = []
        for side in sides:
            correlated = sides[side]
            for r, c in correlated:
                rotating_cells.append(side[r][c])

        rotating_cells = rotating_cells[-3:] + rotating_cells[:-3]
        
        for side in sides:
            correlated = sides[side]
            for r, c in correlated:
                side[r][c] = rotating_cells.pop(0)


    def _rotateSelf(self, rotation):
        involved = [(2,0), (2,1), (2,2), (1,2), (0,2), (0,1), (0,0), (1,0)]

        if rotation == CCW:
            involved.reverse()
        elif rotation == CW:
            pass
        else: raise ValueError

        if self.which == 'D':
            involved.reverse()
        
        cells = []
        for r, c in involved:
            cells.append(self[r][c])

        cells = cells[-2:] + cells[0:-2]

        for r, c in involved:
            self[r][c] = cells.pop(0)

    def rotate(self, rotation):
        self._rotateSides(rotation)
        self._rotateSelf(rotation)



class RubiksCube:
    def __init__(self):
        self.sides = {}

        # Initialize all 6 sides.
        for side_str in SIDE_INIT:
            self.sides[side_str] = RubiksSide(side_str)

        # Connect each side to it's adjacent sides.
        for side_str in self.sides:
            adj_sides = []

            for adj_side_str, correlated in ADJ_SIDES_INIT[side_str]:
                adj_sides.append((self.sides[adj_side_str], correlated))

            self.sides[side_str].setAdjSides(adj_sides)

    def __getitem__(self, key):
        return self.sides[key]

    def rotate(self, side_str, rotation):
        self.sides[side_str].rotate(rotation)

        color_counts = {}
        for side_str in self.sides:
            side = self.sides[side_str]
            for r in range(3):
                for c in range(3):
                    color_counts[side[r][c]] = color_counts.get(side[r][c], 0) + 1

        for c in color_counts:
            assert color_counts[c] == 9

    # DEBUG
    def print(self):
        print(' ' * 3, end='')
        print(''.join(self.sides['U'][2]))
        print(' ' * 3, end='')
        print(''.join(self.sides['U'][1]))
        print(' ' * 3, end='')
        print(''.join(self.sides['U'][0]))

        for i in range(2, -1, -1):
            print(''.join(self.sides['L'][i]), end='')
            print(''.join(self.sides['F'][i]), end='')
            print(''.join(self.sides['R'][i]), end='')
            print(''.join(self.sides['B'][i]))

        print(' ' * 3, end='')
        print(''.join(reversed(self.sides['D'][2])))
        print(' ' * 3, end='')
        print(''.join(reversed(self.sides['D'][1])))
        print(' ' * 3, end='')
        print(''.join(reversed(self.sides['D'][0])))


# Parse input.
num_test_cases = int(input())
for test_case in range(num_test_cases):
    cube = RubiksCube()

    num_rotations = int(input())
    actions = [(s[0], s[1]) for s in input().split()]

    # Perform rotations.
    for side_str, rotation in actions:
        cube.rotate(side_str, rotation)    

    # Print top side.
    cube['U'].print()
    #cube.print()


