N = int(input())

dp = [1] * 10

for i in range(1, N):   # 1부터 반복하는 이유는 숫자 0이 맨 뒤에 오는 경우는 1으로 고정이기 때문이다.
    for j in range(1, 10):
        dp[j] += dp[j - 1]

print(sum(dp) % 10007)
