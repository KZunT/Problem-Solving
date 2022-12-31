N = int(input())

dp = [[0 for i in range(10)] for j in range(101)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N + 1):   # 수의 끝자리가 0,9 인경우는 이전 계단수의 끝자리가  1,8 인 경우 밖에 없다. 이외의 수는 자신의 수보다 +- 1 숫자를 통해 계단수가 만들어질 수 있다.
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[N]) % 1000000000)