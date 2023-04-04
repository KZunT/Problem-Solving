N, K = map(int, input().split())

coin = [int(input()) for _ in range(N)]
dp = [100001] * (K + 1)
dp[0] = 0

# 반복문을 통해 코인으로 1부터 k를 확인
for i in coin:
    for j in range(1, K + 1):
        # 코인으로 현재 값을 만들 수 있다면 이전 값과 비교
        if j - i >= 0:
            dp[j] = min(dp[j], dp[j - i] + 1)

if dp[K] == 100001:
    print(-1)
else:
    print(dp[K])
