import sys

D, K = map(int, sys.stdin.readline().split())

for i in range(1, 100000):
    for j in range(1, 100000):
        dp = [0] * (D + 1)
        dp[1] = i
        dp[2] = j

        for k in range(3, D + 1):
            dp[k] = dp[k - 1] + dp[k - 2]

        if dp[-1] == K:
            print(dp[1])
            print(dp[2])
            exit()
