N = int(input())

dp = [0] * 11
dp[1] = 0
dp[2] = 1

for i in range(3, N + 1):
    temp = i // 2
    dp[i] = temp * (i - temp) + dp[temp] + dp[i - temp]

print(dp[N])

# N = int(input())
# print(N * (N-1) // 2)
