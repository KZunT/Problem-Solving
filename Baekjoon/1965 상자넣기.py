N = int(input())

box_list = list(map(int, input().split()))

dp = [0 for _ in range(N)]

for i in range(1, N):
    for j in range(i):
        if box_list[i] > box_list[j]:  # 상자중 크기가 작은게 있다면 넣을 수 있으므로 변경
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp) + 1)
