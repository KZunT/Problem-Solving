N, K = map(int, input().split())
coins = []
dp = [0 for i in range(K + 1)]
dp[0] = 1

for i in range(N):
    coins.append(int(input()))

for i in coins:
    for j in range(1, K + 1):
        if j - i > -1:
            dp[j] += dp[j - i]
print(dp[K])