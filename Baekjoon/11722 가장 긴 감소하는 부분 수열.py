N = int(input())
array = list(map(int, input().split()))

dp = [1] * N

for i in range(1,N):
    for j in range(i):
        if array[j] > array[i]: # 반복하면서 감소하는 수열 중 최대길이를 찾음
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))