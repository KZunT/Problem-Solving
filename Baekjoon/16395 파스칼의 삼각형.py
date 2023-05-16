N, K = map(int, input().split())
triangle = [[] for _ in range(N)]

for i in range(0, N):
    for j in range(0, i + 1):
        if i == 0 or j == 0 or j == i:
            triangle[i].append(1)
        else:
            triangle[i].append(triangle[i - 1][j - 1] + triangle[i - 1][j])

print(triangle[N - 1][K - 1])

# dp 기본문제