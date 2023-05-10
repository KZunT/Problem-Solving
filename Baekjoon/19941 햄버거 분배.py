N, K = map(int, input().split())
loc = list(input())
cnt = 0

for idx in range(N):
    if loc[idx] == 'P':
        for j in range(max(idx - K, 0), min(idx + K + 1, N)):  # 신기하다.
            if loc[j] == 'H':
                loc[j] = 0
                cnt += 1
                break

print(cnt)
