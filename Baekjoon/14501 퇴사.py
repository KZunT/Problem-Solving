N = int(input())

consult_list = []

dp = [0] * (N + 1)

for _ in range(N):
    consult_list.append(list(map(int, input().split())))

dp = [0 for _ in range(N + 1)]  # dp 생성

for i in range(N - 1, -1, -1):  # 거꾸로 반복
    #print(dp)
    if i + consult_list[i][0] > N:  # 날짜가 최대 일을 초과 한다면
        dp[i] = dp[i + 1]   # 일을 맡지 않을경우 보상
    else:   # 최대 일을 초과 하지 않으면, 현재 일을 맡았을 때 들어오는 보상 + 현재 일을 끝낸 다음날에 쌓여있는 보상 or 일을 맡지 않을 경우 보상 중 큰 값을 선택
        dp[i] = max(dp[i + 1], consult_list[i][1] + dp[i + consult_list[i][0]])

print(dp[0])
