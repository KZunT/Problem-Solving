from collections import deque

M, N, K = map(int, input().split())
graph = [[0] * N for _ in range(M)]

for _ in range(K):      # 직사각형 그리기
    x1, y1, x2, y2 = map(int, input().split())      # 왼쪽 아래가 (0,0)
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 1
    size = 1    # 구해지는 너비 사이즈

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < M and -1 < ny < N and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                queue.append((nx, ny))
                size += 1
    result.append(size)

result = []

for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            bfs(i, j)

result.sort()

print(len(result))

for i in result:
    print(i, end=' ')