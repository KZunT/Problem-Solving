from collections import deque


def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    graph[y][x] = 0

    while queue:
        y, x = queue.popleft()

        for dy, dx in di:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and graph[ny][nx] == -1:
                queue.append((ny, nx))
                graph[ny][nx] = graph[y][x] + 1


N = int(input())
r1, c1, r2, c2 = map(int, input().split())

graph = [[-1] * N for _ in range(N)]

di = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]
bfs(r1, c1)

print(graph[r2][c2])
