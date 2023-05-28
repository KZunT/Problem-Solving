N = int(input())

dp = [False] * 1001
dp[1] = True
dp[3] = True
dp[4] = True

for i in range(5, N + 1):
    if dp[i - 1] and dp[i - 3] and dp[i - 4]:
        dp[i] = False
    else:
        dp[i] = True

print('SK' if dp[N] else 'CY')