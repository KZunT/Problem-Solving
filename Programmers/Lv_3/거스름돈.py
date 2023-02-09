def solution(n, money):
    dp = [0] * (n + 1)

    for m in money:
        dp[m] += 1
        for i in range(m + 1, n + 1):
            dp[i] += dp[i - m]

    return dp[n] % 1000000007