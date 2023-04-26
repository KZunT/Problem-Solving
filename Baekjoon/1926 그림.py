from collections import deque


def bfs(x, y):
    area = 1
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    area += 1
    return area


N, M = map(int, input().split())
visited = [[False] * M for _ in range(N)]
graph = [list(map(int, input().split())) for _ in range(N)]
picture = []

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and not visited[i][j]:
            picture.append(bfs(i, j))

print(len(picture))
print(0 if len(picture) == 0 else max(picture))