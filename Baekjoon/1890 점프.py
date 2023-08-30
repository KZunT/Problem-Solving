import sys

input = sys.stdin.readline

N = int(input())
game = [list(map(int, input().split())) for _ in range(N)]

direct = [(1, 0), (0, 1)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N - 1 and j == N - 1:
            break
        dist = game[i][j]
        if i + dist < N:
            dp[i + dist][j] += dp[i][j]
        if j + dist < N:
            dp[i][j + dist] += dp[i][j]

print(dp[i][j])
