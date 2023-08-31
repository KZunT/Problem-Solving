N, S, M = map(int, input().split())

volumn = list(map(int, input().split()))

dp = [[0] * (M + 1) for i in range(N + 1)]

dp[0][S] = 1

for i in range(1, N + 1):
    for j in range(M + 1):
        if dp[i - 1][j] != 0:
            if 0 <= j + volumn[i - 1] <= M:
                dp[i][j + volumn[i - 1]] = 1
            if 0 <= j - volumn[i - 1] <= M:
                dp[i][j - volumn[i - 1]] = 1

ans = -1
dp = dp[N]

for i in range(M, -1, -1):
    if dp[i] == 1:
        ans = i
        break
print(ans)
