from collections import deque


def bfs(x, y, rain_map):
    queue = deque()
    queue.append((x, y))
    rain_map[x][y] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        x, y = queue.popleft()  # x는 가로축 y는 세로축

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if -1 < nx < N and -1 < ny < N:
                if rain_map[nx][ny] == 1:
                    queue.append((nx, ny))
                    rain_map[nx][ny] = 0  # 방문처리


N = int(input())

graph = []
maxi = 0
result = []

for _ in range(N):
    road = list(map(int, input().split()))
    graph.append(road)
    maxi = max(maxi, max(road))

for rain in range(maxi):
    rain_map = [[0 for _ in range(N)] for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if graph[i][j] <= rain:
                rain_map[i][j] = 0
            else:
                rain_map[i][j] = 1

    for i in range(N):
        for j in range(N):
            if rain_map[i][j] == 1:
                bfs(i, j, rain_map)
                cnt += 1

    result.append(cnt)

print(max(result))