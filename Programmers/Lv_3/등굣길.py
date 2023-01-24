def solution(m, n, puddles):
    answer = 0
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    dp[1][1] = 1

    # m,n 범위에 주의
    for i, j in puddles:
        dp[j][i] = -1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if dp[i][j] == -1:
                dp[i][j] = 0
                continue

            dp[i][j] += (dp[i - 1][j] + dp[i][j - 1]) % 1000000007

    for d in dp:
        print(d)
    return dp[n][m]