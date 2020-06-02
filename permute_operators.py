# https://www.acmicpc.net/problem/14888

from itertools import permutations

N = int(input())
A = list(map(int, input().split()))

num_pluses, num_mins, num_muls, num_divs = map(int, input().split())
operators = ['+'] * num_pluses + ['-'] * num_mins + \
            ['*'] * num_muls + ['/'] * num_divs

def plus(lhs, rhs):
    return lhs + rhs

def minus(lhs, rhs):
    return lhs - rhs

def multiply(lhs, rhs):
    return lhs * rhs

def divide(lhs, rhs):
    if lhs < 0:
        lhs = -lhs
        return -(lhs // rhs)
    else:
        return lhs // rhs

operation = { '+' : plus, '-' : minus, \
              '*' : multiply, '/' : divide }

odds = set(permutations(operators))

def evaluate(A, symbols):
    product = A[0]
    for i in range(N-1):
        product = operation[symbols[i]](product, A[i+1])
    
    return product

min_value = 0xFFFF_FFFF_FFFF_FFFF
max_value = -min_value

for odd in odds:
    result = evaluate(A, odd)

    min_value = min(min_value, result)
    max_value = max(max_value, result)

print(max_value)
print(min_value)

    
