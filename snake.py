# https://www.acmicpc.net/problem/3190

from collections import deque

apples = set()
commands = deque()

# Directions
U, R, D, L = 0, 1, 2, 3
stringify = {0: "up", 1: 'right', 2: 'down', 3:'left'}

# Deltas
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# Rotation dictionaries
CW = {U : R, R : D, D : L, L : U}
CCW = {R : U, D : R, L : D, U : L}

# Parse board size.
n = int(input())

# Parse apples location.
k = int(input())
for _ in range(k):
    coords = tuple(map(int, input().split()))
    apples.add(coords)

# Parse commands.
l = int(input())
for _ in range(l):
    time, direction = input().split()
    time = int(time)
    commands.append((time, direction))

# Initialize snake.
current_direction = R
snake = deque()
snake.append((1,1))
current_time = 0

def isOver():
    snake_bite_itself = len(snake) != len(set(snake))
    snake_hit_wall = not(0 < snake[-1][0] <= n and 0 < snake[-1][1] <= n)

    return snake_bite_itself or snake_hit_wall

while True:
    # Update command.
    if len(commands):
        if commands[0][0] == current_time:
            time, direction = commands.popleft()
            current_direction = CCW[current_direction] if direction == 'L' else CW[current_direction]

    # Advance snake.
    hx, hy = snake[-1]
    nhx, nhy = hx + dx[current_direction], hy + dy[current_direction]
    snake.append((nhx,nhy))

    if isOver(): 
        current_time += 1
        break

    if (nhx, nhy) in apples:
        apples.remove((nhx,nhy))
    else:
        snake.popleft()

    #print(current_time, ':', snake, current_direction)
        
    # Advance current time.
    current_time += 1

print(current_time)

    
