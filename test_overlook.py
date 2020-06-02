# https://www.acmicpc.net/problem/13458

import math

# n = number of test cites
n = int(input())
# List of number of students in each test cite
test_cites = list(map(int, input().split()))

# Main/sub director coverage of overlook (in # students)
main_coverage, sub_coverage = map(int, input().split())

num_directors = n

def divRoundUp(x, y):
    return (x + y - 1) // y

for i in range(n):
    test_cites[i] -= main_coverage
    if test_cites[i] > 0:
        num_directors += (test_cites[i] + sub_coverage - 1) // sub_coverage

print(num_directors)
    


