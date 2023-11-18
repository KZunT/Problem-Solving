import sys

input = sys.stdin.readline

N = int(input().rstrip())

cur = 1
step = 1
k = 1
area = 1

INT_MAX = int(10e9)
dp = [INT_MAX] * 300001

four = [1]
dp[1] = True
dp[0] = True

while True:
    if N == area:
        print(1)
        sys.exit(0)
    if N < area:
        break
    k += 1
    cur += k
    area += cur
    four.append(area)
    if area <= 300000:
        dp[area] = 1

for i in range(1, N + 1):
    for j in four:
        if i - j > 0:
            dp[i] = min(dp[i], dp[i - j] + 1)

print(dp[N])
