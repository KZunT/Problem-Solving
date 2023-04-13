from collections import deque

def bfs():
    dx = [-1, -1, -1, 0, 1, 0, 1, 1]
    dy = [-1, 0, 1, 1, 1, -1, 0, -1]

    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if -1 < nx < N and -1 < ny < M and not graph[nx][ny]:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

queue = deque()

for i in range(N):
    for j in range(M):
        if graph[i][j]:
            queue.append((i, j))

bfs()

print(max(map(max, graph)) - 1) # 이런 방법은 처음 알았다.