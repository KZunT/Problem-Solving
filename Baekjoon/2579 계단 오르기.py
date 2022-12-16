N = int(input())

stage_list = [0] * 301

for i in range(N):
    stage_list[i] = int(input())

dp = [0] * 301

# 세번째 계단까지는 하드코딩

dp[0] = stage_list[0]
dp[1] = stage_list[0] + stage_list[1]
dp[2] = max(stage_list[0] + stage_list[2], stage_list[1] + stage_list[2])

# 이후 점화식
# 한 칸을 올라오거나 or 연속 두 칸을 올라오거나 중 큰 값 선택

for i in range(3, N):
    dp[i] = max(dp[i - 3] + stage_list[i - 1] + stage_list[i], dp[i - 2] + stage_list[i])

print(dp[N - 1])

# 런타임 에러 조심;
