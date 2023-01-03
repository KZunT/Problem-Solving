N = int(input())

dp = [0] * 90
dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, 90):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[N - 1])
