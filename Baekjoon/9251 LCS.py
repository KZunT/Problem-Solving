s1 = input()
s2 = input()

dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        if s1[i - 1] == s2[j - 1]:  # 이전 문자열과 같다면 갱신된 LCS 길이는 이전의 LCS에 1만큼 추가
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:  # 이전 문자열과 다르다면 두 CASE를 비교하여 큰 값 을 가져온다.
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])
