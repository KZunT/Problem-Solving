import sys

input = sys.stdin.readline

N = int(input())
power = [int(x) for x in input().split()]
dp = [1] * N

for i in range(N):
    for j in range(i):
        if power[i] < power[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(len(power) - max(dp))
