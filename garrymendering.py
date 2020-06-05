# https://www.acmicpc.net/problem/17779

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

def is_valid(x, y, d1, d2):
    if 0 <= x + d1 < N and 0 <= y - d1 < N and\
       0 <= x + d2 < N and 0 <+ y + d2 < N and\
       0 <= x + d1 + d2 < N and y - d1 + d2 and\
       0 <= x + d2 + d1 < N and y + d2 - d1:
       return True
    else:
       return False

def get_districts(x0, y0, d1, d2):
    dist1 = []
    dist2 = []
    dist3 = []
    dist4 = []
    dist5 = []

    for x in range(N):
        for y in range(N):
            # District 5
            if y >= -x + x0 + y0 and\
               y <= x - x0 + y0 and\
               y >= x - x0 + y0 - 2*d1 and\
               y <= -x + x0 + y0 + 2*d2:
                   dist5.append((x, y))
            else:
                # District 1
                if y < -x + x0 + y0 and x < x0 + d1 and y <= y0:
                    dist1.append((x, y))
                # District 2
                elif y > x - x0 + y0 and x <= x0 + d2 and y0 < y:
                    dist2.append((x, y))
                # District 3
                elif y < x - x0 + y0 - 2*d1 and x0 + d1 <= x and y < y0 - d1 + d2:
                    dist3.append((x, y))
                # District 4
                elif y > -x + x0 + y0 + 2*d2 and x0 + d2 < x and y0 -d1 + d2 <= y:
                    dist4.append((x,y))

    districts = [dist1, dist2, dist3, dist4, dist5]
    return districts

def get_A(coords):
    result = 0
    for x, y in coords:
        result += A[x][y]
    return result

min_diff = 0xFFFF_FFFF_FFFF_FFFF

for x in range(N):
    for y in range(N):
        for d1 in range(1, N):
            for d2 in range(1, N):
                if is_valid(x, y, d1, d2):
                    districts = get_districts(x, y, d1, d2)

                    As = []
                    for dist in districts:
                        pass
                        pop = get_A(dist)
                        As.append(pop)

                    max_A = max(As)
                    min_A = min(As)

                    diff = max_A - min_A
                    min_diff = min(min_diff, diff)

print(min_diff)
