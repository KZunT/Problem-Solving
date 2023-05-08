import sys

input = sys.stdin.readline

T = int(input())

dp = [1] * (10001)  # 1로는 다 나타낼 수 있기에 1로 초기화

for i in range(2, 10001):
    dp[i] += dp[i - 2]

for i in range(3, 10001):
    dp[i] += dp[i - 3]

for _ in range(T):
    num = int(input())
    print(dp[num])
