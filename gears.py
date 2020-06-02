# https://www.acmicpc.net/problem/14891

NUM_GEARS = 4

R, L = 2, 6
N, S = 0, 1
CW, CCW = 1, -1

gears = [[int(x) for x in input()] for _ in range(NUM_GEARS)]

k = int(input())

# command = (target, rotation)
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Move base index to zero from one.
for i in range(len(commands)):
    commands[i] = (commands[i][0] - 1, commands[i][1])

def invert(rotation):
    if rotation == CCW:
        return CW
    elif rotation == CW:
        return CCW

def rotateGear(gear, rotation):
    if rotation == CW:
        gear.insert(0, gear.pop())
    elif rotation == CCW:
        gear.append(gear.pop(0))


def rotate(target, rotation):
    left, right = target - 1, target + 1

    while left >= 0:
        # Track which direction the gears start 
        # rotating at the left starting point.
        rotation = invert(rotation)
        left_rotate = gears[left][R] != gears[left+1][L]
        if not left_rotate: 
            rotation = invert(rotation)
            break

        left -= 1

    while right < NUM_GEARS:
        right_rotate = gears[right-1][R] != gears[right][L]
        if not right_rotate: 
            break
    
        right += 1

    for i in range(left+1, right):
        rotateGear(gears[i], rotation)
        rotation = invert(rotation)

for target, rotation in commands:
    rotate(target, rotation)

def getScore(gears):
    score = 0

    if gears[0][0] == S:
        score += 1
    if gears[1][0] == S:
        score += 2
    if gears[2][0] == S:
        score += 4
    if gears[3][0] == S:
        score += 8

    return score

print(getScore(gears))
#for gear in gears:
#    print(gear)
