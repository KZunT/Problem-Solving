N = int(input())

drink = [0] * 10000

for i in range(N):
    drink[i] = int(input())

dp = [0] * 10000
dp[0] = drink[0]
dp[1] = drink[0] + drink[1]
dp[2] = max(drink[2] + drink[0], drink[2] + drink[1], dp[1])

for i in range(3, N):  # 세가지 경우의 수 중에 선택
    dp[i] = max(drink[i] + dp[i - 2], drink[i] + drink[i - 1] + dp[i - 3], dp[i - 1])
    # 한번 쉬기 , 한번 마시기, 두번 연속 마시기

print(max(dp))
