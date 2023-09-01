N = int(input())

dp = [i for i in range(N + 1)]
dp[1] = 0

number = [i for i in range(N + 1)]
number[1] = 0

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1
    number[i] = i - 1

    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i // 3] + 1
        number[i] = i // 3
    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1
        number[i] = i // 2

print(dp[N])

print(N, end=" ")
idx = N
while number[idx] != 0:
    print(number[idx], end=" ")
    idx = number[idx]
