# https://www.acmicpc.net/problem/14501

N = int(input())

T, P = [0], [0]
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t), P.append(p)

# DP[N]
dp = [0] * (N + 1)

for n in range(1, N+1):
    interim_max = max(dp[0:n])
    if n + T[n] <= N + 1:
        dp[n+T[n]-1] = max(interim_max + P[n], dp[n+T[n]-1])

print(max(dp))

