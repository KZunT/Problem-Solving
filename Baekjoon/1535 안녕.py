import sys

input = sys.stdin.readline

N = int(input())
lost = list(map(int, input().split()))
get = list(map(int, input().split()))

lost, get = [0] + lost, [0] + get
dp = [[0 for _ in range(101)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, 101):
        if lost[i] <= j:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - lost[i]] + get[i])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[N][99])
