N = int(input())
card_list = [0] + list(map(int, input().split()))

dp = [0] * (N+1)
dp[1] = card_list[1]
dp[2] = max(card_list[2], card_list[1]*2)

for i in range(3, N+1):
    dp[i] = card_list[i] #자기 자신으로 만드는 경우
    for j in range(1, i + 1): #j와 i-j로 만드는 경우
        dp[i] = max(dp[i], dp[j] + dp[i-j])

print(dp[N])
