from collections import deque

def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == graph[x][y] and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx, ny))


N = int(input())
graph = [list(input()) for _ in range(N)]

visited = [[0] * N for _ in range(N)]
color = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS(i,j)
            color += 1

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited = [[0] * N for _ in range(N)]
color_weak = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS(i, j)
            color_weak += 1

print(color, color_weak)
